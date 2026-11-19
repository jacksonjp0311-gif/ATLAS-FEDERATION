"""Compiler Design v0.2: independent recursive-descent parser for Tiny-I32.

Algorithmic oracle for the Pratt parser in core.py. Reuses ONLY the lexical
scanner and immutable AST datatypes; no call to core.Parser or core.parse.
Thus it tests precedence/associativity and ambiguity handling, not lexing.
"""
from __future__ import annotations
from .core import (lex, CompileError, Lit, Var, Unary, Binary, If, Let,
                   Program, MAX_I32, MAX_DEPTH, MAX_SLOTS)
import re

_IDENTIFIER=re.compile(r'[A-Za-z_][A-Za-z_0-9]*\Z')
_NUMBER=re.compile(r'[0-9]+\Z')
_RESERVED=frozenset(('let','return','if','then','else','true','false'))

class ReferenceParser:
    def __init__(self,source):
        self.tokens=lex(source)
        self.pos=0
        self.depth=0
        self.prefix_depth=0
    def peek(self):
        return self.tokens[self.pos].text
    def consume(self,word=None):
        token=self.tokens[self.pos]
        if word is not None and token.text!=word:
            raise CompileError(f'reference grammar expected {word!r} at {token.offset}; got {token.text!r}')
        self.pos+=1
        return token.text
    def identifier(self):
        v=self.peek()
        if v in _RESERVED or not _IDENTIFIER.fullmatch(v):
            raise CompileError(f'expected source identifier at {self.tokens[self.pos].offset}')
        return self.consume()
    def parse(self):
        stmts=[]
        while self.peek()=='let':
            self.consume('let')
            name=self.identifier()
            self.consume('=')
            v=self.expression()
            self.consume(';')
            stmts.append(Let(name,v))
            if len(stmts)>MAX_SLOTS:raise CompileError('local budget exceeded')
        self.consume('return')
        result=self.expression()
        self.consume(';')
        self.consume('<EOF>')
        return Program(tuple(stmts),result)
    def expression(self):
        self.depth+=1
        if self.depth>MAX_DEPTH:raise CompileError('reference parser depth exceeded')
        try: return self.compare()
        finally:self.depth-=1
    def compare(self):
        v=self.sum()
        while self.peek() in ('<','=='):
            op=self.consume()
            v=Binary(op,v,self.sum())
        return v
    def sum(self):
        v=self.product()
        while self.peek() in ('+','-'):
            op=self.consume()
            v=Binary(op,v,self.product())
        return v
    def product(self):
        v=self.prefix()
        while self.peek() in ('*','/'):
            op=self.consume()
            v=Binary(op,v,self.prefix())
        return v
    def prefix(self):
        self.prefix_depth+=1
        if self.prefix_depth>MAX_DEPTH:raise CompileError('prefix nesting exceeded')
        try:return self._prefix_inner()
        finally:self.prefix_depth-=1
    def _prefix_inner(self):
        v=self.peek()
        if v=='-':
            self.consume('-')
            return Unary('-',self.prefix())
        if v=='(':
            self.consume('(')
            r=self.expression()
            self.consume(')')
            return r
        if v=='if':
            self.consume('if')
            cond=self.expression()
            self.consume('then')
            yes=self.expression()
            self.consume('else')
            no=self.expression()
            return If(cond,yes,no)
        if v=='true' or v=='false':
            self.consume()
            return Lit(v=='true')
        if _NUMBER.fullmatch(v):
            value=int(self.consume())
            if value>MAX_I32:raise CompileError('literal out of i32 range')
            return Lit(value)
        if _IDENTIFIER.fullmatch(v) and v not in _RESERVED:
            return Var(self.consume())
        raise CompileError(f'unexpected token {v!r} at {self.tokens[self.pos].offset}')

def parse_reference(source):
    return ReferenceParser(source).parse()

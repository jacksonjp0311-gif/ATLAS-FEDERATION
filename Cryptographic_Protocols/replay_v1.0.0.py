"""Finite anti-replay acceptance model; authenticate before calling accept()."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ReplayWindow:
    width: int = 64
    high: int = -1
    seen: int = 0

    def __post_init__(self) -> None:
        if type(self.width) is not int or not 1 <= self.width <= 4096:
            raise ValueError("invalid replay window width")
        if type(self.high) is not int or not (-1 <= self.high < 2**64):
            raise ValueError("invalid stored high water mark")
        if type(self.seen) is not int or not (0 <= self.seen < (1 << self.width)):
            raise ValueError("invalid stored replay bitmap")

    def accept(self, seq: int) -> bool:
        if type(seq) is not int or not 0 <= seq < 2**64:
            raise ValueError("invalid sequence number")
        if self.high < 0:
            self.high, self.seen = seq, 1
            return True
        if seq > self.high:
            shift = seq - self.high
            self.seen = ((self.seen << shift) | 1) & ((1 << self.width) - 1)
            self.high = seq
            return True
        offset = self.high - seq
        if offset >= self.width or ((self.seen >> offset) & 1):
            return False
        self.seen |= 1 << offset
        return True

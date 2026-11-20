"""ATLAS FORGE Software Design Patterns v0.1.0, original federation.

Offline recovery patterns are finite educational references, not validated
life-safety software, physically fault-tolerant machinery, or secure systems.
"""
from .contracts import envelope,parse_envelope,digest,canonical_bytes,ContractError
from .state import StateMachine,Transition,recovery_machine,TransitionError
from .resilience import CircuitBreaker,Bulkhead,bounded_retry,Rejected

"""Offline combined casebook. No cloud, model or network calls."""
import json
from .v1_cases import casebook_v1
print(json.dumps(casebook_v1(),indent=2,default=str))

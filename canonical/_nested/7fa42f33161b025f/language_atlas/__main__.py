"""Offline Language Atlas casebook CLI."""
import json
from .cases import casebook
print(json.dumps(casebook(),ensure_ascii=False,indent=2))

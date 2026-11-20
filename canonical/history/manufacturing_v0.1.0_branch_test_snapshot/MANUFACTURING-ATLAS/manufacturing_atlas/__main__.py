import json
from .cases import casebook
print(json.dumps(casebook(),indent=2))

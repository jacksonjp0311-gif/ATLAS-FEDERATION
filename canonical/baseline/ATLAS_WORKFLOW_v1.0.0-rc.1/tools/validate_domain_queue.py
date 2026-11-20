import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"DOMAIN_QUEUE.json"
a=json.loads(p.read_text())
assert len(a["candidates"])==30
assert len({x["node_id"] for x in a["candidates"]})==30
assert [x["priority"] for x in a["candidates"]]==list(range(1,31))
assert [x["node_id"] for x in a["candidates"] if x["status"].startswith("active")]==["measurement-atlas"]
assert not a["next_domain_allowed"]
print("Domain queue verified: 30 candidates; Measurement only active")

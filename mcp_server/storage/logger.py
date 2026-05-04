import json
from datetime import datetime, timezone


class MCPLogger:
    def __init__(self, filepath="logs/mcp.log"):
        self.filepath = filepath

    def log(self, data: dict):
        entry = {
            "timestamp" : datetime.now(timezone.utc).isoformat(),
            **data
        }
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry)+ "\n")
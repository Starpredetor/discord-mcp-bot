


class PolicyEngine:
    def __init__(self):
        
        # DEFAULT Policy map
        self.policies = {
            # Safe actions
            "MESSAGE_CREATE" : "ALLOW",
            "MESSAGE_LIST" : "ALLOW",
            "MESSAGE_FETCH" : "ALLOW",
            "MESSAGE_EDIT" : "ALLOW",

            # Controlled actions
            "MESSAGE_DELETE" : "ASK",

            # Denied actions (temp)
            "MESSAGE_BULK_DELETE" : "DENY",

        }

    def evaluate(self, route: str, params:dict) -> str:
        return self.policies.get(route, "DENY")
from mcp_server.discord_api.client import DiscordClient
from mcp_server.discord_api import endpoints as ep
from mcp_server.core.route_map import ROUTE_MAP
from mcp_server.core.policy_engine import PolicyEngine

class MCPExecutor:
    def __init__(self, token):
        self.client = DiscordClient(token)
        self.policy = PolicyEngine()


    async def execute(self, route: str, params: dict, body: dict = None):

        #Policy Check
        decision = self.policy.evaluate(route, params)        

        if decision == "DENY":
            return {"error" : f"Denied by policy: {route}"}
        
        if decision == "ASK":
            return {
                "status" : "approval_required",
                "route" : route,
                "params" : params
            }


        #Route Config
        config = ROUTE_MAP.get(route)

        if not config:
            return {"error" : f"Unknown route {route}"}
        

        method = config["method"]
        endpoint = config["endpoint"](params)

        # Execution Dispatch
        if method == "GET":
            return await self.client.get(endpoint)

        if method == "POST":
            return await self.client.post(endpoint, json=body)

        if method == "PATCH":
            return await self.client.patch(endpoint, json=body)

        if method == "PUT":
            return await self.client.put(endpoint, json=body)

        if method == "DELETE":
            return await self.client.delete(endpoint)


        return {"error" : "Invalid Method"}
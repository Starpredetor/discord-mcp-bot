from mcp_server.discord_api.client import DiscordClient
from mcp_server.discord_api import endpoints as ep
from mcp_server.core.route_map import ROUTE_MAP
from mcp_server.core.policy_engine import PolicyEngine
from mcp_server.storage.logger import MCPLogger
from mcp_server.core.approval_manager import ApprovalManager

class MCPExecutor:
    def __init__(self, token):
        self.client = DiscordClient(token)
        self.policy = PolicyEngine()
        self.logger = MCPLogger()
        self.approvals = ApprovalManager()


    async def execute(self, route: str, params: dict, body: dict = None):


        #Policy Check
        decision = self.policy.evaluate(route, params)        
        self.logger.log({
            "route" : route,
            "params" : params,
            "decision" : decision,
            "status" : "policy_checked"
        })

        if decision == "DENY":

            self.logger.log({
            "route": route,
            "status": "denied"
            })

            return {"error" : f"Denied by policy: {route}"}
        
        if decision == "ASK":

            request_id = self.approvals.create_request(route,params,body)

            self.logger.log({
            "route": route,
            "status": "pending_approval"
            })  
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
        try:
            if method == "GET":
                result = await self.client.get(endpoint)
            elif method == "POST":
                result = await self.client.post(endpoint, json=body)
            elif method == "PATCH":
                result = await self.client.patch(endpoint, json=body)
            elif method == "PUT":
                result = await self.client.put(endpoint, json=body)
            elif method == "DELETE":
                result = await self.client.delete(endpoint)
            else:
                return {"error": "Invalid method"}

            #Execution success
            self.logger.log({
                "route": route,
                "status": "success"
            })

            return result

        except Exception as e:
            #Error log
            self.logger.log({
                "route": route,
                "status": "error",
                "error": str(e)
            })

        return {"error": str(e)}
    
    async def approve(self, request_id: str):
        request = self.approvals.get_request(request_id)

        if not request:
            return {"error" : "Invalid or expired request"}
        
        route = request["route"]
        params = request["params"]
        body = request["body"]

        self.approvals.remove_request(request_id)
        self.logger.log({
            "route": route,
            "status": "request_approved"
            })
        return await self.execute(route, params, body)

    def deny(self, request_id: str):
        request = self.approvals.get_request(request_id)
    
        if not request:
            return {"error": "Invalid or expired request"}
    
        self.approvals.remove_request(request_id)
        
        self.logger.log({
            "request": request_id,
            "status": "request_denied"
            }) 
    
        return {"status": "denied", "request_id": request_id}
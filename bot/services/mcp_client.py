import httpx

MCP_URL = "http://127.0.0.1:8000"


class MCPClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def execute(self, route, params, body=None):
        res = await self.client.post(
            f"{MCP_URL}/execute",
            json={
                "route" : route,
                "params" : params,
                "body" : body
                }
            )
        return res.json()
    
    async def approve(self, request_id):
        res = await self.client.post(
            f"{MCP_URL}/approve",
            json={"request_id" : request_id}
        )
        return res.json()
    
    async def deny(self, request_id):
        res = await self.client.post(
            f"{MCP_URL}/deny",
            json={"request_id" : request_id}
        )
        return res.json()
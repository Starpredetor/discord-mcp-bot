import httpx
import asyncio



BASE_URL = "https://discord.com/api/v10"

class DiscordClient:
    def __init__(self, token: str):
        self.client = httpx.AsyncClient(
            base_url=BASE_URL,
            headers={
                "Authorization" : f"Bot {token}",
                "Content-Type" : "application/json"
            }
        )
    
    async def request(self, method: str, endpoint: str, json=None):
        while True:
            response = await self.client.request(
                method,
                endpoint,
                json=json
            )

            # Rate limiter logic
            if response.status_code == 429:
                retry = response.json().get("retry_after", 1)
                await asyncio.sleep(retry)
                continue

            if response.status_code >= 400:
                return {
                    "error" : response.text,
                    "status" : response.status_code
                }
            if response.status_code == 204:
                return {"status": "success", "code": 204}
            
            return response.json()
        
        """Basic HTTP I/O functionality"""
    async def get(self, endpoint):
        return await self.request("GET", endpoint)

    async def post(self, endpoint, json=None):
        return await self.request("POST", endpoint, json)
    
    async def patch(self, endpoint, json=None):
        return await self.request("PATCH", endpoint, json)
    
    async def put(self, endpoint, json=None):
        return await self.request("PUT", endpoint, json)
    
    async def delete(self, endpoint):
        return await self.request("DELETE", endpoint)
        
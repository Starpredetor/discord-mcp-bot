from fastapi import FastAPI
from pydantic import BaseModel
from mcp_server.core.executor import MCPExecutor
import os, dotenv

dotenv.load_dotenv()

app = FastAPI()
executor = MCPExecutor(os.getenv("BOT_TOKEN"))

class ExecuteRequest(BaseModel):
    route: str
    params: dict
    body: dict | None = None
    
class ApprovalRequest(BaseModel):
    request_id: str
    
 
 
#Routes   
@app.post("/execute")
async def execute(req: ExecuteRequest):
    return await executor.execute(req.route, req.params, req.body)


@app.post("/approve")
async def approve(req: ApprovalRequest):
    return await executor.approve(req.request_id)


@app.post("/deny")
async def deny(req: ApprovalRequest):
    return executor.deny(req.request_id)
# Discord MCP Bot

A modular Discord bot powered by a custom MCP (Model Control Plane) backend that enables controlled, policy-driven automation of Discord actions.

Instead of directly executing commands, all actions go through an MCP layer that enforces:
- Policy checks (ALLOW / ASK / DENY)
- Approval workflows for sensitive actions
- Logging of all operations

---

## Features

- Custom Discord API client (no heavy abstractions)
- Route-based execution system (intent → execution separation)
- Policy engine (risk-based control)
- Approval system (button-based interaction in Discord)
- Structured logging (JSON logs)
- Fully asynchronous architecture

---

## Architecture

Discord → Bot → MCP Server  
      ↓  
    Policy Engine  
      ↓  
  ASK → Approval UI → Approve/Deny  
      ↓  
  Executor → Discord API

---

## Getting Started

### 1. Clone the repository

git clone <your-repo-url>  
cd discord-mcp-bot

---

### 2. Create a virtual environment
```bash
python -m venv .venv
```
Activate it:
```bash
#Windows command prompt:
.venv\Scripts\activate.bat  

#Windows Powershell
.venv\Scripts\Activate.ps1

#Linux/macOS:
source .venv/bin/activate  
```
---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---

### 4. Configure bot token

Add your Discord bot token in:

mcp_server/main.py

(And in your bot config if applicable.)

---

### 5. Run MCP server

```bash
uvicorn mcp_server.main:app --reload
```

Server will run at:
http://127.0.0.1:8000

---

### 6. Run Discord bot

```bash
python bot/main.py
```
---

## Example Flow

1. Trigger a command in Discord  
2. MCP evaluates policy  
3. If sensitive → approval buttons appear  
4. Approve → action executes  
5. Logs are recorded  

---

## Project Structure

mcp_server/
  core/          # executor, policy, approval logic  
  discord_api/   # raw Discord API client + endpoints  
  storage/       # logging  

bot/
  interactions/  # UI components (buttons/views)  
  services/      # MCP client  

---

## Current Limitations

- In-memory approvals (lost on restart)
- Limited endpoint coverage (messages only)
- No role-based policies yet
- No LLM integration (planned)

---

## Future Plans

- LLM-based command parsing
- Role-based and per-guild policies
- Persistent storage (database)
- Expanded Discord API coverage

---

## Summary

This project acts as a controlled automation layer for Discord, bridging user intent and API execution through policies and approvals.
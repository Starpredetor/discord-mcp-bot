import discord

class ApprovalView(discord.ui.View):
    def __init__(self, mcp_client, request_id):
        super().__init__(timeout=60)
        self.mcp = mcp_client
        self.request_id = request_id
        
    @discord.ui.button(label="Approve", style=discord.ButtonStyle.green)
    async def approve(self, button: discord.ui.Button, interaction: discord.Interaction):
        res = await self.mcp.approve(self.request_id)
        self.disable_all_items()
        await self.message.edit(content="✅ Action Approved", view=self)
        await interaction.response.send_message(f"Approved: {res}", ephemeral=True)
        
    @discord.ui.button(label="Deny", style=discord.ButtonStyle.red)
    async def deny(self, button: discord.ui.Button, interaction: discord.Interaction):
        res = await self.mcp.deny(self.request_id)
        self.disable_all_items()
        await self.message.edit(content="❌ Action Denied", view=self)
        await interaction.response.send_message(f"Denied: {res}", ephemeral=True)
    
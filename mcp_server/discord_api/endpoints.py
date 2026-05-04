"""All MASTER Endpoints required for MCP interaction with the discord API"""


"""Messages Endpoints from API Reference"""

# GET
def get_messages(channel_id):
    return f"/channels/{channel_id}/messages"

# GET (for single messsage)
def fetch_message(channel_id, message_id):
    return f"/channels/{channel_id}/messages/{message_id}"

#POST
def create_message(channel_id):
    return f"/channels/{channel_id}/messages"

#PATCH
def edit_message(channel_id, message_id):
    return f"/channels/{channel_id}/messages/{message_id}"

#DELETE
def delete_message(channel_id, message_id):
    return f"/channels/{channel_id}/messages/{message_id}"

#POST
def bulk_delete_messages(channel_id):
    return f"/channels/{channel_id}/messages/bulk-delete"

#PUT
def add_reaction(channel_id, message_id, emoji_id):
    return f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji_id}/@me"

#DELETE
def remove_self_reaction(channel_id, message_id, emoji_id):
    return f"/channels/{channel_id}/messages/{message_id}/reactions/{emoji_id}/@me"


""""""
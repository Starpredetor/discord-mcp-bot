from mcp_server.discord_api import endpoints as ep

ROUTE_MAP = {
    # -------- MESSAGES --------
    "MESSAGE_CREATE": {
        "method": "POST",
        "endpoint": lambda p: ep.create_message(p["channel_id"])
    },

    "MESSAGE_LIST": {
        "method": "GET",
        "endpoint": lambda p: ep.list_messages(p["channel_id"])
    },

    "MESSAGE_FETCH": {
        "method": "GET",
        "endpoint": lambda p: ep.fetch_message(
            p["channel_id"],
            p["message_id"]
        )
    },

    "MESSAGE_DELETE": {
        "method": "DELETE",
        "endpoint": lambda p: ep.delete_message(
            p["channel_id"],
            p["message_id"]
        )
    },

    "MESSAGE_EDIT": {
        "method": "PATCH",
        "endpoint": lambda p: ep.edit_message(
            p["channel_id"],
            p["message_id"]
        )
    },

    "MESSAGE_BULK_DELETE": {
        "method": "POST",
        "endpoint": lambda p: ep.bulk_delete_messages(
            p["channel_id"]
        )
    },
}
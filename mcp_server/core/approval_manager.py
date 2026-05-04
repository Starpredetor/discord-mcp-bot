import uuid


class ApprovalManager:
    def __init__(self):
        self.pending = {
            # stores all pending requets
        }

    
    def create_request(self, route, params, body):
        request_id = str(uuid.uuid4())

        self.pending[request_id] = {
            "route" : route,
            "params" : params,
            "body" : body
        }

        return request_id

    def get_request(self, request_id):
        return self.pending.get(request_id)
    
    def remove_request(self, request_id):
        if request_id in self.pending:
            del self.pending[request_id]
            
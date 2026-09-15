import json, sys
from client import AutonomousRefundDisputeArbitratorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "refund-dispute-arbitrator", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "arbitrate_dispute_case", "description": "Arbitrates customer refund and dispute claims based on evidence and policies."}]}}
    elif method == "tools/call":
        client = AutonomousRefundDisputeArbitratorClient()
        res = client.arbitrate_dispute_case()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AutonomousRefundDisputeArbitratorClient()
        print(json.dumps(client.arbitrate_dispute_case(), indent=2))

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutonomousRefundDisputeArbitratorClient

def main():
    client = AutonomousRefundDisputeArbitratorClient()
    res = client.arbitrate_dispute_case()
    print("=== Autonomous Refund Dispute Arbitrator Output ===")
    print(f"Order: {res['order_id']} | Eligibility Score: {res['eligibility_score']}/100")
    print(f"Verdict: {res['arbitrated_verdict']}")
    print(f"Settlement Action: {res['recommended_settlement_action']}")
    print(f"Evidence Hash: {res['evidence_proof_hash']}")

if __name__ == '__main__':
    main()

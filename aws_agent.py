import boto3
import json
from getpass import getpass

def create_session():
    print("=== AWS Login Required ===")
    access_key = input("Enter AWS Access Key: ").strip()
    secret_key = getpass("Enter AWS Secret Key: ").strip()
    region = input("Enter AWS Region (default: us-east-1): ").strip() or "us-east-1"

    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    return session

def get_user_info(session):
    sts = session.client("sts")
    iam = session.client("iam")

    identity = sts.get_caller_identity()
    arn = identity["Arn"]

    username = arn.split("/")[-1]

    print("\n===== BASIC INFO =====")
    print("User ARN:", arn)
    print("Account ID:", identity["Account"])

    try:
        user = iam.get_user(UserName=username)
        print("User Created:", user["User"]["CreateDate"])
    except:
        print("User Type: Role or Federated user")

    return username, arn

def list_policies(session, username):
    iam = session.client("iam")

    print("\n===== ATTACHED MANAGED POLICIES =====")
    attached = iam.list_attached_user_policies(UserName=username)
    for p in attached["AttachedPolicies"]:
        print("-", p["PolicyName"])

    print("\n===== INLINE POLICIES =====")
    inline = iam.list_user_policies(UserName=username)
    for p in inline["PolicyNames"]:
        print("-", p)

def check_groups(session, username):
    iam = session.client("iam")
    print("\n===== GROUP MEMBERSHIP =====")
    groups = iam.list_groups_for_user(UserName=username)
    if not groups["Groups"]:
        print("No groups attached.")
    for g in groups["Groups"]:
        print("-", g["GroupName"])

def simulate_permissions(session, arn):
    iam = session.client("iam")

    print("\n===== PERMISSION CHECK =====")

    actions = [
        "ec2:RunInstances",
        "s3:CreateBucket",
        "rds:CreateDBInstance",
        "lambda:CreateFunction",
        "iam:CreateUser"
    ]

    response = iam.simulate_principal_policy(
        PolicySourceArn=arn,
        ActionNames=actions
    )

    for r in response["EvaluationResults"]:
        print(f"{r['EvalActionName']} → {r['EvalDecision']}")

def detect_admin(session, arn):
    iam = session.client("iam")

    response = iam.simulate_principal_policy(
        PolicySourceArn=arn,
        ActionNames=["*"]
    )

    allowed = any(r["EvalDecision"] == "allowed" for r in response["EvaluationResults"])

    print("\n===== ADMIN CHECK =====")
    if allowed:
        print("⚠️ This user MAY have broad administrative privileges.")
    else:
        print("This user is NOT full admin.")

def main():
    session = create_session()
    username, arn = get_user_info(session)
    list_policies(session, username)
    check_groups(session, username)
    simulate_permissions(session, arn)
    detect_admin(session, arn)

if __name__ == "__main__":
    main()

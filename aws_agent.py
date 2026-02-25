import boto3
from datetime import datetime

# ANSI Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    print(f"""{CYAN}{BOLD}
====================================================
        AWS IAM AUDIT AGENT
        Security Permission Scanner
====================================================
{RESET}""")

def create_session():
    print(f"{YELLOW}Using AWS CLI configured credentials...{RESET}")
    # Automatically uses credentials from `aws configure`
    return boto3.Session()

def get_user_info(session):
    sts = session.client("sts")
    iam = session.client("iam")

    identity = sts.get_caller_identity()
    arn = identity["Arn"]
    username = arn.split("/")[-1]

    print(f"\n{CYAN}{BOLD}===== BASIC INFO ====={RESET}")
    print(f"{GREEN}User ARN:{RESET} {arn}")
    print(f"{GREEN}Account ID:{RESET} {identity['Account']}")

    try:
        user = iam.get_user(UserName=username)
        print(f"{GREEN}Created:{RESET} {user['User']['CreateDate']}")
    except:
        print(f"{YELLOW}User Type: Role or Federated user{RESET}")

    return username, arn

def list_policies(session, username):
    iam = session.client("iam")

    print(f"\n{CYAN}{BOLD}===== ATTACHED MANAGED POLICIES ====={RESET}")
    attached = iam.list_attached_user_policies(UserName=username)
    if not attached["AttachedPolicies"]:
        print(f"{RED}No managed policies attached{RESET}")
    for p in attached["AttachedPolicies"]:
        print(f"{GREEN}✔{RESET} {p['PolicyName']}")

    print(f"\n{CYAN}{BOLD}===== INLINE POLICIES ====={RESET}")
    inline = iam.list_user_policies(UserName=username)
    if not inline["PolicyNames"]:
        print(f"{RED}No inline policies{RESET}")
    for p in inline["PolicyNames"]:
        print(f"{GREEN}✔{RESET} {p}")

def check_groups(session, username):
    iam = session.client("iam")
    print(f"\n{CYAN}{BOLD}===== GROUP MEMBERSHIP ====={RESET}")
    groups = iam.list_groups_for_user(UserName=username)
    if not groups["Groups"]:
        print(f"{RED}No groups attached{RESET}")
    for g in groups["Groups"]:
        print(f"{GREEN}✔{RESET} {g['GroupName']}")

def simulate_permissions(session, arn):
    iam = session.client("iam")
    print(f"\n{CYAN}{BOLD}===== PERMISSION CHECK ====={RESET}")

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
        action = r['EvalActionName']
        decision = r['EvalDecision']
        if decision.lower() == "allowed":
            print(f"{GREEN}[ALLOWED]{RESET} {action}")
        else:
            print(f"{RED}[DENIED]{RESET} {action}")

def detect_admin(session, username):
    iam = session.client("iam")

    # Simplest way: check if attached policies include AdministratorAccess
    attached = iam.list_attached_user_policies(UserName=username)
    policy_names = [p["PolicyName"] for p in attached["AttachedPolicies"]]

    is_admin = any("AdministratorAccess" in p for p in policy_names)

    print(f"\n{CYAN}{BOLD}===== ADMIN CHECK ====={RESET}")
    if is_admin:
        print(f"{RED}⚠️ This user MAY have full administrative privileges.{RESET}")
    else:
        print(f"{GREEN}This user is NOT full admin.{RESET}")

def security_best_practices():
    print(f"\n{CYAN}{BOLD}🔒 Security Best Practices{RESET}")
    print("- Never commit AWS credentials")
    print("- Use environment variables or aws configure")
    print("- Apply least-privilege principle")
    print("- Rotate access keys regularly")

def future_roadmap():
    print(f"\n{CYAN}{BOLD}🧠 Future Roadmap{RESET}")
    print("- Dockerized version")
    print("- Scheduled IAM audit via GitHub Actions")
    print("- Slack / Teams alert integration")
    print("- HTML report generation")
    print("- Risk scoring system")
    print("- AI-based policy explanation")
    print("- Privilege escalation detection module")

def author_info():
    print(f"\n{CYAN}{BOLD}👨‍💻 Author{RESET}")
    print("Muhammad Imran Bashir")
    print("DevOps Engineer | AWS | Docker | CI/CD | Infrastructure Automation")

def license_info():
    print(f"\n{CYAN}{BOLD}📜 License{RESET}")
    print("MIT License")

def main():
    banner()
    session = create_session()
    username, arn = get_user_info(session)
    list_policies(session, username)
    check_groups(session, username)
    simulate_permissions(session, arn)
    detect_admin(session, username)
    security_best_practices()
    future_roadmap()
    author_info()
    license_info()
    print(f"\n{YELLOW}Scan Completed at {datetime.now()}{RESET}\n")

if __name__ == "__main__":
    main()

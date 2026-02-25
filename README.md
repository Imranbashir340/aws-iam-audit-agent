# 🔐 AWS IAM Audit Agent

A professional-grade AWS IAM permission auditing tool built using Python and boto3.

This tool analyzes the effective permissions of the currently authenticated AWS principal and helps identify over-privileged access, security gaps, and administrative risks.

---

## 🚀 Project Overview

Cloud security starts with visibility.

The AWS IAM Audit Agent programmatically inspects IAM configurations and simulates permissions to determine what actions a user can actually perform.

It answers critical security questions:

- Do I have EC2 launch privileges?
- Can this user create IAM users?
- Is this account over-privileged?
- Does it violate least-privilege principles?

---

## 🏗 Architecture

User → Python Agent → AWS STS → AWS IAM → Policy Simulation → Structured Report

---

## ✨ Features

- Detects authenticated AWS identity using STS
- Lists attached managed policies
- Lists inline policies
- Detects group memberships
- Simulates critical AWS service permissions:
  - EC2
  - S3
  - RDS
  - Lambda
  - IAM
- Detects potential administrative privileges
- Generates a clear permission summary

---

## 🛠 Tech Stack

- Python 3.9+
- boto3
- AWS IAM APIs
- AWS STS
- Policy Simulation Engine

---

## 📦 Installation

Clone repository:
cd aws-iam-audit-agent

Install dependencies:
Install dependencies

pip install -r requirements.txt

Configure AWS CLI (never hardcode credentials)

aws configure

Provide:

AWS Access Key ID

AWS Secret Access Key

Default region (e.g., us-east-1)

Default output format (json)

Usage

Run the agent:

python aws_agent.py

Output example:

====================================================
        AWS IAM AUDIT AGENT
        Security Permission Scanner
====================================================

===== BASIC INFO =====
User ARN: arn:aws:iam::123456789:user/devops-user
Account ID: 123456789
Created: 2023-05-01 12:30:45

===== ATTACHED MANAGED POLICIES =====
✔ AmazonEC2FullAccess
✔ IAMReadOnlyAccess

===== INLINE POLICIES =====
✔ CustomInlinePolicy

===== GROUP MEMBERSHIP =====
✔ DevOpsTeam

===== PERMISSION CHECK =====
[ALLOWED] ec2:RunInstances
[DENIED] s3:CreateBucket
[ALLOWED] rds:CreateDBInstance
[DENIED] lambda:CreateFunction
[DENIED] iam:CreateUser

===== ADMIN CHECK =====
This user is NOT full admin.

🔒 Security Best Practices
- Never commit AWS credentials
- Use environment variables or aws configure
- Apply least-privilege principle
- Rotate access keys regularly

🧠 Future Roadmap
- Dockerized version
- Scheduled IAM audit via GitHub Actions
- Slack / Teams alert integration
- HTML report generation
- Risk scoring system
- AI-based policy explanation
- Privilege escalation detection module

👨‍💻 Author
Muhammad Imran Bashir
DevOps Engineer | AWS | Docker | CI/CD | Infrastructure Automation

📜 License
MIT License

Scan Completed at 2026-02-25 22:45:10

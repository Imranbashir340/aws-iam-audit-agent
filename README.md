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

pip install -r requirements.txt
python aws_agent.py
python aws_agent.py

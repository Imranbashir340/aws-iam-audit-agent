# AWS IAM Audit Agent

A lightweight AWS IAM auditing tool that analyzes effective permissions of the currently authenticated user.

## Features

- Detects current AWS principal via STS
- Lists attached managed policies
- Lists inline policies
- Checks group membership
- Simulates permissions for critical services
- Detects potential admin privileges
- Generates structured permission summary

## Architecture

User → Python Agent → AWS STS → AWS IAM → Policy Simulation → Report

## Requirements

- Python 3.9+
- AWS Access Key & Secret Key
- IAM permissions:
  - iam:GetUser
  - iam:ListAttachedUserPolicies
  - iam:ListUserPolicies
  - iam:ListGroupsForUser
  - iam:SimulatePrincipalPolicy
  - sts:GetCallerIdentity

## Installation

```bash
pip install -r requirements.txt

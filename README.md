# Enterprise Oracle WebLogic Engineering

**Oracle Database 12.2.0.1 → 19.3.0 → 19.32**  
**Oracle WebLogic Server 14.1.1**

Terraform • Ansible • AWS • Oracle Multitenant • RMAN • WLST • JDBC

---

## Overview

Enterprise Oracle WebLogic Engineering is a production-style Oracle platform engineering project demonstrating the provisioning, automation, administration, integration, and modernization of an enterprise Oracle Database and WebLogic environment on AWS.

The project begins with an Oracle Database 12.2.0.1 platform integrated with Oracle WebLogic Server 14.1.1 and a Java EE application.

The database is then upgraded in place to Oracle 19c, patched to 19.32, and re-integrated with WebLogic.

### Modernization Flow

```text
AWS
 │
 ├── Terraform
 │
 └── Ansible
      │
      ▼
 RHEL 8
      │
      ├── Oracle Database 12.2.0.1
      │      │
      │      └── WEBLOGIC12C PDB
      │
      └── WebLogic Server 14.1.1
             │
             ├── AdminServer
             ├── tinacloudMS1
             └── tinacloudMS2
                    │
                    │ JDBC
                    ▼
              app_user
After modernization:

Oracle Database 12.2.0.1
          │
          │ In-Place Upgrade
          ▼
      Oracle 19.3.0
          │
          │ Patch
          ▼
      Oracle 19.32
          │
          │ JDBC
          ▼
 WebLogic Server 14.1.1
Project Objectives
Provision AWS infrastructure using Terraform
Configure Oracle and Linux infrastructure using Ansible
Deploy Oracle Database 12.2.0.1 Enterprise Edition
Configure Oracle Multitenant CDB/PDB architecture
Deploy Oracle WebLogic Server 14.1.1
Configure the tinacloud WebLogic domain
Configure AdminServer and multiple Managed Servers
Configure JDBC connectivity between WebLogic and Oracle
Deploy and validate a Java EE application
Protect the database with RMAN
Perform an in-place Oracle 12c → 19c upgrade
Patch Oracle 19c to 19.32
Perform post-upgrade validation
Upgrade the Oracle RDBMS time zone files
Reconnect WebLogic to the upgraded database
Validate application functionality after modernization
Technology Stack
Cloud & Infrastructure
AWS
Amazon VPC
Amazon EC2
Amazon EBS
IAM
Security Groups
Bastion Host
CloudWatch
Infrastructure & Automation
Terraform
Terraform Remote State
Ansible
Bash
SQL*Plus
GitHub Actions
Oracle Database
Oracle Database 12.2.0.1
Oracle Database 19.3.0
Oracle Database 19.32
Oracle Multitenant
CDB/PDB
RMAN
Oracle Data Pump
Oracle Net Services
Database Patching
Database Upgrades
Time Zone Management
WebLogic
Oracle WebLogic Server 14.1.1
WebLogic Domains
AdminServer
Managed Servers
Node Manager
WLST
JDBC Data Sources
JDBC Connection Pools
Java EE
WebLogic Environment

Domain: tinacloud

Component	Name
Administration Server	AdminServer
Managed Server 1	tinacloudMS1
Managed Server 2	tinacloudMS2

The WebLogic environment provides centralized administration, Node Manager lifecycle management, multiple Managed Servers, JDBC connectivity, and Java EE application deployment.

Database Architecture
ORCL12C
   │
   ├── PDB$SEED
   │
   └── WEBLOGIC12C
          │
          └── app_user

The application data is based on the V1 Oracle/WebLogic platform, allowing V2 to demonstrate a realistic database modernization rather than an empty upgrade.

Project Phases
Phase 1 — Infrastructure

Terraform provisions the AWS environment including networking, EC2, storage, IAM, security groups, and bastion infrastructure.

Phase 2 — Configuration

Ansible configures RHEL, Oracle prerequisites, storage, Oracle configuration, networking, and WebLogic prerequisites.

Phase 3 — Initial Platform

Deploy:

Oracle Database 12.2.0.1
CDB/PDB architecture
Application user and data
WebLogic Server 14.1.1
tinacloud domain
AdminServer
Managed Servers
Node Manager
JDBC Data Sources
Java EE application
Phase 4 — Stabilization

Operate and validate the integrated 12c/WebLogic environment before beginning the database upgrade.

Phase 5 — Database Modernization
12.2.0.1
   │
   ▼
19.3.0
   │
   ▼
19.32

Includes:

Pre-upgrade validation
RMAN backup
In-place upgrade
CDB/PDB upgrade
Component validation
Invalid object remediation
Time zone upgrade
Oracle 19c patching
Phase 6 — WebLogic Re-Integration

Reconnect WebLogic 14.1.1 to Oracle 19.32 and validate:

JDBC connectivity
Connection pools
Managed Servers
Node Manager
Application startup
Database access
Application functionality
Automation Architecture
GitHub
   │
GitHub Actions
   │
   ├── Terraform
   │      └── AWS Infrastructure
   │
   └── Ansible
          └── RHEL / Oracle / WebLogic Configuration

WLST  → WebLogic Automation
RMAN  → Database Protection
SQL   → Database Administration & Validation
Repository Structure
enterprise-oracle-weblogic-engineering/
│
├── docs/
├── terraform/
├── ansible/
├── oracle/
├── weblogic/
├── scripts/
├── monitoring/
├── screenshots/
└── README.md
Skills Demonstrated

Oracle DBA

Oracle installation and configuration
CDB/PDB administration
RMAN backup and recovery
Oracle Data Pump
Database upgrades and patching
Oracle Net Services
Time zone management
Performance diagnostics
Database troubleshooting

WebLogic

Domain administration
AdminServer
Managed Servers
Node Manager
JDBC configuration
Connection pools
WLST automation
Java EE deployment

Platform Engineering

AWS
Terraform
Ansible
Infrastructure as Code
Configuration Management
GitHub Actions
Linux administration
Automation
V1 → V2
V1 — Platform Foundation

Established the Oracle 19c + WebLogic 14.1.1 enterprise platform, including:

AWS infrastructure
Terraform
Oracle 19c
WebLogic 14.1.1
Java EE application
JDBC integration
RMAN
WebLogic administration
V2 — Enterprise Modernization

Extends V1 into a realistic database lifecycle scenario:

Oracle 12.2.0.1
      │
      ▼
WebLogic 14.1.1 Integration
      │
      ▼
Stabilization
      │
      ▼
In-Place Oracle Upgrade
      │
      ▼
Oracle 19.3.0
      │
      ▼
19.32
      │
      ▼
WebLogic Re-Integration
      │
      ▼
Application Validation
Why This Project?

Enterprise databases and middleware are tightly coupled.

A database upgrade can affect JDBC connectivity, connection pools, application compatibility, PDB availability, database objects, authentication, and application transactions.

This project demonstrates the complete lifecycle:

Provision
   ↓
Configure
   ↓
Integrate
   ↓
Validate
   ↓
Operate
   ↓
Backup
   ↓
Upgrade
   ↓
Patch
   ↓
Reintegrate
   ↓
Validate

The goal is to demonstrate modern Oracle platform engineering rather than treating the database as an isolated system.

Author

Tina Collins

Oracle Database Administrator • Oracle Platform Engineer • DevOps Engineer

Oracle • WebLogic • AWS • Terraform • Ansible • RMAN • WLST • Java EE • Linux • GitHub Actions

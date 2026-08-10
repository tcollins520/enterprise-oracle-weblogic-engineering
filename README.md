# Enterprise Oracle WebLogic Engineering

Oracle Database 12.2.0.1 → 19c  
Oracle WebLogic Server 14.1.1  
Terraform • Ansible • AWS • Oracle Multitenant • RMAN • WLST

---

# Overview

Enterprise Oracle WebLogic Engineering is a production-style Oracle platform engineering project demonstrating the design, provisioning, automation, integration, modernization, and operational management of an enterprise Oracle Database and Oracle WebLogic Server environment on AWS.

The project focuses on a realistic enterprise modernization scenario:

1. Provision the AWS infrastructure using Terraform.
2. Configure the Linux and Oracle platform using Ansible.
3. Deploy Oracle Database 12.2.0.1.
4. Deploy Oracle WebLogic Server 14.1.1.
5. Configure the WebLogic domain and Managed Servers.
6. Create and configure Oracle Multitenant PDBs.
7. Connect WebLogic applications to Oracle Database 12.2.0.1.
8. Validate the integrated environment.
9. Operate the environment for a stabilization period.
10. Perform an in-place Oracle Database 12.2.0.1 → 19c upgrade.
11. Apply Oracle 19c patching to reach 19.32.
12. Revalidate the upgraded database.
13. Reconnect and validate WebLogic against Oracle 19c.
14. Verify application functionality and database connectivity.

The goal is to demonstrate how an enterprise Oracle database and middleware platform can be modernized while maintaining application integration and operational continuity.

---

# Project Objectives

The primary objectives of this project are to demonstrate:

- Enterprise Oracle Database administration
- Oracle WebLogic Server administration
- Oracle Multitenant architecture
- Infrastructure as Code
- Configuration Management
- Oracle database upgrades
- Oracle database patching
- WebLogic database integration
- JDBC configuration
- WLST automation
- Node Manager administration
- RMAN backup and recovery
- Linux administration
- AWS cloud infrastructure
- Enterprise middleware validation
- Production-style operational procedures
- Repeatable infrastructure and configuration

---

# Modernization Scenario

This project simulates a real-world enterprise database modernization.

The WebLogic application initially operates against:

```text
Oracle Database 12.2.0.1
        │
        │ JDBC
        ▼
WebLogic Server 14.1.1

After the database modernization:

Oracle Database 19c
19.3 baseline
        │
        │ patched
        ▼
Oracle Database 19.32
        │
        │ JDBC
        ▼
WebLogic Server 14.1.1
``

The application and middleware platform are validated before and after the database upgrade.

This allows the project to demonstrate not only how to upgrade Oracle Database, but also how to manage the dependencies between the database and enterprise middleware platform.

```
Platform Architecture
                           GitHub
                              │
                              │
                       GitHub Actions
                              │
                              ▼
                         Terraform
                              │
                              ▼
                       AWS Infrastructure
                              │
             ┌────────────────────────────────┐
             │                                │
             │              VPC               │
             │                                │
             │   ┌──────────────┐             │
             │   │   Bastion    │             │
             │   └──────┬───────┘             │
             │          │                     │
             │          │                     │
             │   ┌──────▼──────────┐          │
             │   │   Oracle DB     │          │
             │   │                 │          │
             │   │ Oracle 12.2.0.1 │          │
             │   │      CDB        │          │
             │   │                 │          │
             │   │ ┌─────────────┐ │          │
             │   │ │ WEBLOGIC12C │ │          │
             │   │ │     PDB     │ │          │
             │   │ └─────────────┘ │          │
             │   └───────┬─────────┘          │
             │           │                    │
             │           │ JDBC                │
             │           │                    │
             │   ┌───────▼─────────┐           │
             │   │   WebLogic      │           │
             │   │    14.1.1       │           │
             │   │                 │           │
             │   │    tinacloud     │           │
             │   │      Domain      │           │
             │   │                 │           │
             │   │ ┌─────────────┐ │           │
             │   │ │ AdminServer │ │           │
             │   │ └─────────────┘ │           │
             │   │                 │           │
             │   │ ┌─────────────┐ │           │
             │   │ │tinacloudMS1 │ │           │
             │   │ └─────────────┘ │           │
             │   │                 │           │
             │   │ ┌─────────────┐ │           │
             │   │ │tinacloudMS2 │ │           │
             │   │ └─────────────┘ │           │
             │   └─────────────────┘           │
             │                                │
             └────────────────────────────────┘

              Terraform → Infrastructure
              Ansible  → Configuration
              WLST     → WebLogic Automation
              RMAN     → Database Protection
```
Technology Stack
Cloud Platform
Amazon Web Services
Amazon VPC
Amazon EC2
Amazon EBS
IAM
Security Groups
Bastion Host
CloudWatch
Infrastructure as Code
Terraform
Terraform Remote State
Modular Terraform architecture
Environment-specific variables
AWS infrastructure provisioning
Configuration Management
Ansible
Ansible Playbooks
Ansible Roles
Bash
Shell scripting
Operating System
Red Hat Enterprise Linux 8
Oracle Database
Initial Platform
Oracle Database 12.2.0.1 Enterprise Edition
Oracle Multitenant
CDB/PDB architecture
Oracle Net Services
RMAN
Oracle Data Pump
SQL*Plus
Modernized Platform
Oracle Database 19c
Oracle Database 19.3 baseline
Oracle Database 19.32 patched release
Oracle Multitenant
CDB/PDB architecture
Oracle Database upgrade tooling
Oracle RDBMS time zone management
Oracle WebLogic
Oracle WebLogic Server 14.1.1
WebLogic Domain Administration
AdminServer
Managed Servers
Node Manager
WLST
JDBC Data Sources
JDBC Connection Pools
Java EE application deployment
Application
Java EE
Apache Maven
Enterprise Middleware Validation Dashboard
Oracle Database integration
Automation
Terraform
Ansible
WLST
Bash
GitHub Actions
WebLogic Domain

The WebLogic environment uses the following domain configuration:

Domain:
tinacloud

AdminServer:
AdminServer

Managed Server 1:
tinacloudMS1

Managed Server 2:
tinacloudMS2

The domain is configured to provide a production-style WebLogic administration model with:

Centralized domain administration
Node Manager
AdminServer
Multiple Managed Servers
Application deployment
JDBC connectivity
Database-backed application integration
Database Architecture

The Oracle database uses a multitenant architecture.
```
ORACLE DATABASE
       │
       ▼
     CDB
  ORCL12C
       │
       ├── PDB$SEED
       │
       └── WEBLOGIC12C
```

The application database environment uses:

Application User:
app_user

The database contains application data based on the V1 environment so that the V2 project can demonstrate a realistic modernization scenario rather than an empty database upgrade.

Day 1 — Initial Enterprise Platform

The first stage establishes the original enterprise environment.

```
Terraform
    │
    ▼
AWS Infrastructure
    │
    ▼
RHEL 8
    │
    ├── Oracle Database 12.2.0.1
    │       │
    │       └── WEBLOGIC12C PDB
    │
    └── WebLogic Server 14.1.1
            │
            ├── AdminServer
            ├── tinacloudMS1
            └── tinacloudMS2
```

Day 1 activities include:

Provision AWS infrastructure
Configure networking
Provision EC2 instances
Configure EBS storage
Configure security groups
Configure RHEL
Install Oracle Database 12.2.0.1
Create CDB/PDB architecture
Create app_user
Load application data
Install WebLogic Server 14.1.1
Create tinacloud domain
Configure AdminServer
Configure ManagedServer1
Configure ManagedServer2
Configure Node Manager
Configure JDBC Data Sources
Deploy the Java EE application
Validate application/database connectivity
Day 2 — Oracle Database Modernization

After the 12c environment has been validated and stabilized, the database modernization begins.

The database upgrade follows an in-place modernization strategy:

```
Oracle 12.2.0.1
      │
      │ In-Place Upgrade
      ▼
Oracle 19c
      │
      │ Patch
      ▼
Oracle 19.32
```

The upgrade process includes:

Pre-upgrade validation
RMAN backup
Control file backup
SPFILE backup
Oracle upgrade readiness checks
Database shutdown
Oracle 19c environment activation
startup upgrade
catctl.pl upgrade execution
CDB$ROOT upgrade
PDB upgrade
Component validation
Object recompilation
Invalid-object investigation
Post-upgrade validation
Oracle time zone upgrade
Final database validation
Upgrade Validation

The upgrade is validated at multiple levels.

Database
Database:
ORCL12C

Version:
Oracle Database 19c

Patch Level:
19.32
Instance
Instance:
ORCL12C

Status:
OPEN
PDBs
PDB$SEED
WEBLOGIC12C
Components

Oracle component registry is validated for:

CATPROC
CATALOG
JAVAVM
CATJAVA
XDB
XML
SDO
ORDIM
OWM
OLS
DV
CONTEXT
XOQ
APS
Invalid Objects

Application-owned invalid objects are validated after the upgrade.

The goal is:

```
Application Invalid Objects
        │
        ▼
        0
Oracle Time Zone Upgrade
```

The Oracle 19c environment is also validated for RDBMS time zone compatibility.

The modernization includes:

```
DSTv26
   │
   │ Oracle DST Upgrade
   ▼
DSTv45
```
The upgrade is validated using Oracle's time zone upgrade utilities.

WebLogic Re-Integration

After the database upgrade and patching are complete, the WebLogic platform is validated against the modernized Oracle database.

```
WebLogic 14.1.1
       │
       │ JDBC
       ▼
Oracle Database 19c
       │
       ▼
Oracle 19.32

```
Validation includes:

Database connectivity
JDBC Data Source connectivity
Connection pool validation
Application startup
Application database access
Managed Server health
Node Manager health
AdminServer health
Application functionality

The objective is to demonstrate that the enterprise middleware platform can continue operating against the modernized Oracle database.

```
Automation Architecture
                   GitHub
                      │
                      ▼
             GitHub Actions
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
          Terraform          Ansible
              │                │
              ▼                ▼
       AWS Infrastructure   OS / Oracle
                              Configuration
                                  │
                                  ▼
                         Oracle Database
                                  │
                                  ▼
                         WebLogic Platform

```
Terraform is responsible for infrastructure provisioning.

Ansible is responsible for configuration and repeatable platform setup.

WLST is used for WebLogic administration and automation.

Bash and SQL scripts are used for Oracle operational procedures.

Terraform Responsibilities

Terraform provisions the AWS infrastructure required for the platform.

Responsibilities include:

VPC
Subnets
Route Tables
Internet/NAT connectivity as required
Security Groups
IAM
EC2 instances
EBS storage
Bastion infrastructure
Database infrastructure
Middleware infrastructure
Environment configuration

Example structure:

```
terraform/
├── bootstrap/
│
└── environments/
    └── production/
        ├── backend.tf
        ├── bastion.tf
        ├── compute.tf
        ├── iam.tf
        ├── keypair.tf
        ├── locals.tf
        ├── network.tf
        ├── outputs.tf
        ├── security.tf
        ├── storage.tf
        ├── terraform.tfvars
        ├── userdata.sh
        ├── variables.tf
        ├── versions.tf
        └── vpc-endpoints.tf
```       
Ansible Responsibilities

Ansible provides repeatable configuration management for the Oracle platform.

Responsibilities include:

RHEL configuration
Oracle prerequisites
Filesystem configuration
Oracle users and groups
Environment configuration
Oracle software configuration
Database configuration
Listener configuration
Oracle Net configuration
PDB configuration
WebLogic prerequisites
Middleware configuration
Managed Server configuration
Operational automation

Ansible is also used to automate the creation and configuration of additional PDB environments required by the WebLogic platform.

Oracle Administration

The project demonstrates enterprise Oracle DBA responsibilities including:

Oracle installation
Database creation
CDB/PDB administration
User administration
Oracle Net configuration
Listener administration
RMAN backup
RMAN recovery
Data Pump
Database upgrades
Database patching
Time zone management
Invalid object management
Component validation
Database health checks
Performance diagnostics
SQL troubleshooting
WebLogic Administration

The project demonstrates enterprise middleware administration including:

WebLogic installation
Domain creation
AdminServer administration
Managed Server administration
Node Manager configuration
JDBC Data Source configuration
JDBC connection pools
Application deployment
WLST automation
Server lifecycle management
Middleware health validation
Database integration
Backup & Recovery

RMAN is used to provide database protection and upgrade safety.

Pre-upgrade protection includes:

```
RMAN
 │
 ├── Database Backup
 │
 ├── Control File Backup
 │
 └── SPFILE Backup
 ```

The upgrade process is designed around the principle that a production database should have a validated recovery path before major lifecycle operations.

Validation Strategy

Validation is performed throughout the project rather than only at the end.

Infrastructure Validation
AWS resources
Network connectivity
EC2 instances
Storage
Security groups
Database Validation
Database status
Instance status
CDB/PDB status
Listener status
Component registry
Invalid objects
Database connectivity
Middleware Validation
AdminServer
Managed Servers
Node Manager
JDBC Data Sources
Application deployment
Application health
Upgrade Validation

```
12.2.0.1
   │
   ├── Pre-upgrade checks
   ├── RMAN backup
   ├── In-place upgrade
   ├── PDB validation
   ├── Component validation
   ├── Object recompilation
   ├── DST upgrade
   └── Final validation
          │
          ▼
        19c
          │
          ▼
        19.32
          │
          ▼
     WebLogic Validation
```
Engineering Principles

This project follows modern enterprise platform engineering principles.

Infrastructure as Code
Configuration as Code
Automation First
Repeatable Deployments
Least Privilege
Security by Design
Operational Excellence
Production Readiness
Disaster Recovery
Observability
Upgrade Safety
Validation-Driven Operations
Documentation as Code

# Project Progress

🚧 **Status:** Actively Under Development

| Phase | Status |
|--------|--------|
Project Architecture	✅ Complete
Terraform AWS Infrastructure	⏳ In Progress
RHEL Configuration	⏳ Planned
Oracle 12.2.0.1 Installation	⏳ Planned
Oracle CDB/PDB Configuration	⏳ Planned
Application User/Data Load	⏳ Planned
WebLogic 14.1.1 Installation	⏳ Planned
tinacloud Domain	⏳ Planned
AdminServer	⏳ Planned
tinacloudMS1	⏳ Planned
tinacloudMS2	⏳ Planned
Node Manager	⏳ Planned
JDBC Integration	⏳ Planned
Java EE Application	⏳ Planned
12c Platform Validation	⏳ Planned
Stabilization Period	⏳ Planned
RMAN Pre-Upgrade Backup	⏳ Planned
Oracle 12c → 19c Upgrade	⏳ Planned
Oracle 19c Patching → 19.32	⏳ Planned
Post-Upgrade Validation	⏳ Planned
DST Upgrade	⏳ Planned
WebLogic 19c Re-Integration	⏳ Planned
Application Validation	⏳ Planned
Performance Testing	⬜ Planned
Monitoring & Observability	⬜ Planned
Disaster Recovery Exercise	⬜ Planned
Production Runbooks	⬜ Planned
Repository Structure
```
enterprise-oracle-weblogic-engineering/
│
├── docs/
│   ├── architecture/
│   ├── installation/
│   ├── administration/
│   ├── upgrades/
│   ├── troubleshooting/
│   ├── runbooks/
│   └── diagrams/
│
├── terraform/
│   ├── bootstrap/
│   └── environments/
│       └── production/
│
├── ansible/
│   ├── inventories/
│   ├── playbooks/
│   ├── roles/
│   └── group_vars/
│
├── oracle/
│   ├── installation/
│   ├── database/
│   ├── cdb-pdb/
│   ├── network/
│   ├── rman/
│   ├── datapump/
│   ├── upgrades/
│   ├── patching/
│   ├── timezone/
│   ├── performance/
│   └── users/
│
├── weblogic/
│   ├── install/
│   ├── domains/
│   ├── nodemanager/
│   ├── jdbc/
│   ├── wlst/
│   ├── deployments/
│   └── scripts/
│
├── scripts/
│   ├── shell/
│   ├── sql/
│   └── validation/
│
├── monitoring/
│
├── screenshots/
│
└── README.md
```

V1 vs V2
V1 — Platform Foundation

V1 established the Oracle enterprise platform:

```
AWS
 │
Terraform
 │
RHEL
 │
Oracle 19c
 │
WebLogic 14.1.1
 │
Java EE Application
 │
JDBC
```

V1 focused on:

Platform construction
Oracle administration
WebLogic administration
Application deployment
JDBC integration
RMAN
Terraform
AWS
V2 — Enterprise Modernization

V2 extends the platform into a database modernization scenario:
```
AWS
 │
Terraform
 │
Ansible
 │
Oracle 12.2.0.1
 │
WebLogic 14.1.1
 │
JDBC Integration
 │
Stabilization
 │
Oracle 12c → 19c
 │
19c → 19.32
 │
DST Upgrade
 │
WebLogic Re-Integration
 │
Application Validation
```
This makes V2 a continuation of the platform engineering work rather than simply another Oracle installation project.

Skills Demonstrated
Oracle Database
Oracle Database 12.2.0.1
Oracle Database 19c
Oracle Multitenant
CDB/PDB
Oracle Database Upgrades
Oracle Patching
RMAN
Data Pump
Oracle Net
Database Security
Time Zone Management
Performance Diagnostics
Production Troubleshooting
Oracle Middleware
Oracle WebLogic Server 14.1.1
WebLogic Domains
AdminServer
Managed Servers
Node Manager
WLST
JDBC
Connection Pools
Java EE
Application Deployment
Cloud & Platform Engineering
AWS
Terraform
Ansible
Infrastructure as Code
Configuration Management
EC2
VPC
EBS
IAM
Security Groups
GitHub Actions
Automation
Terraform
Ansible
WLST
Bash
SQL
GitHub Actions
Why This Project?

Enterprise organizations rarely operate databases and middleware in isolation.

Database upgrades can affect:

JDBC connectivity
Application compatibility
Connection pools
Authentication
Network configuration
PDB availability
Database objects
Time zone behavior
Application transactions
Middleware configuration

This project demonstrates the complete lifecycle of an enterprise Oracle platform:
```
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
```
The objective is to demonstrate the skills required to operate Oracle platforms as modern, automated enterprise infrastructure rather than treating the database as an isolated system.

Author

Tina Collins

Oracle Database Administrator • Oracle Platform Engineer • DevOps Engineer

Technologies

Oracle Database • Oracle WebLogic • AWS • Terraform • Ansible • RMAN • WLST • Java EE • Linux • GitHub Actions • Infrastructure as Code • Platform Engineering
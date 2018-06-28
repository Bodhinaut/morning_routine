### 3:00 AM - 7:00 AM

* AWS course working toward Developer Associate Cert.
* MySQL and databases
* Main focus on finishing Python Crash Course for solidification of concept and development of fun projects
* Space Invaders Clone
* Website with Django, uses SQLite
* Working with Pytest, like how modular it is comapred to unittest with python

---

AWS

Intro to IAM

---

IAM
Identiy Access Management 101

IAM allows you to manage users and their leve of access to the AWS Console. It is important to understand
IAM and how it works, both for the exam and for administrating a compnay's AWS account in real life. 

(Maybe under Security Identity and Compliance)

What does IAM give you?
Centralised control of your AWS account 
Shared Access to your AWS account
Granular Permissions - restrict system admin and database owners from accessing user data
Identity Federation (including active directory, Facebook, Linkedin etc) you can connect your IAM into 
active directory, with FB Linkdin etc.. you can federate with those providers, allows you to access your
AWS Cloud resources centrally, use IAM to enable users to sign in to their AWS account with their
existing corporate credentials. 

Multifactor Authentication, use two-factor authentication
Provide temoporar access for users/devices and services where necessary 
Ex, if making app or mobile phone app, that application can temp access your account and store stuff
in Dynamo, 
Allows you to set up your own password rotation policy 
Integrates with many different AWS services
Supports PCI DSS Compliance - Payment Card Industry Data Security Standard

--

CRITICAL TERMS 

Users - End Users (think people)
Groups - A collections of users under one set of permissions (groups users together and apply permission
to that specified group, ex, finance group, system adminstrator group)
Roles - You create roles and can then assing them to AWS resources, 
Example - Create Roles and assign to AWS resources, have EC2 instance (virtual machine) give the role 
in order to access S3, then that EC2 instance can write files directly to S3, and don't need to set up user 
and password for that EC2 instance, (next lab)
Policies - Documents that defines one or more permissions, attatch to users groups and roles, all connect
can all share policy document, 

LET'S GET STARTED

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


---


EC2
ECC
Amazon Elastic Computer Cloud - virtual machine in cloud, only take minutes to get going
resizable, quickly scale up and down, as your computing requirements change 
use to take 10 days to months to get servers, now takes minutes, amazon led this industry change 

can add more and more instances behind elactic load balancer, pay for capacity you use, use to have to buy 
servers and over provision, pay for what you need as you use it, amazing, pay by the hour or by the second, 

EC2 Options, 
On Demand: pay fixed rate by hour or second with no commitment; linux by second windows by hour, 

Reserved Instances: capacity reservation, 1 to three years, discount and you pay for year long terms 

Spot - enables to bid a price, for instance capacity, give lots of savings if you get the price, 
if your app has flexible start and end times this is a good option, but the share when it drops, for a sale when it 
goes over a certain amount 

Dedicated Hosts - Physical EC2 server dedicated for your use, dedicated hosts can help you reduce costs 

----- 

Use cases for pricing models 
On Demand : Low cost and flexibility of amaozon EC2 without up fron payment or long term commitemnt, 

Application being developer or tested on Amaazon EC2

Reserved Instances: an actual web service, up front payment to reduce computing costs, pay all up front for 
3 year contract get a great discount, 
Standard RIs can be up to 75% off on demand costs, 
Convertible RIs 54% off, can change your reservations, go from CPU intensive to memory intensive instance, 
not locked into an instance time, 

Scheudlued Reserved Instances : launched in a time window, recurring schedule, fraction of day or month, 
scale from on demand scale back 

Spot instances: flexible start and end times, applictions feasible at very low compute prices 
do huge amount of compute at 4 am on a sunday morining, its spoty, bang, 
users with an urgent need for large amounts of additional computing capacity 

Dedicated Hosts: regulatory requirments that may not supor t multi-tenant virtualization, could expose data 
to someone else, ??
great for licesning 
can be purchased on demand hourly 
puurcahses as reservation for 70% off

EC2 Instance Types -- dont need to memorize going into associate exams, useful at professional lvl, 
F1 - data analytics   --- LETTER FOR EXAM 
I3 - databases
G3 - video encoding 
H1 - file systems 
T2 - web serves small databases
D2 - data warehousing 
R4 - ram memory intensive 
M5- general purpose application servers 
C5 compute optimized - cpu intensive apps and databases 
P3 - general purpose GPUS machine learning, bit coing mining 
X1 - huge amoutns of RAM, apache spark, SAP HANA 

Imagine Edwards Notrton fighting Dr Mc Px, a scotting duck who likes to hand out pictures of scotland, 
F - FPGA
I - IOPS
G - Graphics
H - High Disk Throughput
T - cheap general purpose (think T2 Micro)
D - Density 
R - RAM
M - main choice for general purpose apps
C - Compute
P - Graphics (think Pics)
X - Extreme Memory

WHAT IS EBS?
EC2 virtual servier in cloud, EBS is ELASTIC BLOCK STORAGE it is a virtual disc, 
create storage volumes and attach them to EC2 instances, placed in AZ and replicated to protect from failure, 
spread across AZ, EBS will be fine if one disc dies, EBS is disc in cloud that coonects to EC2 instance, 
windows installed on C:drive, but can have other drives, 
EBS 
genreal purpose SSD (GP2)
general puspose balances both price and performance, Input Output Operations Per Second
EXAM - less the 10,00 IOPS, then you want GP2 EXAM 
Provisioned IOPS SSD - instensive applications RDMS, NOSQL , need extreme performace, if you need more than 
10,000 IOPS , big SQL, go PROVISIONS IOPS SSD, provision 20000 IOPS per volume, 

EBS volumes, throughtput optimized disc is additional volume not boot volume 
big data, data warehouse, long procssing 

Magnetic Standar
lowest cost mangetic bootable volume, legacy, lowest storage cost is important, 

EC2 EXAM TIPS
- ON DEMAND - fix rate by the hour or by the second with no commitment 
- RESERVED - capacity reservation, offer significant discount on hourly charge for an 
insatance   1 Year of 3 Year terms 
- SPOT - bid a price, for instance capacity, great savings if your app have flexible start and 
end times, pay only for what you bid on, prolly charged by the hour 
- DEDICATED HOSTS - physical EC2 server dedicated for your use, help you reduce cost
by allowing you to use existing server-bound software license 

is SPOT instance is terminated by EC2, you will not be charged for partial hour of usage, 
howver, if you temrinate the instance yourself you will be chaged for the time it ran 
POPULAR EXAM QUESTION ABOVE 
remember FIGHT DR MC PX

EXAM 

SSD - GENERAL PURPOSE SSD - balanc price and performance for wide workloads
Provisioned IOPS SSD - Highest performance SSD volume for mision-critical low-latency 
or high-throughput workloads

Magnetic
Throughoutput Optimized HDD - low cost HDD volume designed for frequenctly accessed 
thoughput intenisve workload 

A defined workload can be specified as a benchmark when evaluating a computer system 
in terms of performance (how easily the computer handles the workload), which in turn is 
generally divided into response time (the time between a user request and a response to 
the request from the system) and throughput (how much work is accomplished over a 
period of time).

COLD HDD - lowest cost HDD volume for less frequently accessed workload
Magnetic - Legacy, boot volume 

-------------------------
EC2 101 PART 2

went to download 

chmod 400 - lockdown - review this at some point, 

ssh ec2-user@ ip address - i MyNewKeyPair.pem

sudo su
super user for full admin access

yum update -y

install apache 

yum install httpd -y

service httpd start, or now systemctl start httpd.service

chkconfig httpd on -- if restart come appache automatically 

service httpd status

cd /var/www/html - nano and made html document


Doing a lab! 

created web server in the cloud, created web site, 
we can connect using public IP address, 

now register domain name and point back to this ec2 instance, 
first, must create an application load balancer for all of this to work, 

so lets see what is avaiable, then register domain name, then point our domain name to our load balancer, 
which will then point to our ec2 instance, 

---


Elastic load balancer 

balance ourl load across multiple different servers,
helps to balance load across servers, keeps app from crashing, 
AWS 3 different types pf load balancer 

Application Load Balancer - make clever decions, down to applicaton layer, load balancer there, 
can see to application layer and make clever routing decisions, 
Network Load Balancer- operates at layer 4, fast performace fast speed, aws most expencisve, 
would use in production
Classic Load Balancer - pretty much, dont reccomend anymore, for legacy, dev ass tests alot here

Application Load Balancer - best suited for load balancing of HTTp and HTTPS traffic, 
they operate at Layer 7 and are appplication-awaare, the are intelligent and you can create advanced
request routing, sending specified reuests to specific web servers, could send to different EC2 instance

Network Load Balancer are best suited for load balancing of TCP traffic, where extrmee performance 
is requried, operating at the ocnnection leve (layer 4) network load balancer are cpaable of handling
millions of request per second while mantianing ultra-low latencies 


Claassic load balancer - are the legacy Elastic Load Balancers, you can load balance HTTP/HTTPS
applications and use Layer 7 specific features, such as X-Forwarded and sticky sessions, 
you can also use strict Layer 4 load balancing for applictions that reply purely on the TCP protocol
layer seven or layer 4, or sticky sessions, 

Classic Load Balancer - 504 Error, app stops responding, ELB responsd 504
means the app is having issues, could be Web Server Layer or at Database Layer,
identify issue and scale it up or out where possible, 


X-Forwarded-For Header, 
ip address from user ---> DNS request, hits our load balancer, takes it and uses private ip address, 
sends to our EC2 instances, how get ip public address when EB sends you private address?
Get it from X-FOrwarded-For, 

ELB EXAM TIPS 

- 3 types of Load Balancers:
- Application Load Balancers
- Network Load Balancers
- Classic Load Balancers
- 504 Error means gateway has times out, app not responding, idle timeout period, 
- Trouble shoot app, web server or database server?
- If you need IPv4 address of end user, look for the X-Forwarded-For header. 

ROUTE53 - buy name and then connect, 
Amazons DNS service, 
- Allows you to map your domain names to 
EC2 Instances
Load Balancers
S3 Buckets 

---
OSI Model, logical model for how network systems should ocmmunicate 
OSI MODEL 7 LOGICAL LAYERS, THINK OF NETWORKING PROBLEM, THINK OF HOW TO FIX 

layers top to bootm, closest to end user, all the way to 

first layer application
this is the layer the user interacts with, google chrome for example, safari, firfox, 

presentation layer, this is the layer the operating system is on, 

seession layer, deals with communication creating a session between two computers, 

transport layer, assings how much information should be sent at a time, how much is commincated
and transefered 

netowkr layer, this is where routers operate on,  ip address is at the network level, 

data link layer, is the layer that switches 

layer one, the physcial layer, literally the phycsal stuff that connects computers together, 
programmers use OSI to know what they have to build for, 
break down compentns of network communicate and slot them into layers, 
physical is the wiring, 
layer 2 data link layer, where switching occures,

95% of all netwroing problems are layer 1 problems, 

https://www.youtube.com/watch?v=HEEnLZV2wGI

------------------------------


















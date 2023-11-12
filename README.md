# cloud_db_mgmt_pooling_migrations

## the objective of this assignment was gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

### Step 1: create instances in GCP and Azure then create a database in both and modify the IP addresses so that they can be accessible

### Step 2: enter a mySQL environment in cloud shell; use mysql -u steph -h (connection/IP address) -p then enter password

### Step 3: make a folder in google shell called "migrations-class" and enter "touch python_migrations.py" to make a file in the folder

## Running migrations 

### 1. alembic init migrations ` alembic init migrations `

### 2. edit alembic.ini to point to your database ` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

### 3. edit env.py to point to your models `from db_schema import Base` `target_metadata = Base.metadata `

### 4. create a migration ` alembic revision --autogenerate -m "create tables" `

### 5. run the migration ` alembic upgrade head `

### 6. check the database

### 7. roll back: To roll back a migration in Alembic, you can use the downgrade command. `alembic downgrade <target_revision>` 

 

## troubles while working on this:

### i ran into many issues while working on this assignment. I was not able to connect engine to azure or gcp instance. I tried changing my passoword, deleting and creating new azure migrations sql instance. I also turned off "ssl-mode"

### i had to change IDEs multiple times because cloud shell was being difficult. Decided to use vscode instead

### i waas not able to properly run alembic because there were so many issues that kept popping up and could not be resolved because every time i fix one issue another popped up.

### i was then not ble to fully deploy the app to but i did attach an image of the preview from when i ran the code. That was as far as I could get.

### i tried many IDE's as well and I don't know if it is beause I have a macbook air so the processing power isn't as good but at some point even the IDEs stated acting up. For example, in cloudshell, a code that i know should have worked all of a sudden cannot be found in the dirrectory and in vscode, even when i imported all the necessary packages, I got the same issues. These happened at different times over the period I was working on this homework. Moreover, i know it was not a problem on my end because if it didn't work at one point and i logged off and logged back on hours later, the code would start working again only to stop in a while. At some point cloud shell didn;t even let me cd into my repo.

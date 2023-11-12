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

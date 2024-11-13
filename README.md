# Strict-Multi-Tenant


# Multi-Tenant Django Project

This project uses Django with the `django-tenants` package to create a multi-tenant application structure. It includes API endpoints for `Todo` items, `Projects`, and `Tasks` with separate tenant schemas.

## Prerequisites

- Python 3.x
- PostgreSQL
- Pip (Python package installer)

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd multi_tenant_project
```

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate    # For MacOS/Linux
env\Scripts\activate       # For Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: PostgreSQL Setup

1. Ensure PostgreSQL is installed and running.
2. Log into PostgreSQL:

    ```bash
    psql -U postgres
    ```

3. Create a new database and user:

    ```sql
    CREATE DATABASE MultiTenant;
    CREATE USER tenant_user WITH PASSWORD 'password';
    ALTER ROLE tenant_user SET client_encoding TO 'utf8';
    ALTER ROLE tenant_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE tenant_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE MultiTenant TO tenant_user;
    ```

### Step 5: Update Database Configuration

In `settings.py`, confirm the `DATABASES` settings match your PostgreSQL setup:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'MultiTenant',
        'USER': 'tenant_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 6: Run Migrations for Tenants

```bash
python manage.py makemigrations
python manage.py migrate_schemas --shared
```

### Step 7: Create a Tenant

To add tenants, open the Django shell:

```bash
python manage.py shell
```

Then, run:

```python
from tenants.models import Client, Domain

# Create a new tenant (Client)
tenant = Client(
    name="Tenant A",
    paid_until="2024-12-31",
    on_trial=True,
    schema_name="tenant_a"
)
tenant.save()

# Assign a domain to the tenant
domain = Domain(
    domain="tenant1.localhost", 
    tenant=tenant, 
    is_primary=True
)
domain.save()
```

Repeat these steps if you need additional tenants.

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

Access each tenant with a unique domain (e.g., `tenant1.localhost` if mapped in `/etc/hosts` for local testing).

## API Documentation

### 1. **User Registration**

- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Payload**:

    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }
    ```

### 2. **Todo List**

- **Endpoint**: `/api/todos/`
- **Method**: `GET` or `POST`
- **Payload** for `POST`:

    ```json
    {
        "title": "Sample Todo",
        "description": "Description of the todo",
        "completed": false,
        "recurrence_interval": 5,
        "completion_time": "2024-11-15T15:05:00Z"
    }
    ```

### 3. **Projects**

- **Endpoint**: `/api/projects/`
- **Method**: `GET` or `POST`
- **Payload** for `POST`:

    ```json
    {
        "name": "Sample Project",
        "description": "Project description",
        "owner": 1
    }
    ```

### 4. **Tasks**

- **Endpoint**: `/api/tasks/`
- **Method**: `GET` or `POST`
- **Payload** for `POST`:

    ```json
    {
        "project": 1,
        "todo": 1,
        "assigned_user": 1,
        "due_date": "2024-11-20"
    }
    ```

---

## Running Tests

To test the API endpoints, you can use tools like Postman or CURL commands as per the examples above.

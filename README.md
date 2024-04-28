# Test assignment

## Description
This project is a Django REST Framework application that provides a REST API for managing wallets and transactions. It includes features such as pagination, sorting, filtering, and comprehensive API documentation using JSON:API standards.

## Features
- REST API to manage wallets and transactions.
- Pagination, sorting, and filtering for API responses.
- MySQL database integration.
- Docker integration for easy setup and deployment.

## Tech Stack
- Python 3.10
- Django and Django REST Framework
- MySQL
- Docker and Docker Compose

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have Docker and Docker Compose installed on your machine to run this project. Instructions for installing Docker can be found [here](https://docs.docker.com/get-docker/).

### Installing

1. Clone the repository:
   ```bash
   git clone git@github.com:Robsth/browallet.git
   cd browallet
   
2. Start the project:
   ```bash
   make up

3. Usage:  
- Stop the application:
   ```bash
   make down
- Run tests:
   ```bash
   make test
- Create a superuser:
   ```bash
   make createsuperuser

### API Endpoints

Once the application is running, you can access the following API endpoints:

- **Wallets Endpoint**:
  - Description: Retrieve or create wallet entries.
  - URL: [http://0.0.0.0:8000/api/wallets/](http://0.0.0.0:8000/api/wallets/)

- **Transactions Endpoint**:
  - Description: Retrieve or create transaction records.
  - URL: [http://0.0.0.0:8000/api/transactions/](http://0.0.0.0:8000/api/transactions/)

### Admin Interface

For administrative tasks, you can access the Django admin panel:

- **Admin Panel**:
  - URL: [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)

### How to Access the API

You can interact with the API using any HTTP client. Below are examples using `curl`:

```bash
# Retrieve all wallets
curl http://0.0.0.0:8000/api/wallets/?format=api

# Retrieve all transactions
curl http://0.0.0.0:8000/api/transactions/?format=api

# fastapi-backend-example

FastAPI backend example with REST API, Docker support, and best practices

## Overview

Modern REST API built with FastAPI demonstrating:

- Clean architecture with separated concerns
- Pydantic schemas for validation
- Docker containerization
- In-memory data store (demo)
- Type hints and modern Python
- RESTful endpoints

## Features

- ✅ FastAPI framework
- ✅ Pydantic models for validation
- ✅ CRUD operations (Create, Read, Delete)
- ✅ Dockerized application
- ✅ Health check endpoint
- ✅ Auto-generated OpenAPI docs

## Project Structure

```
fastapi-backend-example/
├── README.md
├── requirements.txt
├── Dockerfile
└── app/
    ├── main.py        # Application entry point
    ├── routes.py      # API endpoints
    ├── schemas.py     # Pydantic models
    └── models.py      # Domain models
```

## Quick Start

### Local Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API will be available at: http://localhost:8000

### Docker

```bash
docker build -t fastapi-backend .
docker run -p 8000:8000 fastapi-backend
```

## API Endpoints

### Health Check
- `GET /health` - Check API status

### Items
- `GET /items` - List all items
- `POST /items` - Create new item
- `GET /items/{id}` - Get item by ID
- `DELETE /items/{id}` - Delete item

## Documentation

Interactive API documentation available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Requirements

- Python 3.11+
- FastAPI 0.115.0
- Uvicorn 0.30.6

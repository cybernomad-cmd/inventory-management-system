# Inventory Management System

A simple Flask REST API for managing inventory items. The application supports CRUD operations, integrates with the OpenFoodFacts API to fetch product details, and includes a CLI for interacting with the inventory.

## Features

- View, add, update, and delete inventory items
- Fetch product details using OpenFoodFacts
- Command-line interface (CLI)
- API testing with pytest

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

Start the API:

```bash
python app.py
```

Run the CLI:

```bash
python cli.py
```

## API Endpoints

| Method | Endpoint |
|--------|----------|
| GET | `/` |
| GET | `/inventory` |
| GET | `/inventory/<id>` |
| POST | `/inventory` |
| PATCH | `/inventory/<id>` |
| DELETE | `/inventory/<id>` |
| GET | `/product/<barcode>` |

## Testing

```bash
python -m pytest -v
```

**Current Status:** 7 tests passed.

## Technologies

- Python
- Flask
- Requests
- Pytest
- OpenFoodFacts API
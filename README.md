# Material Registration Module - Odoo 14

A custom Odoo 14 module for material registration and management with REST API integration.

![Material Registration](./erd.png)

## Features

- Material registration with validation
- REST API endpoints for CRUD operations
- Price validation constraints
- Material type categorization

## Technical Specifications

- Odoo Version: 14.0
- Python: 3.6+
- Database: PostgreSQL

## Installation

1. Clone this repository:

```bash
git clone https://github.com/andrepurnomo/odoo-test.git material
```

2. Move to Odoo addons directory:

```bash
cp -r path/to/material /path/to/odoo/addons
```

3. Install through Odoo:

- Navigate to Apps
- Update Apps List
- Search for "Material Registration"
- Click Install

## API Endpoints

### Update Material

- URL: /api/material/<int:id>
- Method: PUT
- Authentication: Public
- Parameters:
  - material_code
  - material_name
  - material_type
  - material_buy_price
  - supplier_id

### Delete Material

- URL: /api/material/<int:id>
- Method: DELETE
- Authentication: Public

### Data Model

#### Material Registration

- material_code (Char): Unique identifier
- material_name (Char): Material name
- material_type (Selection): fabric/jeans/cotton
- material_buy_price (Float): Purchase price (min: 100)
- supplier_id (Many2one): Related supplier

#### Testing

```bash
docker-compose run web  --test-enable  --stop-after-init -d test -i material
```

### Author

Andre Agung Purnomo

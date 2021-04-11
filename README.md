# Heka API

Heka API is a web service used internally by Heka Distribution LLC to support critical business operations.

## Getting Started

Ensure you have at least Python 3.6+ installed:

> python3 --version

Clone this project to your computer:

> git clone https://github.com/orojas12/heka_api.git

Navigate to your project folder, create a virtualenv and activate it:

> cd /path/to/project/folder
> python3 -m venv venv
> source venv/bin/activate

Install dependencies:

> pip install -r requirements.txt

## Development/Testing

To run the Flask development server, set FLASK_APP and FLASK_ENV environment variables:

> export FLASK_APP=heka_api
> export FLASK_ENV=development

You can also set these in a .env file in the project folder to avoid doing it every time in a new terminal session:

> touch .env
> echo "FLASK_APP=heka_api" >> .env
> echo "FLASK_ENV=development" >> .env

Then run the development server.

> flask run

## Deployment

## API Reference

Get all orders placed:

> GET  /api/orders

---

Get data for a specific order:

> GET  /api/orders/<order_id>

| Parameter | Description                                                 |
|-----------|-------------------------------------------------------------|
| order_id  | UUID of order (e.g. "abb9dc99-0694-414e-b26f-920f20500fd9") |

---

Create a new order:

> POST  /api/orders

```json
{
    "customer_id": 3,
    "date_delivered": null,
    "date_placed": "2021-04-09T00:00:00",
    "date_shipped": null,
    "ship_address_same_as_customer": true,
    "ship_city": null,
    "ship_state": null,
    "ship_street": null,
    "ship_zip": null,
    "vaccines": [
        {
            "manufacturer_id": 1,
            "quantity": 5
        },
        {
            "manufacturer_id": 2,
            "quantity": 5
        },
        {
            "manufacturer_id": 3,
            "quantity": 5
        }
    ]
}
```
| Field                         | Required | Type          | Description                                                                                                                                                   |
|-------------------------------|----------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| customer_id                   | yes      | number        | The customer this order belongs to. Must be > 0.                                                                                                              |
| date_delivered                | no       | string        | The date and time that the order was delivered. Use ISO 8601 format.                                                                                          |
| date_placed                   | yes      | string        | The date and time that the order was placed. Use ISO 8601 format.                                                                                             |
| date_shipped                  | no       | string        | The date and time that the order was shipped. Use ISO 8601 format.                                                                                            |
| ship_address_same_as_customer | yes      | boolean       | Whether the order will be shipped to the saved customer address or a different one.                                                                           |
| ship_city                     | no       | string        | Shipping city. Use only if ship_address_same_as_customer is false.                                                                                            |
| ship_state                    | no       | string        | Shipping state. Use abbreviated state names (e.g. "TX"). Use only if ship_address_same_as_customer is false.                                                  |
| ship_street                   | no       | string        | Shipping house or building number + street name (e.g. "123 Fifth St). Use only if ship_address_same_as_customer is false.                                     |
| ship_zip                      | no       | string        | Shipping zip code. Use only if ship_address_same_as_customer is false.                                                                                        |
| vaccines                      | yes      | array<object> | Each vaccine object in the array should include "manufacturer_id": (1 = Pfizer, 2 = Moderna, 3 = J&J), and "quantity": (How many vaccine containers of each). |

---

Get all customers:

> GET  /api/customers

---

Create a new customer:

> POST  /api/customers

```json
{
    "first_name": "Oscar",
    "last_name": "Rojas",
    "company": "Vaccines Inc.",
    "email": "oscar@vaccines.com",
    "phone": "123-456-7890",
    "street": "100 Montana Ave",
    "city": "El Paso",
    "state": "TX",
    "zip": "79936",
    "dist_center": 1
}
```

| Field       | Required | Type   | Description                                                                                                |
|-------------|----------|--------|------------------------------------------------------------------------------------------------------------|
| first_name  | yes      | string | Customer's first name.                                                                                     |
| last_name   | yes      | string | Customer's last name.                                                                                      |
| company     | no       | string | The company or organization the customer represents.                                                       |
| email       | yes      | string | The customer's email address.                                                                              |
| phone       | yes      | string | The customer's phone number.                                                                               |
| street      | yes      | string | The customer's house/building number and street name (e.g. "123 Fifth St").                                |
| city        | yes      | string | The customer's city.                                                                                       |
| state       | yes      | string | The customer's state.                                                                                      |
| zip         | yes      | string | The customer's zip code.                                                                                   |
| dist_center | yes      | number | The ID of the Heka Distribution center serving the customer's city. (1 = El Paso, 2 = Dallas, 3 = Houston) |

---

Get data for a specific customer:

> GET  /api/customers/<customer_id>

| Parameter | Description                                                 |
|-----------|-------------------------------------------------------------|
| customer_id | Customer ID number |

---

Get all vaccine manufacturers:

> GET /api/manufacturers

---
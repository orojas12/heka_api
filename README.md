# Heka API

Heka API is a web service used internally by Heka Distribution LLC to support critical business operations.

## Getting Started

## API Reference

### Vaccine Orders

> blockquote

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
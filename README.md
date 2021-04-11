# Heka API

Heka API is a web service used internally by Heka Distribution LLC to support critical business operations.

## Getting Started

## API Reference

### Vaccine Orders

> GET /api/orders

Returns an array of all orders placed.

> GET /api/orders/<order_id>

> POST /api/orders

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


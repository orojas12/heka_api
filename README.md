# Heka API

Heka API is a web service used internally by Heka Distribution LLC to support its vaccine distribution system.

## Getting Started

Ensure you have at least Python 3.6+ installed:

```bash
python3 --version
```

Clone this project to your computer:

```bash
git clone https://github.com/orojas12/heka_api.git
```

Navigate to your cloned project folder, create a virtualenv and activate it:

```bash
cd /path/to/project/folder
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Development/Testing

To run the Flask development server, set FLASK_APP and FLASK_ENV environment variables:

```bash
export FLASK_APP=heka_api
export FLASK_ENV=development
```

You can also set these in a .env file in the project folder for persistence:

```bash
touch .env
echo "FLASK_APP=heka_api" >> .env
echo "FLASK_ENV=development" >> .env
```

Then run the development server.

```bash
flask run
```

When development/testing is done, you can deactivate your virtual environment:

```bash
deactivate
```

## Deployment

Before deploying, make sure you add your own production configuration to a .env file in the project folder.

Example:

```
SQLALCHEMY_DATABASE_URI={your_production_database_uri}
DEBUG=False
TESTING=False
```

Heka API uses Gunicorn as a WSGI http server for use with a reverse proxy such as Nginx. **Do not use the flask development server for production.**

### Deploying with Nginx

Create a systemd service unit file so the operating system can automatically start Gunicorn and serve the application on startup:

```bash
sudo nano /etc/systemd/system/heka_api.service
```
Insert this configuration, replacing anything inside {} with your own:

```
[Unit]
Description=Gunicorn instance to serve heka_api
After=network.target

[Service]
User={user}
Group={group}
WorkingDirectory=/home/{user}/heka_api
Environment="PATH=/home/{user}/heka_api/venv/bin"
ExecStart=/home/{user}/heka_api/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 "heka_api:create_app()"

[Install]
WantedBy=multi-user.target
```

You can now start the heka_api service and enable it so it starts on boot:

```bash
sudo systemctl start heka_api
sudo systemctl enable heka_api
```

Check the status to see if it is running correctly:

```bash
sudo systemctl status heka_api
```

Create the nginx server configuration for heka_api:

```bash
sudo nano /etc/nginx/sites-available/heka_api
```

Insert this configuration, replacing anyting inside {} with your own:

```
server {
    listen 80;
    server_name {your_domain} {www.your_domain} # if using static ip address, you can omit this line.

    location / {
        include proxy_params;
        proxy_pass http:127.0.0.1:8000;
    }
}
```

To enable the nginx server that was just created, link the file to the *sites-enabled* directory:

```bash
sudo ln -s /etc/nginx/sites-available/heka_api /etc/nginx/sites-enabled
```

Test the file for syntax errors:

```bash
sudo nginx -t
```

Restart nginx to read the new configuration:

```bash
sudo systemctl restart nginx
```

> Note: Ensure that *default* is removed from /etc/nginx/sites-enabled to prevent duplicate server errors.

Finally, adjust your firewall to allow incoming requests on port 80:

```bash
sudo ufw allow 'Nginx Full'
```

You should now be able to make http requests to your server's ip address or domain name:

```bash
curl -X GET http://example.com/api/orders
```

If you encounter any errors try checking the following logs:

```bash
sudo less /var/log/nginx/error.log
sudo less /var/los/nginx/access.log
sudo journalctl -u nginx
sudo journalctl -u heka_api
```

## API Reference

Get all orders placed:

```bash
curl -X GET https://localhost:5000/api/orders
```

Get data for a specific order:

> GET  /api/orders/<order_id>

| Parameter | Description                                                 |
|-----------|-------------------------------------------------------------|
| order_id  | UUID of order (e.g. "abb9dc99-0694-414e-b26f-920f20500fd9") |

Create a new order:

```bash
curl -X POST http://localhost:5000/api/orders
```
JSON body example:

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

```bash
curl -X GET https://localhost:5000/api/customers
```

Create a new customer:

```bash
curl -X POST http://localhost:5000/api/customers
```

JSON body example:

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

Get data for a specific customer:

```bash
curl -X GET https://localhost:5000/api/customers/<customer_id>
```

| Parameter | Description                                                 |
|-----------|-------------------------------------------------------------|
| customer_id | Customer ID number |

---

Get all vaccine manufacturers:

```bash
curl -X GET https://localhost:5000/api/manufacturers
```

## License

This project is licensed under the [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

## Contributors

Oscar Rojas - [orojas12](https://github.com/orojas12)
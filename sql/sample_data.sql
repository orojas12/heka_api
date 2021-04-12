INSERT INTO manufacturers (name, country, state, city, street, zip) VALUES 
  ('Pfizer Inc.', 'USA', 'NY', 'New York', '235 East 42nd St', '10017'),
  ('Moderna', 'USA', 'MA', 'Cambridge', '200 Technology Square', '02139'),
  ('Johnson & Johnson', 'USA', 'NJ', 'New Brunswick', '1 Johnson & Johnson Plaza', '08933')
;

INSERT INTO distribution_centers (phone, state, city, street, zip) VALUES
  ('915-123-4567', 'TX', 'El Paso', '9201 Empire Dr', '79901'),
  ('469-123-4567', 'TX', 'Dallas', '5915 Peeler St', '72096'),
  ('281-123-4567', 'TX', 'Houston', '123 Some Street', '77001')
;

INSERT INTO customers (first_name, last_name, company, email, phone, state, city, street, zip, dist_center) 
  VALUES
    ('John', 'Smith', 'El Paso Clinic', 'contact@elpclinic.org', '915-123-1234', 'TX', 'El Paso', 
      '123 Some Street', '79901', 1),
    ('Ann', 'Johnson', 'Dallas Medical Center', 'contact@dallasmc.org', '469-123-1234', 'TX', 'Dallas',
      '456 Some Street', '72096', 2),
    ('Bob', 'White', 'Houston Hospital', 'contact@houstonhospital.org', '281-123-1234', 'TX', 'Houston',
      '789 Some Street', '77001', 3)
;

INSERT INTO orders (id, customer_id, ship_address_same_as_customer, date_placed, date_shipped,
  date_delivered)
  VALUES
    ('abb9dc99-0694-414e-b26f-920f20500fd9', 1, 1, CURDATE(), NULL, NULL),
    ('029c0c54-c2ba-4599-befe-2142e6cb6003', 2, 1, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 1 DAY), NULL),
    ('a3c2040b-7e0f-43a9-8dd3-012428e60821', 1, 1, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 1 DAY), DATE_ADD(CURDATE(), INTERVAL 2 DAY)),
    ('17b70bf4-3c7f-407b-83f6-6f9aeac362f8', 3, 1, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 1 DAY), DATE_ADD(CURDATE(), INTERVAL 2 DAY))
;

INSERT INTO orders (id, customer_id, ship_address_same_as_customer, ship_street, ship_city, ship_state,
  ship_zip, date_placed, date_shipped, date_delivered)
  VALUES
    ('e6ef78e9-5186-4366-98a0-51257ae48a5b', 2, 0, '100 Fake St', 'Dallas', 'TX', '79936', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 1 DAY), NULL),
    ('224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 3, 0, '200 Fake St', 'Houston', 'TX', '79928', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 1 DAY), 
      DATE_ADD(CURDATE(), INTERVAL 2 DAY))
;

INSERT INTO vaccine_containers VALUES
  ('5662ed77-8f0e-4f42-89cb-9ad9a904040a', 'abb9dc99-0694-414e-b26f-920f20500fd9', 1, 1),
  ('1bf32878-8ea5-4826-9714-60b52e2bde53', 'abb9dc99-0694-414e-b26f-920f20500fd9', 1, 1),
  ('6eae56a9-6be1-47ae-a5ca-1c333957fc5b', '029c0c54-c2ba-4599-befe-2142e6cb6003', 2, 1),
  ('2d609ea3-2219-434c-a113-b90548b31620', '029c0c54-c2ba-4599-befe-2142e6cb6003', 2, 1),
  ('49fdf4b5-6c10-4dc7-aa06-dcfe16c35464', 'a3c2040b-7e0f-43a9-8dd3-012428e60821', 1, 1),
  ('f9fd59f7-4b51-4765-9761-21101a5b0938', 'a3c2040b-7e0f-43a9-8dd3-012428e60821', 2, 2),
  ('98b50347-5ac4-4fcc-9600-7412a884b682', 'a3c2040b-7e0f-43a9-8dd3-012428e60821', 1, 2),
  ('8e37e731-da5d-4995-82fb-5ba36c0540e7', '17b70bf4-3c7f-407b-83f6-6f9aeac362f8', 3, 2),
  ('b50a4863-7b67-4a6d-beb6-7e1227cb39e7', 'e6ef78e9-5186-4366-98a0-51257ae48a5b', 1, 2),
  ('fa11c09d-928b-43dc-8475-9cc7e8236caa', 'e6ef78e9-5186-4366-98a0-51257ae48a5b', 1, 3),
  ('40c25ff1-7ebb-4a46-9f97-87cf03afdcfa', '224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 2, 3),
  ('b5a2caa1-21af-4a9d-8be0-e650fcb22665', '224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 2, 3),
  ('427bec84-34c3-4796-ab7e-383bfc929a73', '224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 2, 3)
;

INSERT INTO ancillary_kits VALUES
  ('2618e978-1bc5-4b11-939b-977abed7655e', 'abb9dc99-0694-414e-b26f-920f20500fd9', 1, 1),
  ('b9fd51d0-047d-4681-86a5-4c7312ba6c7a', 'abb9dc99-0694-414e-b26f-920f20500fd9', 1, 1),
  ('3acf14cb-1f85-405b-8d91-61becd05b23f', '029c0c54-c2ba-4599-befe-2142e6cb6003', 2, 1),
  ('564d3680-2f3d-4ffc-83e2-457f8205e119', '029c0c54-c2ba-4599-befe-2142e6cb6003', 2, 1),
  ('28c101fa-13a6-4865-87e6-8ffc3c380ca9', 'a3c2040b-7e0f-43a9-8dd3-012428e60821', 1, 2),
  ('8ac77e6e-e6cb-4f38-b805-909c9a8b9ec7', 'a3c2040b-7e0f-43a9-8dd3-012428e60821', 2, 2),
  ('2391e123-c987-4749-878c-d08fda5a6a9a', 'a3c2040b-7e0f-43a9-8dd3-012428e60821', 1, 2),
  ('b119b5c0-bdd2-4640-b028-b25dfe8dcf03', '17b70bf4-3c7f-407b-83f6-6f9aeac362f8', 3, 2),
  ('723692aa-8ac2-44d4-abba-c771fdf1129e', 'e6ef78e9-5186-4366-98a0-51257ae48a5b', 1, 3),
  ('ccd902f7-687f-44d1-9557-60d77e7604b8', 'e6ef78e9-5186-4366-98a0-51257ae48a5b', 1, 3),
  ('5bf4bab7-85df-43e7-ad71-27655098e77a', '224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 2, 3),
  ('24383617-22c7-465d-8a9f-538819e568de', '224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 2, 3),
  ('e5388635-7156-47e4-a4f3-d3fadb1abea7', '224abc5b-ca63-4c5c-a23b-fc80d8364c7c', 2, 3)
;

INSERT INTO departments (name, phone, manager_id, dist_center) VALUES
  ('Human Resources', '915-456-1234', NULL, 1),
  ('Accounting & Finance', '915-456-1233', NULL, 1),
  ('Information Technology', '915-456-1235', NULL, 1),
  ('Customer Service', '915-456-1236', NULL, 1),
  ('Marketing', '915-456-1232', NULL, 1),
  ('Operations', '915-456-1237', NULL, 1),
  ('Human Resources', '469-123-1234', NULL, 2),
  ('Accounting & Finance', '469-123-1233', NULL, 2),
  ('Information Technology', '469-123-1235', NULL, 2),
  ('Customer Service', '469-123-1236', NULL, 2),
  ('Marketing', '469-123-1232', NULL, 2),
  ('Operations', '469-123-1237', NULL, 2),
  ('Human Resources', '281-789-1234', NULL, 3),
  ('Accounting & Finance', '281-789-1233', NULL, 3),
  ('Information Technology', '281-789-1235', NULL, 3),
  ('Customer Service', '281-789-1236', NULL, 3),
  ('Marketing', '281-789-1232', NULL, 3),
  ('Operations', '281-789-1237', NULL, 3)
;

INSERT INTO it_assets VALUES
  ('23439993-ca74-4341-9580-64ee7df4efe2', 'Dell', 'OptiPlex 3080', 'Desktop computer', 1),
  ('fff1ba38-647e-457d-9147-6cc1bc119825', 'Dell', 'OptiPlex 3080', 'Desktop computer', 2),
  ('1638a4dc-6a2b-4c23-b7fd-1744f965b424', 'Dell', 'OptiPlex 3080', 'Desktop computer', 3),
  ('066b913b-1a61-4cd9-a092-31432f4d56da', 'Netgear', 'GS324TP', 'Switch', 1),
  ('0c914ab5-373f-4a67-8ecd-879e02b4ed95', 'Netgear', 'GS324TP', 'Switch', 2),
  ('42b3ae84-67ec-4b72-9d83-46a09828cf58', 'Netgear', 'GS324TP', 'Switch', 3),
  ('0ee85dc4-4486-4a2b-9e92-6b64acaa3d52', 'Netgear', 'Nighthawk R6700', 'Wireless router', 1),
  ('9a3abd57-32c0-4d37-a653-4e88230a2e0c', 'Netgear', 'Nighthawk R6700', 'Wireless router', 2),
  ('2bffe34d-e911-45ba-9f87-1eb028ad9e94', 'Netgear', 'Nighthawk R6700', 'Wireless router', 3),
  ('f1a57047-a98a-4b04-bf36-122681cbb418', 'HP', 'Inspiron 15 3000', 'Laptop', 1),
  ('21199508-415c-4096-8041-363cdd188586', 'HP', 'Inspiron 15 3000', 'Laptop', 2),
  ('7aecf491-d6f7-43b8-8da8-c2f20a375f20', 'HP', 'Inspiron 15 3000', 'Laptop', 3),
  ('321f829f-995c-4eef-9753-571e67428900', 'HP', 'ProLiant DL360p', 'Server', 1),
  ('810f9012-c226-449b-811c-a7f6c3d15c7b', 'HP', 'ProLiant DL360p', 'Server', 1)
;

INSERT INTO employees (first_name, last_name, employment_date, job_title, department_id,
  street, city, state, zip)
  VALUES
    ('Joe', 'Willock', '2020-01-05', 'IT Manager', 3, '123 Made Up St', 'El Paso', 'TX', '79901'),
    ('Amy', 'Scott', '2020-02-12', 'Network Administrator', 3, '456 Some St', 'El Paso', 'TX', '79905'),
    ('Bob', 'Smith', '2020-02-03', 'Database Administrator', 3, '789 Fake Ave', 'El Paso', 'TX', '79901'),
    ('Tony', 'Stewart', '2020-01-05', 'IT Technician', 3, '123 El Paso St', 'El Paso', 'TX', '79901'),
    ('Susan', 'White', '2020-01-05', 'IT Technician', 3, '123 South St', 'El Paso', 'TX', '79901')
;
DROP TABLE IF EXISTS vaccine_containers;
DROP TABLE IF EXISTS ancillary_kits;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS it_assets;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS distribution_centers;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE IF NOT EXISTS manufacturers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  street VARCHAR(50),
  city VARCHAR(50),
  state VARCHAR(50),
  province VARCHAR(50),
  zip VARCHAR(15),
  country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS distribution_centers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  phone VARCHAR(50),
  street VARCHAR(50),
  city VARCHAR(50),
  state VARCHAR(50),
  zip VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  company VARCHAR(50),
  email VARCHAR(50) NOT NULL,
  phone VARCHAR(50) NOT NULL,
  street VARCHAR(50) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zip VARCHAR(15) NOT NULL,
  dist_center INT NOT NULL,
  FOREIGN KEY (dist_center) 
    REFERENCES distribution_centers(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS orders (
  id VARCHAR(100) PRIMARY KEY,
  customer_id INT NOT NULL,
  ship_address_same_as_customer BOOLEAN NOT NULL,
  ship_street VARCHAR(50),
  ship_city VARCHAR(50),
  ship_state VARCHAR(50),
  ship_zip VARCHAR(15),
  date_placed DATETIME,
  date_shipped DATETIME,
  date_delivered DATETIME,
  FOREIGN KEY (customer_id)
    REFERENCES customers(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS vaccine_containers (
  id VARCHAR(100) PRIMARY KEY,
  order_id VARCHAR(100),
  manufacturer_id INT NOT NULL,
  dist_center INT NOT NULL,
  FOREIGN KEY (order_id)
    REFERENCES orders(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (manufacturer_id)
    REFERENCES manufacturers(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (dist_center)
    REFERENCES distribution_centers(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS ancillary_kits (
  id VARCHAR(100) PRIMARY KEY,
  order_id VARCHAR(100),
  manufacturer_id INT NOT NULL,
  dist_center INT NOT NULL,
  FOREIGN KEY (order_id)
    REFERENCES orders(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (manufacturer_id)
    REFERENCES manufacturers(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS departments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  phone VARCHAR(50),
  manager_id INT,
  dist_center INT NOT NULL,
  FOREIGN KEY (dist_center)
    REFERENCES distribution_centers(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS it_assets (
  serial_no VARCHAR(100),
  brand VARCHAR(50),
  model_name VARCHAR(50),
  description VARCHAR(100),
  department_id INT NOT NULL,
  FOREIGN KEY (department_id)
    REFERENCES departments(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  employment_date DATE,
  job_title VARCHAR(50),
  department_id INT,
  street VARCHAR(50),
  city VARCHAR(50),
  state VARCHAR(50),
  zip VARCHAR(15),
  FOREIGN KEY (department_id)
    REFERENCES departments(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);
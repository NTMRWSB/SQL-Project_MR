CREATE USER 'admin' @'localhost' IDENTIFIED BY '123456';

ALTER USER 'admin' @'localhost' IDENTIFIED WITH mysql_native_password BY '123456';

CREATE DATABASE IF NOT EXISTS supermr_db;

GRANT ALL PRIVILEGES ON supermr_db.* TO 'admin' @'localhost';
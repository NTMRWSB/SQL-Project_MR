CREATE USER 'admin' @'localhost' IDENTIFIED BY '123456';

--docker
--CREATE USER 'admin' @'172.17.0.1' IDENTIFIED BY '123456';

ALTER USER 'admin' @'localhost' IDENTIFIED WITH mysql_native_password BY '123456';

--docker
--ALTER USER 'admin' @'172.17.0.1' IDENTIFIED WITH mysql_native_password BY '123456';

CREATE DATABASE IF NOT EXISTS supermr_db;

GRANT ALL PRIVILEGES ON supermr_db.* TO 'admin' @'localhost';

--docker
--GRANT ALL PRIVILEGES ON supermr_db.* TO 'admin' @'172.17.0.1';
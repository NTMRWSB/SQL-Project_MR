--用户表
CREATE TABLE IF NOT EXISTS tb_user
(
--用户ID 主键 非空 自增
userid INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
--用户名 唯一
username VARCHAR(255) UNIQUE NOT NULL,
--密码 PASSWORD加密
userpassword VARCHAR(255) NOT NULL,
--账号添加/修改时间
add_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--供应商/公司表
CREATE TABLE IF NOT EXISTS tb_company
(
--公司ID
companyid INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
--公司名
company_name VARCHAR(255) UNIQUE NOT NULL,
--公司地址
company_address VARCHAR(255) NOT NULL,
--公司电话
company_tel VARCHAR(255) NOT NULL,
--公司联系人
company_contact_people VARCHAR(255) NOT NULL,
--公司邮箱
company_email VARCHAR(255) NOT NULL,
--操作用户
username VARCHAR(255) NOT NULL,
--添加/修改时间
add_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--商品表
CREATE TABLE IF NOT EXISTS tb_goods
(
--商品ID
goodsid INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
--商品名称
goods_name VARCHAR(255) UNIQUE NOT NULL,
--商品产地
place_of_production VARCHAR(255) NOT NULL,
--价格
price FLOAT NOT NULL,
--公司ID
companyid INT UNSIGNED,
CONSTRAINT companyid_for_tb_goods
FOREIGN KEY(companyid) REFERENCES tb_company(companyid),
--操作用户
username VARCHAR(255) NOT NULL,
--添加/修改时间
add_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--库存表
CREATE TABLE IF NOT EXISTS tb_stock
(
--库存ID 主键 非空 自增
stockid INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
--商品ID 外键
goodsid INT UNSIGNED,
CONSTRAINT goodsid_for_tb_stock
FOREIGN KEY(goodsid) REFERENCES tb_goods(goodsid),
--数量
num INT NOT NULL,
--操作用户
username VARCHAR(255) NOT NULL,
--库存变更时间
add_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--订单表
CREATE TABLE IF NOT EXISTS tb_order
(
--订单ID 主键 非空 自增
orderid INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
--商品ID 外键
goodsid INT UNSIGNED,
CONSTRAINT goodsid_for_tb_order
FOREIGN KEY(goodsid) REFERENCES tb_goods(goodsid),
--交易数量
num INT NOT NULL,
--交易方式
payment_type VARCHAR(255) NOT NULL,
--操作用户
username VARCHAR(255) NOT NULL,
--交易时间
add_time DATETIME NULL DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
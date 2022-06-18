--增加触发器
CREATE TRIGGER add_num
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE goods SET num=num-new.num WHERE id = new.goodsid;
END$

--删除触发器
CREATE TRIGGER del_num
AFTER delete ON orders
FOR EACH ROW
BEGIN
UPDATE goods SET num=num+old.num WHERE id = old.goodsid;
END$

--修改触发器
CREATE TRIGGER mod_num
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
UPDATE goods SET num=num+old.num-new.num WHERE id = old.goodsid;
END$
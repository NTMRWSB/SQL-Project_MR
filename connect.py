import pymysql

class ConnectMysql(object):

    def __init__(self,host,port,db,user,password):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.password=password

    def __enter__(self):
        # 在进入的时候自动获取连接和cursor
        conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.password)
        cursor = conn.cursor()#pymysql.cursors.DictCursor)
        # conn.autocommit = False
        self.db = conn
        self.cursor = cursor
        return self

    def __exit__(self, *exc_info):
        self.cursor.close()
        self.db.close()

def mult_query(s,
            host='localhost',
            port=3306,
            db='supermr_db',
            user='admin',
            password='123456'):
    s=''.join(s).split(';')[:-1]
    with ConnectMysql(host,port,db,user,password) as m:
        for a in s:
            m.cursor.execute(a+';')
            m.db.commit()
        data = m.cursor.fetchall()
    return data

def one_query(s,
            host='localhost',
            port=3306,
            db='supermr_db',
            user='admin',
            password='123456'):
    with ConnectMysql(host,port,db,user,password) as m:
        m.cursor.execute(s)
        m.db.commit()
        data = m.cursor.fetchall()
    return data
import wx
from frames import *
from connect import *
from login import login,reg
from show import show


#init
s=[]
with open('init.sql','r')as f:
    s=f.readlines()
mult_query(s)

uid,uname,level=login()
level=int(level)

app = wx.App()
wx.MessageBox('欢迎，%s！您有%d级权限。'%(uname,level),'欢迎',wx.ICON_INFORMATION)
class dashboard(MainFrame):
    def act(self, event):
        if level>1:
            self.m_button1.Hide()
            self.m_button5.Hide()
        if level>2:
            self.m_button2.Hide()
            self.m_button3.Hide()
        s='SELECT COUNT(*) FROM user'
        data=str(one_query(s)[0][0])
        self.m_staticText1.Label='共有 '+data+' 个员工'
        s='SELECT COUNT(*) FROM company'
        data=str(one_query(s)[0][0])
        self.m_staticText2.Label='共有 '+data+' 个供应商'
        s='SELECT COUNT(*) FROM goods'
        data=str(one_query(s)[0][0])
        self.m_staticText3.Label='共有 '+data+' 种商品'
        s='SELECT COUNT(*) FROM orders'
        data=str(one_query(s)[0][0])
        self.m_staticText4.Label='共有 '+data+' 个订单'
    def user_click(self, event):
        col_names=('id','name','password','level','add_time')
        table_name='user'
        show(col_names,table_name)
    def company_click(self, event):
        col_names=('id','name','address','telphone','email','contact_person','userid','add_time')
        table_name='company'
        show(col_names,table_name)
    def goods_click(self, event):
        col_names=('id','name','place_of_production','price','companyid','userid','add_time')
        table_name='goods'
        show(col_names,table_name)
    def orders_click(self, event):
        col_names=('id','goodsid','num','payment_type','userid','add_time')
        table_name='orders'
        show(col_names,table_name)
    def reg_click(self, event):
        app2 = wx.App()
        frame = reg(None)
        frame.textCtrl3.Value = '1'
        frame.Show()
        app2.MainLoop()
dash=dashboard(None)
dash.Show()
app.MainLoop()
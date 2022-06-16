import wx
from frames import *
from connect import *
from hashlib import sha256

class log(LoginFrame):
    def clicked(self, event):
        s='SELECT id,password FROM user;'
        users=dict(one_query(s))
        global uid,uname,level
        a=int(self.textCtrl1.Value)
        b=self.textCtrl2.Value
        b=sha256(b.encode('utf-8')).hexdigest()
        if a not in users:
            wx.MessageBox('无此账号','错误',wx.ICON_ERROR)
        elif users[a]!=b:
            wx.MessageBox('密码错误','错误',wx.ICON_ERROR)
        else:
            s='SELECT name,level FROM user WHERE id=%s;'%a
            uid=a
            uname,level=one_query(s)[0]
            self.Close()

class reg(RegisterFrame):
    def clicked(self, event):
        global uid,uname,level
        a=self.textCtrl1.Value
        b=self.textCtrl2.Value
        c=self.textCtrl3.Value
        d=self.textCtrl4.Value
        if a=='' or b=='' or c=='' or d=='':
            wx.MessageBox('不能留空','输入出错',wx.ICON_ERROR)
        elif not a.isdigit() and not c.isdigit():
            wx.MessageBox('账号和权限必须是数字','输入出错',wx.ICON_ERROR)
        else:
            uid,uname,level=a,d,c
            b=sha256(b.encode('utf-8')).hexdigest()
            s='INSERT INTO user (id,password,name,level) VALUES (%s,"%s","%s",%s);'%(a,b,d,c)
            one_query(s)
            self.Close()

def login()->tuple[int,str,int]:
    app = wx.App()

    global uid,uname,level
    s='SELECT id,password FROM user;'
    users=dict(one_query(s))
    if users:
        #login
        frame=log(None)
        frame.Show()
    else:
        frame=reg(None)
        frame.textCtrl3.Value='1'
        frame.Show()

    app.MainLoop()

    return uid,uname,level
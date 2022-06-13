import wx
from frames import *
from connect import *
from hashlib import sha256
from tkinter.messagebox import showinfo

#start app
app = wx.App()

#init
s=[]
with open('init.sql','r')as f:
    s=f.readlines()
mult_query(s)

global uid,uname,level
s='SELECT id,password FROM user;'
users=dict(one_query(s))
if users:
    #login
    class login(LoginFrame):
        def clicked(self, event):
            global uid,uname,level
            a=self.textCtrl1.Value
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
    frame=login(None)
    frame.Show()
else:
    class reg_boss(RegisterFrame):
        def clicked(self, event):
            global uid,uname,level
            a=self.textCtrl1.Value
            b=self.textCtrl2.Value
            c=self.textCtrl4.Value
            if a=='' or b=='':
                wx.MessageBox('账号、密码和用户名不能留空','输入出错',wx.ICON_ERROR)
            elif not a.isdigit():
                wx.MessageBox('账号必须是数字','输入出错',wx.ICON_ERROR)
            else:
                uid,uname,level=a,c,1
                b=sha256(b.encode('utf-8')).hexdigest()
                s='INSERT INTO user (id,password,name,level) VALUES (%s,"%s","%s",%d);'%(a,b,c,1)
                one_query(s)
                self.Close()
    frame=reg_boss(None)
    frame.textCtrl3.Value='1'
    frame.Show()

# wx.MessageBox('欢迎，%s！您有%d级权限。'%(uname,level),'欢迎',wx.ICON_INFORMATION)

#end app
app.MainLoop()
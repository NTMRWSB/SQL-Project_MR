import wx
import wx.grid
from connect import one_query
from frames import *
from helper_func import *

class Grid(GridFrame):

    col_names=''
    table_name=''

    def delete(self, event):
        wx.Yield()
        i=get_input()
        s='DELETE FROM '+self.table_name+' WHERE id = '+i
        try:
            one_query(s)
            wx.MessageBox('删除完成','成功',wx.ICON_INFORMATION)
            s = 'select '+','.join(self.col_names)+' from '+self.table_name+';'
            data=one_query(s)
            table = Table(head=self.col_names, body=data, changeable=True)
            self.m_grid.SetTable(table=table, takeOwnership=True)
            self.m_grid.AutoSize()
            self.Layout()
        except:
            wx.MessageBox('数据有误，可能是有依赖项导致的，请重试','失败',wx.ICON_WARNING)

    def add(self, event):
        wx.Yield()
        x=get_item(self.col_names).split(',')
        col=[]
        inp=[]
        for i in range(len(self.col_names)):
            if x[i].strip()!='':
                col.append(self.col_names[i])
                inp.append('"'+x[i]+'"')
        s='INSERT INTO '+self.table_name+' ('+','.join(col)+') VALUES ('+','.join(inp)+');'
        try:
            one_query(s)
            wx.MessageBox('添加完成','成功',wx.ICON_INFORMATION)
            s = 'select '+','.join(self.col_names)+' from '+self.table_name+';'
            data=one_query(s)
            table = Table(head=self.col_names, body=data, changeable=True)
            self.m_grid.SetTable(table=table, takeOwnership=True)
            self.m_grid.AutoSize()
            self.Layout()
        except:
            wx.MessageBox('数据有误，请重试','失败',wx.ICON_WARNING)

    def mod(self, event):
        wx.Yield()
        i=get_input().strip()
        s='SELECT * FROM '+table_name+' WHERE id= '+i+';'
        # try:
        col=self.col_names[:-1]
        data=one_query(s)[0][:-1]
        data=mod_item(col,data)
        # print(data)
        data=['"'+x.strip()+'"'for x in data.split(',')]
        t=','.join([x+'='+y for x,y in zip(col,data)])
        s='UPDATE '+self.table_name+' SET '+t+',add_time=CURRENT_TIMESTAMP WHERE id = '+i+';'
        print(s)
        one_query(s)

        wx.MessageBox('修改完成','成功',wx.ICON_INFORMATION)
        s = 'select '+','.join(self.col_names)+' from '+self.table_name+';'
        data=one_query(s)
        table = Table(head=self.col_names, body=data, changeable=True)
        self.m_grid.SetTable(table=table, takeOwnership=True)
        self.m_grid.AutoSize()
        self.Layout()
        # except:
        #     wx.MessageBox('数据有误，请重试','失败',wx.ICON_WARNING)

    # def mod(self, event):
    #     wx.Yield()
    #     i=get_input()
    #     s='DELETE FROM '+self.table_name+' WHERE id = '+i
    #     try:
    #         one_query(s)
    #         wx.Yield()
    #         x=get_item(self.col_names).split(',')
    #         col=[]
    #         inp=[]
    #         for i in range(len(self.col_names)):
    #             if x[i].strip()!='':
    #                 col.append(self.col_names[i])
    #                 inp.append('"'+x[i]+'"')
    #         s='INSERT INTO '+self.table_name+' ('+','.join(col)+') VALUES ('+','.join(inp)+');'
    #         one_query(s)
    #         wx.MessageBox('修改完成','成功',wx.ICON_INFORMATION)
    #         s = 'select '+','.join(self.col_names)+' from '+self.table_name+';'
    #         data=one_query(s)
    #         table = Table(head=self.col_names, body=data, changeable=True)
    #         self.m_grid.SetTable(table=table, takeOwnership=True)
    #         self.m_grid.AutoSize()
    #         self.Layout()
    #     except:
    #         wx.MessageBox('无法修改，可能是有依赖项导致的，请重试','失败',wx.ICON_WARNING)
    #         return

    # def CellChange(self, event):
    #     x,y = event.GetRow(),event.GetCol()
    #     val = self.m_grid.GetCellValue(x, y)
    #     if val == '':
    #         val = 'null'
    #     ColLabel = self.col_names[y]
    #     # self.data[x,0]
    #     ID_new = self.m_grid.GetCellValue(x,0)
    #     s = 'UPDATE ' + self.table_name + ' SET ' + ColLabel + ' = "' + val + '" WHERE id = "' + ID_new + '";'
    #     print(s)
    #     try:
    #         one_query(s)
    #         wx.MessageBox('修改完成','成功',wx.ICON_INFORMATION)
    #         s = 'select '+','.join(self.col_names)+' from '+self.table_name+';'
    #         data=one_query(s)
    #         table = Table(head=self.col_names, body=data, changeable=True)
    #         self.m_grid.SetTable(table=table, takeOwnership=True)
    #         self.m_grid.AutoSize()
    #         self.Layout()
    #     except:
    #         wx.MessageBox('数据有误，请重试','失败',wx.ICON_WARNING)

def show(col_names:tuple[str],table_name:str):
    apps=wx.App()

    frame=Grid(None)

    frame.col_names=col_names
    frame.table_name=table_name
    s = 'SELECT '+','.join(col_names)+' FROM '+table_name+';'
    data=one_query(s)

    table = Table(head=col_names, body=data, changeable=True)
    frame.m_grid.SetTable(table=table, takeOwnership=True)
    frame.m_grid.AutoSize()

    frame.Show()

    apps.MainLoop()

if __name__ == '__main__':
    col_names=('id','name','place_of_production','price','companyid','userid','add_time')
    table_name='goods'
    show(col_names,table_name)
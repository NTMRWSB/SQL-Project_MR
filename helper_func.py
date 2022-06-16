import wx
import wx.grid
from connect import *
from frames import *
from os import popen

class Table(wx.grid.GridTableBase):
    def __init__(self, head, body, changeable):
        super(Table, self).__init__()
        self.head = head
        self.body = body
        self.changeable = changeable
    def GetNumberRows(self):
        return len(self.body)
    def GetNumberCols(self):
        return len(self.head)
    def GetValue(self, row, col):
        return self.body[row][col]
    def GetColLabelValue(self, col):
        return self.head[col]
    def SetValue(self, row, col, value):
        if self.changeable:
            self.body[row][col] = value
        else:
            return

def get_input()->str:
    return popen('python read.py').readlines()[0]

def get_item(col_names)->str:
    return popen('python readItem.py "'+','.join(col_names)+'"').readlines()[0]

def mod_item(col_names,data)->str:
    s='python modItem.py '+','.join(col_names)+' "'+','.join([str(x)for x in data])+'"'
    return popen(s).readlines()[0]
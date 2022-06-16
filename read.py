from frames import *
from wx import App
global data
app=App()
data='nothing'
class iptDlg(InputFrame):
    def clicked(self, event):
        global data
        data=self.m_textCtrl.Value
        self.Close()
i=iptDlg(None)
i.Show()
app.MainLoop()
print(data)
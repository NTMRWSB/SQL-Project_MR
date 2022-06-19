from frames import *
import wx
from helper_func import Table
from sys import argv
global data,col_names
col_names=tuple(argv[1].split(','))
app=wx.App()

class AddFrame ( wx.Frame ):

    def __init__( self, parent ):
        global col_names
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"增加", pos = wx.DefaultPosition, size = wx.Size( 600,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        bSizers=[]
        self.m_staticTexts=[]
        self.m_textCtrls=[]

        for i in range(len(col_names)):
            bSizers.append(wx.BoxSizer( wx.HORIZONTAL ))
            self.m_staticTexts.append(wx.StaticText( self, wx.ID_ANY, col_names[i], wx.DefaultPosition, wx.DefaultSize, 0 ))
            bSizers[i].Add( self.m_staticTexts[i], 1, wx.ALL, 5 )
            self.m_textCtrls.append(wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ))
            bSizers[i].Add( self.m_textCtrls[i], 1, wx.ALL, 5 )
            bSizer.Add( bSizers[i], 1, wx.EXPAND, 5 )

        self.m_button = wx.Button( self, wx.ID_ANY, u"增加", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_button, 0, wx.ALL|wx.EXPAND, 5 )

        self.SetSizer( bSizer )
        self.Layout()
        self.Centre( wx.BOTH )
        # Connect Events
        self.m_button.Bind( wx.EVT_BUTTON, self.clicked )

    def __del__( self ):
        pass

    def clicked( self, event ):
        global data
        data=[x.Value for x in self.m_textCtrls]
        self.Close()
f=AddFrame(None)
f.Show()
app.MainLoop()
print(*data,sep=',')
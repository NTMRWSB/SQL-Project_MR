# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"登录", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,150 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text1.Wrap( -1 )

		gSizer1.Add( self.Text1, 0, wx.ALIGN_CENTER, 5 )

		self.textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrl1, 0, wx.ALIGN_CENTER, 5 )

		self.Text2 = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text2.Wrap( -1 )

		gSizer1.Add( self.Text2, 0, wx.ALIGN_CENTER, 5 )

		self.textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer1.Add( self.textCtrl2, 0, wx.ALIGN_CENTER, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.button = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button.Bind( wx.EVT_BUTTON, self.clicked )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def clicked( self, event ):
		event.Skip()


###########################################################################
## Class RegisterFrame
###########################################################################

class RegisterFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"注册", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,150 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 4, 2, 0, 0 )

		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text1.Wrap( -1 )

		gSizer1.Add( self.Text1, 0, wx.ALIGN_CENTER, 5 )

		self.textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrl1, 0, wx.ALIGN_CENTER, 5 )

		self.Text2 = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text2.Wrap( -1 )

		gSizer1.Add( self.Text2, 0, wx.ALIGN_CENTER, 5 )

		self.textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer1.Add( self.textCtrl2, 0, wx.ALIGN_CENTER, 5 )

		self.Text3 = wx.StaticText( self, wx.ID_ANY, u"级别", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text3.Wrap( -1 )

		gSizer1.Add( self.Text3, 0, wx.ALIGN_CENTER, 5 )

		self.textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrl3, 0, wx.ALIGN_CENTER, 5 )

		self.Text4 = wx.StaticText( self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text4.Wrap( -1 )

		gSizer1.Add( self.Text4, 0, wx.ALIGN_CENTER, 5 )

		self.textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrl4, 0, wx.ALIGN_CENTER, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.button = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button.Bind( wx.EVT_BUTTON, self.clicked )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def clicked( self, event ):
		event.Skip()


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,150 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"主面板", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer = wx.GridSizer( 0, 2, 0, 0 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"员工", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer1.Add( self.m_staticText16, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"共有 个员工", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer16.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"管理员工", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button5, 1, wx.ALL, 5 )


		bSizer16.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer16, 4, wx.EXPAND, 5 )


		gSizer.Add( bSizer1, 1, wx.ALIGN_CENTER, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"供应商", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		bSizer2.Add( self.m_staticText161, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"共有 个供应商", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer161.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"管理供应商", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer2.Add( bSizer161, 4, wx.EXPAND, 5 )


		gSizer.Add( bSizer2, 1, wx.ALIGN_CENTER, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText162 = wx.StaticText( self, wx.ID_ANY, u"商品", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )

		bSizer3.Add( self.m_staticText162, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer162 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"共有 种商品", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer162.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"管理商品", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer162.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer3.Add( bSizer162, 4, wx.EXPAND, 5 )


		gSizer.Add( bSizer3, 1, wx.ALIGN_CENTER, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText163 = wx.StaticText( self, wx.ID_ANY, u"订单", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText163.Wrap( -1 )

		bSizer4.Add( self.m_staticText163, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer163 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"已有 个订单", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer163.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"管理订单", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer163.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer4.Add( bSizer163, 4, wx.EXPAND, 5 )


		gSizer.Add( bSizer4, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( gSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.act )
		self.m_button1.Bind( wx.EVT_BUTTON, self.user_click )
		self.m_button5.Bind( wx.EVT_BUTTON, self.reg_click )
		self.m_button2.Bind( wx.EVT_BUTTON, self.company_click )
		self.m_button3.Bind( wx.EVT_BUTTON, self.goods_click )
		self.m_button4.Bind( wx.EVT_BUTTON, self.orders_click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def act( self, event ):
		event.Skip()

	def user_click( self, event ):
		event.Skip()

	def reg_click( self, event ):
		event.Skip()

	def company_click( self, event ):
		event.Skip()

	def goods_click( self, event ):
		event.Skip()

	def orders_click( self, event ):
		event.Skip()


###########################################################################
## Class GridFrame
###########################################################################

class GridFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"管理", pos = wx.DefaultPosition, size = wx.Size( 600,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.m_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid.CreateGrid( 5, 5 )
		self.m_grid.EnableEditing( True )
		self.m_grid.EnableGridLines( True )
		self.m_grid.EnableDragGridSize( False )
		self.m_grid.SetMargins( 0, 0 )

		# Columns
		self.m_grid.EnableDragColMove( False )
		self.m_grid.EnableDragColSize( True )
		self.m_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid.EnableDragRowSize( True )
		self.m_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer.Add( self.m_grid, 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"增加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button1, 1, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button2, 1, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button3, 1, wx.ALL, 5 )


		bSizer.Add( bSizer34, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.CellChange )
		self.m_button1.Bind( wx.EVT_BUTTON, self.add )
		self.m_button2.Bind( wx.EVT_BUTTON, self.delete )
		self.m_button3.Bind( wx.EVT_BUTTON, self.mod )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def CellChange( self, event ):
		event.Skip()

	def add( self, event ):
		event.Skip()

	def delete( self, event ):
		event.Skip()

	def mod( self, event ):
		event.Skip()


###########################################################################
## Class InputFrame
###########################################################################

class InputFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"输入", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"输入id", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.m_textCtrl, 1, wx.ALL, 5 )

		self.m_button = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.m_button, 0, wx.ALL, 5 )


		self.SetSizer( bSizer )
		self.Layout()
		bSizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button.Bind( wx.EVT_BUTTON, self.clicked )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def clicked( self, event ):
		event.Skip()



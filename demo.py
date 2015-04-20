#coding:utf-8
from pyh import *
#
#t=table()<<tr()在render的时候不会渲染table标签
# 需要先定义t＝table()，然后使用t<<tr()
class Generator(object):
	"""docstring for Generator"""

	def __init__(self):
		pass
		
	def makeTableWithSub(self,title,subtitle,infobuf=None):
		self.table=table(cl="cv_tablestyle")#创建一个table

		header=tr(td(title,cl="cv_tableheader"))#创建标题
		subheader=tr(td(subtitle,cl="cv_subheader"))#创建副标题
		content=tr(td("11111")+td("1111"))
		self.table<<header+subheader+content#依次拆入table标签
		
		return self.table

	def makeTable(self,title,infobuf=None):
		self.table=table(cl="cv_tablestyle")
		header=tr(td(title,cl="cv_tableheader"))
		content=tr(td("11111",cl="cv_content")+td("1111",cl="cv_content"))
		
		self.table<<header+content
		return self.table
	def makeprofile(self,infobuf):
		pass
		
page = PyH('My wonderful PyH page')
page.addCSS("style.css","style1.css")
g=Generator()


page<<g.makeTable(u"科研成果")

page<<g.makeTableWithSub(u"专利申请","111")



page.printOut("demohtml.html")
#coding:utf-8
from pyh import *
#
#t=table()<<tr()在render的时候不会渲染table标签
# 需要先定义t＝table()，然后使用t<<tr()
class Generator(object):
	"""docstring for Generator"""

	def __init__(self):
		pass

	def makeTableWithSub(self,title,subtitles,infobuf=None):
		"""
		生成带有副表头的表
		params:
			title:表头
			subtitles:包含副表头的列表
			infobuf:表格内容
		"""
		self.table=table(cl="cv_tablestyle")#创建一个table

		header=tr(td(title,cl="cv_tableheader",colspan=len(subtitles)))#创建标题
		#创建副标题
		srow=tr()
		for subtitle in subtitles:
			#依次将各个副标题作为列，插入
			srow<<td(subtitle,cl="cv_subheader")

		# 把表头和副表头都插入到表格中
		self.table<<tbody()<<header+srow


		# 开始创建内容
		for i in range(0,10):
			r=tr(cl="cv_content")#新建一行
			for j in range(0,len(subtitles)):#创建列，并逐个插入行中
				r<<td(i*"$",cl="cv_content")

			self.table<<r#把该行插入表格



		return self.table

	def makeTable(self,title,infobuf=None):
		"""
		生成带有表头的表
		params:
			title:表头
			infobuf:表格内容
		"""
		# 创建一个表
		self.table=table(cl="cv_tablestyle")
		# 创建表头
		header=tr(td(title,cl="cv_tableheader"))
		# 循环创建内容
		content=tr(td(u"""
			xxxx年－xxxx年，xx大学，机械工程学院，本科/学士<br/>
xxxx年－xxxx年，xx大学，机械工程学院，研究生/硕士<br/>
xxxx年－xxxx年，xx大学，机械工程学院，研究生/博士<br/>
			""",cl="cv_content"))

		self.table<<tbody()<<header+content
		return self.table

	def makeprofile(self,infobuf=None):
		self.table=table(cl="cv_tablestyle")#总表
		#3列td：图片占位，需要填写的信息，信息内容
		imagecol=td("",id="image",width="25%")
		infocol=td(id="info",width="25%",colspan="4")
		detailcol=td("",id="detail",width="50%")

		#infocol中包含一个表格，表格中包含4行tr
		titlerow=tr(td(u"职称"),cl="cv_profile")
		officerow=tr(td(u"办公室"),cl="cv_profile")
		telrow=tr(td(u"联系电话"),cl="cv_profile")
		emailrow=tr(td(u"E-mail"),cl="cv_profile")
		# detailcol中包含一个表格，表格中包含4行tr
		titleinfo=tr(td(u"教授"),cl="cv_profile")
		officeinfo=tr(td(u"机械楼"),cl="cv_profile")
		telinfo=tr(td(u"12312304"),cl="cv_profile")
		emailinfo=tr(td(u"hanxiaomax@qq.com"),cl="cv_profile")

		#先把4行插入表格，再把表格插入infocol这一列
		infocol<<table()<<titlerow+officerow+telrow+emailrow
		detailcol<<table()<<titleinfo+officeinfo+telinfo+emailinfo

		# 将3个td插入tr标签，再插入表格中
		self.table<<tbody()<<tr(imagecol+infocol+detailcol)
		return self.table

if __name__ == '__main__':
	page = PyH('My wonderful PyH page')
	page.addStyleSnippet("style.css")
	# page.addStyleSnippet('style.css') ＃或者可以把style.css中的代码插入html中
	g=Generator()#表格生成器

	subtitles1=[u"项目名称",u"项目类别",u"项目时间",u"工作类别",u"项目金额"]
	subtitles2=[u"专利号",u"专利名称",u"专利类型"]

	page<<g.makeprofile()
	page<<g.makeTable(u"学习经历")
	page<<g.makeTable(u"工作经历")
	page<<g.makeTable(u"教授课程")
	page<<g.makeTable(u"研究方向")
	page<<g.makeTable(u"获奖情况")
	page<<g.makeTable(u"论文著作")
	page<<g.makeTableWithSub(u"科研项目",subtitles1)
	page<<g.makeTableWithSub(u"专利",subtitles2)


	page.printOut("demohtml.html")#还可以把编码方式通过第二个参数传入


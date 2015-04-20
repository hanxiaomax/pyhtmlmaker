from pyh import *

mydiv=table()
mydiv<<tr()
print mydiv.render()
mydiv<<p("level 1",id="lvl1")
mydiv.lvl1<<span("level 2",id="lvl2")
mydiv.render()
mydiv.render("test.html")


from collections import OrderedDict

f_l=OrderedDict()

f_l['jen']='python'
f_l['sarah']='c'
f_l['edward']='ruby'
f_l['phil']='python'

for name,language in f_l.items():
	print(name.title()+"'s favorite language is "+language.title())


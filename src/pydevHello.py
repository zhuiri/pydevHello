

# print 'hello world'
# 
# poem = '''\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
#         use Python!
# '''
# 
# f = file('poem.txt', 'w') # open for 'w'riting
# f.write(poem) # write text to file
# f.close() # close the fil
# 
# 
# f = file('poem.txt','r')
# 
# while True:
#    line = f.readline()
#    if len(line) == 0:
#    	break
#    print line,
#    
# f.close()

# import cPickle as p
# #import pickle as p
# 
# shoplistfile = 'shoplist.data'
# # the name of the file where we will store the object
# 
# shoplist = {'apple', 'mango', 'carrot'}
# 
# # Write to the file
# f = file(shoplistfile, 'w')
# p.dump(shoplist, f) # dump the object to a file
# f.close()
# 
# del shoplist # remove the shoplist
# 
# # Read back from the storage
# f = file(shoplistfile)
# storedlist = p.load(f)
# print storedlist
   

# class Person:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print '(initializing %s)' % self.name
#         Person.population += 1
#
#     def sayHi(self):
#         print 'Hi, my nameff is %s.' % self.name
#
# Ren = Person('Ren')
# Ren.sayHi()
# print 'population %2.1f' % Person.population
#
#
from jinja2 import Environment, meta, PackageLoader, Template
#
# # env = Environment(loader=PackageLoader('pydevHello', 'templates'))
# # template = env.get_template('mytemplate.html')
# #
# # print template.render(the='variables', go='here')
# env = Environment()
# ast = env.parse('{% extends "layout.html" %}{% include helper %}')
# print list(meta.find_referenced_templates(ast))
#
# expr = env.compile_expression('foo == 43')
# print expr(foo=4)
#
# m = Template(u"{% set a, b = 'foo', 'goo' %}").module
# print m.a, m.b
#
# template = Template('Hello {{ name }}!!!')
# stream = template.stream(name='Joe')
# print [template.render(name='Ren'), stream.next()]
# print [template.render(knigts='that is')]

HTML = """
<html>
<head>
<title>{{title}}</title>
</head>
<body>
Hello.
</body>
</html>
"""


def print_html_doc():
    print [Environment().from_string(HTML).render(title='Hello Gist from Github')]

if __name__ == '__main__':
    print_html_doc()

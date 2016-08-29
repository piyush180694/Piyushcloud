#! /usr/bin/python2

print "content-type:text/html\n"

import cgi,MySQLdb,commands

var=cgi.FormContent()

f1=var['f'][0]
l1=var['l'][0]
user1=var['user'][0]
passwd1=var['passwd'][0]
e1=var['e'][0]
a1=var['a'][0]
pin1=var['pin'][0]
ph1=var['ph'][0]

x=MySQLdb.connect("localhost","root","redhat")

y=x.cursor()

y.execute('use user_pass;')

sql="""insert into reg values('{}','{}','{}','{}','{}','{}',{},{})""".format(f1,l1,user1,passwd1,e1,a1,pin1,ph1)

y.execute(sql)

x.commit()

commands.getoutput("python audio.py | festival --tts")

print """
	<form action='http://192.168.0.1/front.html' method='POST'>
	<h1>successful...!!!!!!!!!!<h1><br />
	<input type='submit' value='OK' />
	</form>
	"""



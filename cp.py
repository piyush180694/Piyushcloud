#! /usr/bin/python2

import cgi,MySQLdb

print 'content-type:text/html\n'

pc=cgi.FormContent()

np1=pc['rp1'][0]
np2=pc['rp2'][0]

if np1==np2:
	x=MySQLdb.connect('localhost','root','redhat')
	y=x.cursor()
	y.execute('use user_pass;')
	y.execute("update reg set password='{}' where uname='xyz';".format(np1))
	x.commit()
else:
	print '''
		<html>
		<style>
		div.cp
		{
		border:2px solid #e1e;
		border-radius:5px 5px 5px 5px;
		width:500px;
		height:300px;
		position:absolute;
		top:100px;
		left:350px;
		background:#00bfff;
		}
		</style>
		<body bgcolor='#00ffff'>
		<div class='cp'>
		<br /><br />
		<form action='http://192.168.0.1/cp.html' method='POST'>
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<b>password mismatch</b><br /><br />
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<b>Please enter to continue</b><br /><br /><br /><br />
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input type='submit' value='Enter' />
		</form> 
		</div>
		</body>
		</html>
		'''

#! /usr/bin/python2  

import commands,cgi,MySQLdb

print "content-type:text/html\n"

x=cgi.FormContent()

user=x['u'][0]
passwd=x['p'][0]
x=MySQLdb.connect('localhost','root','redhat')
y=x.cursor()
y.execute('use user_pass;')
y.execute('select uname,passwd from reg;')
z=y.fetchall()
lenth=len(z)
i=0
while i<=lenth-1:
	if user==z[i][0] and passwd==z[i][1]: 
		print '''
			<center>
			<form action='http://192.168.0.1/menu.html' method='POST'>
			<h1><b>Successful</b></h1>
			<b>Enter OK to go back</b><br /><br />&nbsp;&nbsp;&nbsp;&nbsp;
			<input type='submit' value='OK' />
			</form>
			</center>
			'''
		exit()
	else:
		#print
		if i==lenth-1:
			print '''
				<html>
				<style>
				div.left
				{
					//border:2px solid #00ffff;
					width:600px;
					height:100%;
					position:absolute;
					top:0px;
					left:400px;
					text-align:center;
					background:#00bfff;
					color:white;
					//border-radius:10px 10px 10px 10px;
					box-shadow:2px 2px #87ceeb
				}
				input#li
				{
					width:200px;
					height:50px;
					background:#0080ff;
					border:0px;
				}
				a#fp
				{
					color:blue;
				}
				a:hover#fp
				{
					color:white;
				}
				div#err
				{
					position:absolute;
					top:50px;	
					width:300px;
					height:50px;
				}
				p#berr
				{
					color:blue;
				}
				</style>
				<body>
				<div class='left'>
				<h1><b>Login Form</h1></b><br /><br /><br />
				<div class='err'>
				<p id='berr'>ERROR: Login failed due to username and password mismatch. Try again.</p>
				</div>
				<form action='http://192.168.0.1/cgi-bin/cloud/signin.py' method='POST'>
				<h2><b>Username</b></h2><input type='text' name='u' class='inp' placeholder="Enter Username" style='text-align:center;' /><br/>
				<h2><b>Password</b></h2><input type='password' name='p' class='inp' placeholder="Enter Password" style='text-align:center;' /><br /><br /><br />
				<input type='submit' value="sign in" id='li' /><br /><br />
				</form>
				<a href='http://192.168.0.1/fgt.html' id='fp'>Forgot password</a><br /><br />
				</div>
				</body>
				</html>
				'''
			i+=1
			exit()	
			
		else:
			i+=1



	








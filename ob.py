#! /usr/bin/python2

import commands

print '''
	<form action='http://192.168.0.1/cgi-bin/cloud/ob_a.py' method=POST>
	<b>Type:</b><br />
	Static<input type='checkbox' name='ch' />
	Scalable<input type='checkbox' name='ch' /><br /><br />
	method:<select name='m'>
	<option>Secure</option>
	<option>Unsecure</option>
	</select><br /><br />
	Size(in MB):<input type='text' name='sz' /><br /><br />
	<input type='submit' value='submit' />
	</form>	
	'''

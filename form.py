#! /usr/bin/python2

import cgi

print 'content-type:text/html'

x=cgi.FormContent()

user=x['u'][0]

passwd=x['p'][0]

if user=='avdhesh' and passwd=='sharma':
	print 
	print 'OK'
else:
	print 'location:http://192.168.0.1/form.html\n'



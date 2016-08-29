#! /usr/bin/python2

import cgi,cgitb

from os import environ

if environ.has_key('HTTP_COOKIE'):
	for cookie in map(strip,split(environ['HTTP_COOKIE'],';')):
		(key,value)=split(cookie,'=')
		if key=='UserID':
			user_id=value
		elif key=='Password':
			password=value
	print 'User_ID = {}'.format(user_id)
	print 'Password = {}'.format(password)

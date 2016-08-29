#! /usr/bin/python2

print 'content-type:text/html\n'

import commands 

#print commands.getoutput("sudo echo Welcome to my project. Please stay on the line. You will be contacted soon.  |  festival  --tts")

print commands.getoutput("sudo echo hello")

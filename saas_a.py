#! /usr/bin/python2

print 'content-type:text/html\n'

import cgi,commands,os
ch=cgi.FormContent()

s=ch['soft'][0]

cip=os.environ.get('REMOTE_ADDR')

#print '{} : {} : {} : {}'.format(name,passwd,s,cip)

list1=['/usr/bin/firefox','/usr/bin/google-chrome','/usr/bin/gnome-terminal','/usr/bin/xterm','/usr/sbin/wireshark','/usr/bin/virt-viewer','/usr/bin/virt-manager']

def f1(x):
	#status1=commands.getstatusoutput("sudo useradd -s {} {}".format(x,name))
	#status2=commands.getstatusoutput("sudo echo {} | passwd  {}  --stdin".format(passwd,name))
	fh=open("/var/www/cgi-bin/file/{}".format(s),"w+")
	fh.write("#! /bin/bash\n\nsshpass -p redhat ssh -X -l aks1 192.168.0.1 {}".format(s))
	fh.close()
	commands.getstatusoutput("sudo chmod  +x /var/www/cgi-bin/file/{}")
	status3=commands.getstatusoutput("sudo sshpass -p redhat scp /var/www/cgi-bin/file/{}  {}:/root/Desktop/".format(s,cip))
	#status4=commands.getstatusoutput("sudo rm -rvf /var/www/cgi-bin/file/{}.sh".format(s))
	if status3[0]==0:
		print "Successful....!!!!!!!!!"
	else:
		print "Failure.......!!!!!!!!!!!!"	

if s=='firefox':
	f1(list1[0])
elif s=='google-chrome':
	f1(list1[1])
elif s=='gnome-terminal':
	f1(list1[2])
elif s=='xterminal':
	f1(list1[3])
elif s=='wireshark':
	f1(list1[4])
elif s=='virt-viewer':
	f1(list1[5])
else:
	f1(list1[4])






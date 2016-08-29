#! /usr/bin/python2

print 'content-type:text/html\n'

import commands,time

dir1='aks2'

sz=8

x1=commands.getstatusoutput('sudo lvcreate --name {} --size {}M  myvg'.format(dir1,sz))

x2=commands.getstatusoutput('sudo mkfs.ext4  /dev/myvg/{}'.format(dir1))

x3=commands.getstatusoutput('sudo mkdir /{}'.format(dir1))

x4=commands.getstatusoutput('sudo chmod 777 /{}'.format(dir1))

x6=commands.getstatusoutput('sudo chown apache /{}'.format(dir1))

x7=commands.getstatusoutput('sudo chgrp apache /{}'.format(dir1))

x5=commands.getstatusoutput('sudo  mount  -t  ext4   /dev/myvg/{}   /{}'.format(dir1,dir1))

time.sleep(2)

if x1[0]==0 and x2[0]==0 and x3[0]==0 and x4[0]==0 and x5[0]==0 and x6[0]==0 and x7[0]==0:
	print 'success'
else:
	print 'failure'

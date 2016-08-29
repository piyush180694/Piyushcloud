#! /usr/bin/python2

print 'content-type:text/html\n'
import cgi,commands,os,cgitb,time
cgitb.enable()

x=cgi.FormContent()
tp=x['ch'][0]
vname=x['vn'][0]
aname=x['an'][0]
sz=x['s'][0]
mtd=x['sec'][0]

#print "{} : {} : {} : {} : {}".format(tp,vname,sz,mtd,aname)


cip=os.environ.get('REMOTE_ADDR')
#print "Your ip is {}".format(cip)


if mtd=='unsecure':
	#commands.getstatusoutput('sudo echo -e '\n\n\n' |  ssh-keygen')
	#x11=commands.getstatusoutput('sudo sshpass -p redhat ssh-copy-id root@{}'.format(cip))
	commands.getstatusoutput("sudo  lvcreate --name {} --size  {}M  akvg".format(cip,sz))
	commands.getstatusoutput("sudo  mkfs.ext4  /dev/akvg/{}".format(cip))
	commands.getstatusoutput('sudo  mkdir /mnt/{}'.format(cip))
	x4=os.system("sudo  mount  /dev/akvg/{}  /mnt/{}".format(cip,cip))
	time.sleep(3)
	if x4==0:
		print 'success'
		print x4
	else:
		print 'failure'
		print x4

	'''

	x5=commands.getstatusoutput("sudo echo  '/{}   {}(rw,no_root_squash)'  >>/etc/exports".format(vname,cip))
	x6=commands.getstatusoutput('sudo systemctl restart nfs-server')
	x7=commands.getstatusoutput('exportfs -r')
	commands.getstatusoutput("sudo mkdir /root/Desktop/{}".format(vname))
	fh=open('/root/Desktop/{}'.format(aname),mode='w+')
	fh.write("#! /bin/bash\nmkdir /media/{}\n\nmount 192.168.0.1:/{}  /media/{}".format(vname,vname,vname))
	fh.close()
	commands.getstatusoutput('sudo mv /root/Desktop/{}  /root/Desktop/{}'.format(aname,vname))
	commands.getstatusoutput('sudo tar -cvf /root/Desktop/{}-11-04-16.tar  /root/Desktop/{}'.format(vname,vname))
	sh=commands.getstatusoutput('sudo scp  /root/Desktop/{}-11-04-16.tar  {}:/root/Desktop'.format(vname,cip))
	if sh[0]==0:
		print "<pre>"
		print "<b>Volume has been successfully assigned</b>"
		print "<b>Double click the tar file to get the bucket</b>"
		print "</pre>"
	else: 	
		print "Failure"
		#print sh[1]
	
	'''
	
	
elif mtd=='secure':
	print "sshfs"
else: 
	print 'samba'







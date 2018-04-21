#-*- coding=utf-8
import pexpect  
  
ip="192.168.32.51"  
username='watson'
old_passwd='1234qwer'
new_passwd='1qaz@WSX3edc'
  
child=pexpect.spawn('ssh  %s@%s' % (name,ip)  )  
child.expect ('(yes/no)?') 
child.sendline('yes')  
 
child.expect ('password:')  
child.sendline(old_passwd)
child.expect ('UNIX password:')  
child.sendline(old_passwd)
child.expect ('New password:')  
child.sendline(new_passwd)
child.expect ('Retype new password:')  
child.sendline(new_passwd)
  
child.interact()  
child.close()

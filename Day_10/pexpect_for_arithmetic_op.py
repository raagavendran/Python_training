import pexpect
import sys
m = pexpect.spawn('python arithmetic_op.py')
m.logfile_read = sys.stdout
m.expect("Enter your a: ")
m.sendline("10")
m.expect("Enter your b: ")
m.sendline("20")
m.expect("Enter operator: ")
m.sendline("+")
m.expect("end")
m.close()

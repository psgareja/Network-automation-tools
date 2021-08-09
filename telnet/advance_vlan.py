import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet usernem: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"useranme: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
for i in range(2,11):

    tn.write(b"vlan "+str(n)+"\n")
    tn.write(b"name Python_VLAN "+str(n)+"\n")



tn.write(b"sh vlan brief\n")

tn.write(b"end \n")




tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
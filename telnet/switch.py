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
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN 2\n")

tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN 3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN 4\n")

tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN 5\n")
tn.write(b"vlan 6\n")
tn.write(b"name Python_VLAN 6\n")
tn.write(b"vlan 7\n")
tn.write(b"name Python_VLAN 7\n")
tn.write(b"vlan 8\n")
tn.write(b"name Python_VLAN 8\n")
tn.write(b"sh vlan brief\n")

tn.write(b"end \n")




tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
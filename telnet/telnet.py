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
tn.write(b"int loop 0\n")
tn.write(b"ip 1.1.1.1 255.255.255.255\n")
tn.write(b"end \n")




tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
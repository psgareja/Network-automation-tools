from napalm import get_network_driver
driver=get_network_driver('ios')
iosvl2=driver("ip",'username','pass')
iosvl2.open()
ios_ouput=iosvl2.get_facts()
print(ios_ouput)
ios_ouput2=iosvl2.get_interfaces_counters()
ios_ouput3=iosvl2.get_interfaces()
ios_mac=iosvl2.get_macaddress()

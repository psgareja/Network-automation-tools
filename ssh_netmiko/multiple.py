iosv_l2={
    'device_type':'cisco_ios',
    'ip':'192.168.1.1',
    'username':'pradip',
    'password':'cisco'


}
iosv_l3={
    'device_type':'cisco_ios',
    'ip':'192.168.1.1',
    'username':'pradip',
    'password':'cisco'


}
iosv_l4={
    'device_type':'cisco_ios',
    'ip':'192.168.1.1',
    'username':'pradip',
    'password':'cisco'


}
all_devices=[iosv_l2,iosv_l3,iosv_l4]
for device in all_devices:
    net_connect=ConnectHandler(**device)
output=net_connect.send_command('show ip int brief')
print(output)
config_commands=['int loop 0','ip address 1.1.1.1 255.255.255.255']
output=net_connect.send_config_set(config_commands)
print(output)
for n in range(2,21):
    print("create vlan"+str(n))
    config_commands=['vlan '+str(n),'name Python_VLAN '+str(n)]
    output=net_connect.send_config_set(config_commands)
    print(output)

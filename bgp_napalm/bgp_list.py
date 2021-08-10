import json
from napalm import get_network_drivers
bgplist=['192.167.2.1','192.167.2.3']
for ip_add in bgplist:
    print("Connecting to "+str(ip))
    driver=get_network_driver('ios')
    ios_router=driver(ip_add,'user','pass')
    iosv_router.open()
    print(json.dump(bgp_neighbours,indent=4))
    ios_router.close()
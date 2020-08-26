# import netifaces
# import ipaddress
#
# ips = []
# for interface in netifaces.interfaces():
#     # print(interface)
#     # print(type(netifaces.ifaddresses(interface)))
#     if 2 in netifaces.ifaddresses(interface).keys():
#         for ip in netifaces.ifaddresses(interface)[2]:
#             ips.append(ip['addr'])
# for ip in ips:
#     try:
#         ip = ipaddress.ip_address(ip)
#         print(ip, type(ip))
#         ip.is_global
#     except Exception as e:
#         pass

import zerorpc
import threading
c = zerorpc.Client()
c.connect('tcp://127.0.0.1:9000')
# print(c.hello('client test str'))
# print(c.hello(['client test str']))
# print(c.hello({'msg': 'client test str'}))

e = threading.Event()
while  not e.wait(3):
    print(c.hello('client test str'))
c.close()
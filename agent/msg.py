import uuid
import socket
import os
import time
import datetime
import netifaces
import ipaddress

class Message:
    def __init__(self, myidpath):
        self.id = ''

        if os.path.exists(myidpath):
            with open(myidpath, encoding='utf-8') as f:
                id = f.readline().strip()
                if len(id) == 32:
                    self.id = id
        if not self.id:
            self.id = uuid.uuid4().hex
            with open(myidpath, 'w', encoding='utf-8') as f:
                f.write(self.id)
    def _get_adress(self):
        addresses = []
        for iface in netifaces.interfaces():
            ipv4s = netifaces.ifaddresses(iface).get(2, [])
            for ip in ipv4s:
                ip = ipaddress.ip_address(ip.get('addr'))
                if ip.version != 4:
                    continue
                if ip.is_link_local:
                    continue
                if ip.is_loopback:
                    continue
                if ip.is_multicast:
                    continue
                if ip.is_reserved:
                    continue
                addresses.append(str(ip))
        return  addresses
    def reg(self):
        return {
            'id': self.id,
            'hostname': socket.gethostname(),
            'timestamp': datetime.datetime.now().timestamp(),
            'ip': self._get_adress()
        }
    def heartbeat(self):
        return {
            'id': self.id,
            'hostname': socket.gethostname(),
            'timestamp': datetime.datetime.now().timestamp(),
            'ip': self._get_adress()
        }
    def result(self, task_id, code, output):
        return {
            'id': self.id,
            'task_id': task_id,
            'code': code,
            'output': output
        }
if __name__ == '__main__':
    m = Message('d:/test/myid')
    print(m.reg())
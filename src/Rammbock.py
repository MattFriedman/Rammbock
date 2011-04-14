from Interface import Interface
from Client import Client
from Server import Server

class Rammbock(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.interfaces = {}

    def use_virtual_interface(self, if_alias, ifname, ip_address, netmask):
        print "use_virtual_interface " + if_alias
        if self.interfaces.has_key(if_alias) == True:
            if self.interfaces[if_alias].ifUp == True:
		        return
        else:
            self.interfaces[if_alias] = Interface()

        self.interfaces[if_alias].create_virtual_interface(if_alias, ifname, ip_address, netmask)

    def use_interface(self, if_alias, ifname, ip_address = None, netmask = None, 
                      virtual_interface = False):
        print "use_interface " + if_alias
        if virtual_interface:
            self.use_virtual_interface(if_alias, ifname, ip_address, netmask)
        else:
            self.interfaces[if_alias] = Interface()
            self.interfaces[if_alias].create_physical_interface(if_alias, ifname, ip_address, netmask)
 

    def is_interface_up(self, ifname):
        self.interfaces
        print "is_interface_up " + ifname
        return self.interfaces[ifname].check_interface()

    def delete_interface(self, ifname):
        self.interfaces
        print "delete_interface " + ifname
        return self.interfaces[ifname].del_interface()
    
    def start_server(self, if_alias, port):
        self._server = Server(self.interfaces)
        self._server.server_startup(if_alias, port)

    def connect_to_server(self, host, port):
        self._client = Client()
        self._client.establish_connection_to_server(host, port)

    def close_server(self):
        self._server.close_server()
         
    def close_client(self):
        self._client.close_client()

    def send_packet_over_udp(self, packet): 
        self._client.send_packet_over_udp(packet)
     
    def receive_packet_over_udp(self):
        return self._server.receive_packet_over_udp()  
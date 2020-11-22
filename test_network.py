from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.link import TCLink


class AttackTopo( Topo ):

	def __init__( self ):

		Topo.__init__( self )

		#10.0.0.50
		h1 = self.addHost('h1', ip="10.0.0.50")
		evil = self.addHost ( 'evil', ip='10.0.0.53')
		dhcp = self.addHost('dhcp', ip='10.0.0.66')
		mainSwitch = self.addSwitch('s1')


		self.addLink(h1, mainSwitch)
		self.addLink(evil, mainSwitch)
		self.addLink(dhcp, mainSwitch, delay='500ms')


def simulate():
	topology = AttackTopo()
	net = Mininet(topo=topology, link=TCLink)
	net.start()	
	h1, dhcp, evil = net.get('h1', 'dhcp', 'evil')
	print(dhcp.defaultIntf())
	CLI(net)
	net.stop()

simulate()

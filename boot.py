import network
import socket
import webrepl
import time
from machine import Pin


########## Config ############
WifiSSID="ClarkQAQ"
WifiPass="clarkclark"
SocketPort=25
########## Config ############

wlan=None
listenSocket=None

ap = network.WLAN(network.AP_IF)
ap.active(False)

def connectWifi(ssid, passwd):
	global wlan
	wlan=network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.scan()
	wlan.isconnected()
	wlan.connect(ssid, passwd)
	#while(wlan.ifconfig()[0]=='0.0.0.0'):
		#time.sleep(2)
		#print("ReconnectWifi!")
		#return connectWifi(ssid, passwd)
	return True
 
connectWifi(WifiSSID, WifiPass)
ip=wlan.ifconfig()[0]
import time
time.sleep(2)
print(ip)
listenSocket = socket.socket()
listenSocket.bind((ip, SocketPort))
listenSocket.listen(10)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#print ('tcp waiting...')
while True:
	#print("accepting.....")
	conn,addr = listenSocket.accept()
	#print(addr,"connected")
	while True:
		data = conn.recv(1024).decode()
		if(len(data) == 0):
			#print("close socket")
			conn.close()
			break
		string = data.split('#')
		#print("id:",string[0],"iv:",string[1])
		try:
			Pin(int(string[0]), Pin.OUT).value(int(string[1]))
		except:
			conn.send("err")
			conn.close()
			break
		else:
			conn.send("ok")
			conn.close()
			break

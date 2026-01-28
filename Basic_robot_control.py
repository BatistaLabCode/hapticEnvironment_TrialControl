import socket
import msgpackrpc
import messageDefinitions as MD
import time
from haptics import *
from graphics import enableGraphics, makeBox, makeTorus


THIS_PORT = 8000

MY_IP = "127.0.0.1"

RPC_IP = "127.0.0.1" # Ip of messenger
RPC_PORT = 2000

global client
client = msgpackrpc.Client(msgpackrpc.Address(RPC_IP, RPC_PORT))

client.call("addModule", 2, MY_IP, THIS_PORT)
client.call("subscribeTo", 2, 999)
time.sleep(5) #let system register

def makeAndSendMessage(message):
  message.header.serial_no = client.call_async("getMsgNum").get()
  message.header.timestamp = client.call_async("getTimestamp").get()
  client.call_async("sendMessage", bytes(message), sizeof(message), 2)

sessionStart = MD.M_SESSION_START()
sessionStart.header.msg_type = c_int(MD.SESSION_START)
makeAndSendMessage(sessionStart)
print('session started')
time.sleep(2.0)

freezeTool('initial')

while 1:
    time.sleep(20)


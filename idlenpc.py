#!/usr/bin/env python

# IdleNPC
# https://github.com/mozor/idlenpc

import socket  
import sys
import time
server = "irc.mozor.net" 
channel = "#idlerpg"
botnick = sys.argv[1]
master = "IdleBOT"
host = '[IPV6]'

def ping(): 
  ircsock.send("PONG :Pong\n")

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

def id(master): 
  ircsock.send("PRIVMSG "+ master +" :LOGIN "+ botnick +" examplepass\n")

ircsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
ircsock.bind((host, 0))
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Mega Python IdleRPG Master\n")
ircsock.send("NICK "+ botnick +"\n") 
time.sleep(5)

joinchan(channel) 
id(master)

while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r')
  print(ircmsg)

  if ircmsg.find("PING :") != -1:
    ping()
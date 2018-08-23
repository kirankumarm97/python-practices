from socket import *
sn='DESKTOP-4DQ5G1E'
sp=1222
ss=socket(AF_INET,SOCK_DGRAM)
ss.bind((sn,sp))
while 1:
    msg,adr=ss.recvfrom(2048)
    msg1=msg1.upper()
    ss.sendto(bytes(msg1,'utf-8'),adr)

from socket import *
sn='DESKTOP-4DQ5G1E'
sp=1222
cs=socket(AF_INET,SOCK_DGRAM)
mesage=input()
cs.sendto(bytes(mesage,'utf-8'),(sn,sp))
rm,seeveradd=cs.recvfrom(2048)
print(rm)
cs.close()

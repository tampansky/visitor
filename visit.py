import requests,random,sys,time,os,base64,readline
from thread import *
os.system("clear")
heder = requests.get("https://raw.githubusercontent.com/tampansky/visitor/master/user-age.txt").text
heder = heder.split("\n")
h = '\033[92m'
p = '\033[97m'
m = '\033[91m'
br = '\033[94m'
___banner___ = '''
------------------------------------------
[+] Bot Auto Visitor Blogger / Website
[+] Author : Tampansky
[+] YouTube : Tampansky ID
[+] Github : http://github.com/tampansky
------------------------------------------
'''
print(___banner___)
ip = raw_input("[+] Website Name : ")
if "http" not in ip:
   ip = "https://{}".format(ip)
try:
   requests.get(ip)
except:
   print ("Website not found or Connection Failed,aborting")
   sys.exit()

thr = int(raw_input("Speed (normal : 50) : "))
def atk(proto):

    while True:
      time.sleep(0.2)
      rand = random.choice(heder)
      try:
	a = requests.get(proto,headers = {'User-Agent': rand})
	if (str(a)) == "<Response [200]>":
	   print ("[" + str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) + "] Berhasil Mengirim Bot... ")
	else:
	   print ("This Website Is Protected By Cloudflare, This Attack Will Give No Effect")
      except requests.exceptions.ConnectionError:
	print ("No Connection Or Server Maybe Down")

bi = ""

def kita():
    tred = threading.Thread(target=atk)
    tred.daemon = True
    tred.start()
    time.sleep(2)
    for i in range(thr):
      tred.join()

def lol(bi):
  while True:
   for i in range(thr):
    start_new_thread(atk,(ip,))
    print ("["+ str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) +"] Thread ...")
    time.sleep(1.5)
   print ("Thread Already Full,Restarting")
   time.sleep(2)
lol(bi)

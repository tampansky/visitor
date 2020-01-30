import requests,random,sys,time,os,base64,readline,curses 
from thread import *
os.system("clear")
heder = requests.get("https://raw.githubusercontent.com/tampansky/visitor/master/user-age.txt").text
heder = heder.split("\n")
h = '\033[92m' 
p = '\033[97m'
m = '\033[91m'
br = '\033[94m'
def mengetik(s):
    for c in s + '':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)
mengetik('''{}
---------------------------------------------{}
$ Auto Visitor  |        _     _         V1.0
$ Black Coders  | /\   /(_)___| |_ ___  _ __ 
$ Auto Visitor  | \ \ / / / __| __/ _ \|  __|
$ Black Coders  |  \ V /| \__ \ || (_) | |   
$ Auto Visitor  |   \_/ |_|___/\__\___/|_|  {}
---------------------------------------------
[{}~{}]{} Bot Auto Visitor Blogger / Website {}
[{}~{}]{} Author : Tampansky {}
[{}~{}]{} YouTube : Tampansky ID {}
[{}~{}]{} Github : http://github.com/tampansky {} 
---------------------------------------------
'''.format(p,br,p,m,p,h,p,m,p,h,p,m,p,h,p,m,p,h,p))
___banner___ = '''Note : Author Tidak Bertanggung jawab, atas dosa yang kalian perbuat ini, tools ini di buat hanya untuk bersenang senang saja
---------------------------------------------'''
print(___banner___)
ip = raw_input("[{}+{}] Website Name : ".format(m,p))
if "http" not in ip:
   ip = "https://{}".format(ip)
try:
   requests.get(ip) 
except:
   os.system("clear")

   print ("{}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}]{} Website not found or Connection Failed,aborting".format(p,m))
   sys.exit()

thr = int(raw_input("[{}+{}] Speed (normal : 10) : ".format(m,p)))
def atk(proto):

    while True:
      time.sleep(0.2)
      rand = random.choice(heder)
      try:
	a = requests.get(proto,headers = {'User-Agent': rand})
	if (str(a)) == "<Response [200]>":
	   print ("\t {}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}Berhasil Mengirim Bot{} ".format(p,br,p))
	else:
	   print ("\t {}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}This Website Is Protected By Cloudflare {}".format(p,m,p))
      except requests.exceptions.ConnectionError:
	print ("\t {}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}No Connection Or Server Maybe Down{}".format(p,m,p))

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
    print ("\t {}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) +"{}] {}Thread...{}".format(p,br,p))
    time.sleep(0.25)
   print ("\t {}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}Thread Already Full{}".format(p,m,p))
   time.sleep(2)
lol(bi)

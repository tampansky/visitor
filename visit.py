import requests,random,sys,time,os,base64,readline,curses 
from thread import *
os.system("clear")
heder = requests.get("https://raw.githubusercontent.com/tampansky/visitor/master/user-age.txt").text
heder = heder.split("\n")
#FONT COLOR
h = '\033[92m' # hijau
p = '\033[97m' # putih
m = '\033[91m' # merah
br = '\033[94m' # biru
y = '\033[1;33m' # kuning
blck = "\033[0;30m" #hitam
bu = "\033[0;33m" #abu Abu
pur = "\033[0;35m" # purpel
cy = "\033[0;36m" # cyan
# FONT TYPE
faint = "\033[2m" # faint 
bol = "\033[1m" # bold
ita = "\033[3m" # italic
nega = "\033[7m" # negativ
under = "\033[4m" # underline
blink = "\033[5m" # blink
end = "\033[0m" # end
cros = "\033[9m" #crossed
print("tunggu sebentar")
time.sleep(1)
os.system("clear")
print("loading.")
time.sleep(1)
os.system("clear")
print("loading..")
time.sleep(1)
os.system("clear")
print("loading...")
time.sleep(1)
os.system("clear")
print("{}Subscribe channel {}Tampansky ID{}".format(h,under,end))
time.sleep(5)
os.system("xdg-open https://www.youtube.com/c/TampanskyID")
os.system("clear")
time.sleep(4)
def mengetik(s):
    for c in s + '':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)
mengetik('''{}
---------------------------------------------{}
$ Auto Visitor  |        _     _         {}V1.0{}{}
$ Black Coders  | /\   /(_)___| |_ ___  _ __ 
$ Auto Visitor  | \ \ / / / __| __/ _ \|  __|
$ Black Coders  |  \ V /| \__ \ || (_) | |   
$ Auto Visitor  |   \_/ |_|___/\__\___/|_|  {}
---------------------------------------------
[{}~{}]{} Bot Auto Visitor Blogger / Website {}
[{}~{}]{} Author : {}Tampansky{} 
[{}~{}]{} YouTube : {}Tampansky ID{}
[{}~{}]{} Github : {}http://github.com/tampansky{} 
---------------------------------------------
Note : Author Tidak Bertanggung jawab, atas dosa yang kalian perbuat ini, tools ini di buat hanya untuk bersenang senang saja
---------------------------------------------
'''.format(p,br,under,end,br,p,m,p,h,p,m,p,h,under,end,m,p,h,under,end,m,p,h,under,end)) 
ip = raw_input("[{}+{}] Website Name : {}".format(m,p,under))
if "http" not in ip:
   ip = "https://{}".format(ip)
try:
   requests.get(ip)
except:
   os.system("clear")

   print ("{}[{}".format(p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}]{} Website not found or Connection Failed,aborting".format(p,m))
   sys.exit()

thr = int(raw_input("{}[{}+{}] Speed (normal : 10) : {}".format(end,m,p,under)))
def atk(proto):

    while True:
      time.sleep(0.2)
      rand = random.choice(heder)
      try:
	a = requests.get(proto,headers = {'User-Agent': rand})
	if (str(a)) == "<Response [200]>":
	   print ("\t{}{}[{}".format(end,p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}Berhasil Mengirim Bot{} ".format(p,br,p))
	else:
	   print ("\t{}{}[{}".format(end,p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}This Website Is Protected By Cloudflare {}".format(p,m,p))
      except requests.exceptions.ConnectionError:
	print ("\t{}{}[{}".format(end,p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}No Connection Or Server Maybe Down{}".format(p,m,p))

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
    print ("\t{}{}[{}".format(end,p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) +"{}] {}Thread [+]{}".format(p,br,p))
    time.sleep(0.25)
   print ("\t{}{}[{}".format(end,p,h) + str(time.localtime()[3]) + "{}:{}".format(p,h) + str(time.localtime()[4]) + "{}:{}".format(p,h) + str(time.localtime()[5]) + "{}] {}Thread Already Full [0]{}".format(p,m,p))
   time.sleep(2)
lol(bi)

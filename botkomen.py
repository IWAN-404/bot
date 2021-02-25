# coding=utf-8
import requests,os,sys,re
import datetime,random,json,time,sys
from threading import Thread
reload(sys)
sys.setdefaultencoding('utf8')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def keluar():
    print '\033[0;97m$ \033[0;93mSampai Jumpa Kembali :)\033[0;97m'
    os.sys.exit()


logo = """     
 \033[0;91m ____   ____ _______   _  ______  __  __ ______ _   _ 
\033[0;91m |  _ \ / __ \__   __| | |/ / __ \|  \/  |  ____| \ | |
\033[0;91m | |_) | |  | | | |    | ' / |  | | \  / | |__  |  \| |
 \033[0;91m|  _ <| |  | | | |    |  <| |  | | |\/| |  __| | . ` |
\033[0;91m | |_) | |__| | | |    | . \ |__| | |  | | |____| |\  |
\033[0;91m |____/ \____/  |_|    |_|\_\____/|_|  |_|______|_| \_|
\033[1;91m───────────────────────────────────────────────────── 
\033[1;93m Create \033[1;91m:\033[1;93m Iwan Hadiansah ID      
\033[1;93m Group\033[1;91m  :\033[1;93m VIRAL      
\033[1;93m Github\033[1;91m :\033[1;93m github.com/IWAN-404      
\033[1;91m───────────────────────────────────────────────────── 
 """


def login():
	os.system('clear')
	print logo
	try:
		jalan ("\033[0;93m Tools Ini Menggunakan Cookie Facebook  ")
		jalan ("\033[0;93m Silahkan Masukan Cookie Facebook Anda \n")
		cookie = raw_input("\033[0;97m{\033[0;93m?\033[0;97m} Cookie \033[0;91m>\033[0;93m ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		pup = open('coki.log', 'w')
		pup.write(cookie)
		pup.close()
		pip = open('login.txt', 'w')
		pip.write(hasil)
		pip.close()
		print ' '
		jalan ('\033[0;97m{\033[0;92m√\033[0;97m} \033[0;92mLogin Berhasil')
		time.sleep(2)
		menu()
	except AttributeError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie Salah'
		time.sleep(2)
		login()
	except UnboundLocalError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie Salah'
		time.sleep(2)
		login()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '\033[0;97m{\033[0;91m!\033[0;97m} Koneksi Bermasalah'
		exit()

def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		login()
	try:
		o = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		op = json.loads(o.text)
		a = op['name']
	except UnboundLocalError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie Invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		login()
	except KeyError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie Invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		login()
	except requests.exceptions.ConnectionError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Koneksi Bermasalah !'
		exit()
	print logo
	jalan ('\033[0;97m Halo Selamat Datang, Semoga Hari Mu Menyenangkan :) ');time.sleep(0.09)
	jalan ('\033[0;91m•> \033[0;97mNama \033[0;91m:\033[0;93m '+a+'\n');time.sleep(0.09)
	print ('\033[0;97m1) Bot Komen Facebook');time.sleep(0.09)
	print ('\033[0;97m2) Follow/Add My Facebook');time.sleep(0.09)
	print ('\033[0;97m3) Join Group');time.sleep(0.09)
	print ('\033[0;91m0\033[0;37m) Keluar\n');time.sleep(0.09)
	pilih_menu()
		
def pilih_menu():
	masok = raw_input('\033[0;97m{\033[0;93m?\033[0;97m} Pilih \033[0;91m> \033[0;93m')
	if masok =="":
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi yg benar'
		pilih_menu()
	elif masok == "1":
		bot_komen()
	elif masok == "2":
		jalan ('\n\033[0;93m •••\033[0;91m> \033[0;93mAnda Akan Di Arahkan Ke Browser')
		os.system('xdg-open https://www.facebook.com/Romi.Uyey')
		raw_input('\n\033[0;91m[ \033[0;97mTekan Enter Untuk Kembali\033[0;91m ]')
		menu()
	elif masok == "3":
		jalan ('\n\033[0;93m •••\033[0;91m>\033[0;93m Anda Akan Di Arahkan Ke Group')
		os.system('xdg-open https://www.facebook.com/groups/453688872336137')
		raw_input('\n\033[0;91m[ \033[0;97mTekan Enter Untuk Kembali\033[0;91m ]')
		menu()
	elif masok == "0":
		keluar()
	else:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi yg benar'
		pilih_menu()
    #cok = requests.get(url + tot['href'], headers=headers, cookies=cookies).text
    
def bot_komen():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except KeyError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		exit()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		k = json.loads(o.text)
		a = k['name']
	except AttributeError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		exit()
	print logo
	jalan ('\033[0;91m•> \033[0;97mNama \033[0;91m:\033[0;93m '+a+'\n');time.sleep(0.09)
	print ('\033[0;97m1) Komentar Manual');time.sleep(0.09)
	print ('\033[0;97m2) Komentar Kata Lucu');time.sleep(0.09)
	print ('\033[0;97m3) Komentar Kata Motivasi');time.sleep(0.09)
	print ('\033[0;97m4) Komentar Kata Kasar');time.sleep(0.09)
	print ('\033[0;97m5) Komentar Kata Main Tebakan');time.sleep(0.09)
	print ('\033[0;97m6) Komentar Kata Random');time.sleep(0.09)
	print ('\033[0;91m0\033[0;97m) Back\n');time.sleep(0.09)
	pilih_komen()

def pilih_komen():
	coy = raw_input('\033[0;97m{\033[0;93m?\033[0;97m} Pilih \033[0;91m>\033[0;93m ')
	if coy == "":
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi yg benar'
		pilih_komen()
	elif coy == "1":
		print "\033[0;97m Gunakan Tanda \033[0;97m'\033[0;93m,\033[0;97m'(\033[0;93mkoma\033[0;97m)\033[0;97m Untuk Komen Berbeda! "
		komentar = raw_input('\033[0;97m{\033[0;93m?\033[0;97m} Komentar \033[0;91m>\033[0;93m ')
		kok = komentar
		rando = kok.split(",")
	elif coy == "2":
		rando = ["Cinta adalah pengorbanan, tapi kalau pengorbanan mulu sih namanya penderitaan.",
		"Bekerjalah seperti tuyul. Nggak kelihatan, nggak perlu pujian, nggak cari perhatian, tapi hasil jelas.",
		"Jika doamu belum terkabul maka bersabar, ingatlah bahwa yang berdoa bukan cuma kamu!",
		"Tertawa bisa jadi obat terbaik. Tapi kalau kamu tertawa tanpa alasan yang jelas, mungkin kamu butuh obat.",
		"Ironi dalam hidup Manusia menciptakan ponsel, ponsel makin pintar Manusia tidak.",
		"Persahabatan itu ibarat kita ngompol di celana, setiap orang dapat melihatnya, tapi hanya Anda yang bisa merasakan kehangatannya.",
		"Ikan bandeng makan kawat orang ganteng numpang lewat",
		"Maksud hati cuma KENTUT, apa daya ampasnya malah NGIKUT"]
	elif coy == "3":
		rando = ["Tidak ada seorang pun yang bisa kembali ke masa lalu dan memulai awal yang baru lagi. Tapi semua orang bisa memulai hari ini dan membuat akhir yang baru.” - Maria Robinson",
		"Tidak ada yang bisa membuatmu merasa rendah diri tanpa seizinmu. - Eleanor Roosevelt",
		"Jangan pernah menyesali sehari dalam hidupmu. Hari-hari baik memberimu kebahagiaan dan hari-hari buruk memberimu pengalaman.",
		"Jangan takut berjalan lambat, takutlah jika hanya berdiri diam.",
		"Waktumu terbatas, jangan habiskan untuk hidup orang lain.” -Steve Jobs",
		"Kesuksesan dan kegagalan sama-sama bagian dari hidup. Keduanya sama-sama sementara.” - Shahrukh Khan",
		"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin.",
		"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu.",
		"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita.",
		"Semakin keras kamu bekerja untuk sesuatu, semakin besar perasaanmu saat mencapainya."]
	elif coy == "6":
		rando = ["Tidak ada seorang pun yang bisa kembali ke masa lalu dan memulai awal yang baru lagi. Tapi semua orang bisa memulai hari ini dan membuat akhir yang baru.” - Maria Robinson",
		"Tidak ada yang bisa membuatmu merasa rendah diri tanpa seizinmu. - Eleanor Roosevelt",
		"Jangan pernah menyesali sehari dalam hidupmu. Hari-hari baik memberimu kebahagiaan dan hari-hari buruk memberimu pengalaman.",
		"Bacot doang gede berani nya di sosmed giliran di ajak temuan diem nyali modal di sosmed dek wkwk malu dek di suruh pribadi gk berani wkwk ",
		"Main tebak-tebakan yok, Ayam apa yang tidak di sukai orang tua...?", "Main tebak-tebakan yok, Huruf depan nya K belakang nya L, Terdiri dari enam huruf, bentuk nya panjang dan lonjong, apaan hayo...?",
		"Bekerjalah seperti tuyul. Nggak kelihatan, nggak perlu pujian, nggak cari perhatian, tapi hasil jelas.",
		"Jika doamu belum terkabul maka bersabar, ingatlah bahwa yang berdoa bukan cuma kamu!",
		"Tertawa bisa jadi obat terbaik. Tapi kalau kamu tertawa tanpa alasan yang jelas, mungkin kamu butuh obat.",
		"Ironi dalam hidup Manusia menciptakan ponsel, ponsel makin pintar Manusia tidak.",
		"Persahabatan itu ibarat kita ngompol di celana, setiap orang dapat melihatnya, tapi hanya Anda yang bisa merasakan kehangatannya.",
		"Ikan bandeng makan kawat orang ganteng numpang lewat",
		"Main tebak-tebakan yok, Cuaca sedang mendung. Ada 5 orang tapi hanya ada 1 payung, Bagaimana caranya agar mereka tidal kehujanan...?",
		"Waktumu terbatas, jangan habiskan untuk hidup orang lain.” -Steve Jobs",
		"Kesuksesan dan kegagalan sama-sama bagian dari hidup. Keduanya sama-sama sementara.” - Shahrukh Khan",
		"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin.",
		"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu.",
		"Sadar anjing sadar gk usah sok pro lu jadi orang alay banget dih jijik gw", "Ternyata di sini banyak anak-anak alay ya jadi jijik gw dsni kayak yg mosting alay bat dah",
		"Semakin keras kamu bekerja untuk sesuatu, semakin besar perasaanmu saat mencapainya.",]
	elif coy == "4":
		rando = ["Ini Kisaran Lek Klean Mau Make Kata lu, gue, lu, gue Klean pindah aja ke jakarta ya ajg risih kali aku dengar nya",
		"Yang Posting kek ajg alay lu bangsat postingan macam tae kau malu-malu in aja lu mending nyusu sana ama emak lu wkwkwk",
		"Maaf aku gk suka karna hati mu kayak babi ngepet", "Gk usah berjuang anjing nyesel lu berjuang tapi hati dia milik orang lain inget kata tukang parkir maju mundur cantik",
		"Anak facebook jaman sekarang pada alay semua kayak yg mosting sumpah alay banget cuih jijik gw liat nya", "Kenapa sih disini banyak anak alay",
		"Sadar anjing sadar gk usah sok pro lu jadi orang alay banget dih jijik gw", "Ternyata di sini banyak anak-anak alay ya jadi jijik gw dsni kayak yg mosting alay bat dah",
		"Bacot doang gede berani nya di sosmed giliran di ajak temuan diem nyali modal di sosmed dek wkwk malu dek di suruh pribadi gk berani wkwk ",
		"Bales chat gw anjing gk usah di read chat gw babi berani nya di sosmed lu k*nt*l di suruh pribadi kayak ajg bales chat gw anjing babi woy",]
	elif coy == "5":
		rando = ["Main tebak-tebakan yok, Ada 1 orang sedang ketakutan. Di kawanin kok semakin tambah takut apa hayo...?",
		"Main tebak-tebakan yok, Cuaca sedang mendung. Ada 5 orang tapi hanya ada 1 payung, Bagaimana caranya agar mereka tidal kehujanan...?",
		"Main tebak-tebakan yok, Es apa yang suka di naiki orang...?", "Main tebak-tebakan yok, Orang apa yang bisa terbang...?"
		"Main tebak-tebakan yok, Ayam apa yang tidak di sukai orang tua...?", "Main tebak-tebakan yok, Huruf depan nya K belakang nya L, Terdiri dari enam huruf, bentuk nya panjang dan lonjong, apaan hayo...?",
		"Main tebak-tebakan yok, Ayam jantan, Kepala nya di prancis, Sayap nya di brazil, Kaki nya di Italia, Telur nya di mana ajg bingung gw...?"
		"Main tebak-tebakan yok, Apa sebesar gajah tapi gk ada berat nya sama sekali...?", "Main tebak-tebakan yok, 1 ekor ayam punya 2 kaki, Ayam 2 kaki ada berapa ekor...?",
		"Main tebak-tebakan yok, Mobil tabrakan di jalan tol, yang turun dluan apa nya...?", "Main tebak-tebakan yok, Di luar neraka di dalam surga buah apakah itu...?",]
	elif coy == "0":
		menu()
	else:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi yg benar'
		pilih_komen()
	
	tol = raw_input('\033[0;97m{\033[0;93m?\033[0;97m} Unlimited Komentar \033[0;92mY\033[0;97m/\033[0;93mN \033[0;91m>\033[0;97m ')
	if tol == "":
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi yg benar'
		pilih_komen()
	elif tol == "Y" or tol == "y":
		jumlah = int("1000")
	elif tol == "N" or tol == "n":
		while True:
			try:
				jumlah = int(raw_input('\033[0;97m{\033[0;93m?\033[0;97m} Jumlah Komentar \033[0;91m>\033[0;93m '))
				break
			except ValueError:
				print '\033[0;97m{\033[0;91m!\033[0;97m} Isi Yg Benar'
	else:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi Yg Benar'
		pilih_komen()
	try:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Minimal 40 Detik'
		delay = int(raw_input('\033[0;97m{\033[0;93m?\033[0;97m} Lambat Komentar \033[0;91m>\033[0;93m '))
		if 40 > delay:
			print '\033[0;97m{\033[0;91m!\033[0;97m} Delay Minimal 40 Detik'
			exit()
		
	except ValueError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Isi Yg Benar'
		pilih_komen()
		
	try:
		url = 'https://mbasic.facebook.com'
		toket = open('login.txt','r').read()
		cookie = open('coki.log','r').read().strip()
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'cookie' : cookie}
		cookies = {'Cookie': cookie}
	except KeyError:
		print '\033[0;97m{\033[0;91m!\033[0;97m} Cookie Invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		exit()
		
	class Run(Thread):
		print "\033[1;91m───────────────────────────────────────────────────── "
		jalan ("\033[0;93m      Sedang dalam proses mohon untuk bersabar")
		jalan ("\033[0;93m      Untuk menghentikan proses\033[0;91m,\033[0;93mTekan CTRL+z")
		print "\033[1;91m───────────────────────────────────────────────────── "
		def run(self):
			for ju in range(jumlah):
				time.sleep(delay)
				ju = ju + 1
				while True:
					try:
						ling = requests.get(url + '/home.php', headers=headers, cookies=cookies).text
						#cari_id = re.search('groups(.*?)/permalink/(.*?)/', ling)
						cari_id = re.search('fbid=(.*?)&amp;id=(.*?)&amp;', ling)
						id_post = cari_id.group(1)
						nama = cari_id.group(2)
						#bung = requests.get(url+'/'+id_post, headers=headers, cookies=cookies).text
						tag_nama = nama.replace(nama, '@['+nama+':]')
						break
					except requests.exceptions.ConnectionError:
						rap = random.choice(['\033[0;96m','\033[0;93m','\033[0;95m','\033[0;91m','\033[0;92m'])
						print "\r%s\033[0;97m{\033[0;91m!\033[0;97m} Sedang Menunggu Koneksi..."%(rap),;sys.stdout.flush();time.sleep(1)
						pass
					except:
						pass
				try:
					web = datetime.datetime.now()
					waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
					hour = web.hour
					if 03 < hour < 06:
					  boy = "Selamat Dini Hari 💜"
					elif 06 <= hour < 11:
					  boy = "Selamat Pagi 💙"
					elif 11 <= hour < 15:
					  boy = "Selamat Siang 💛"
					elif 15 <= hour < 18:
					  boy = "Selamat Sore 💚"
					else:
					  boy = "Selamat Malam 🖤"
					pantun = random.choice(rando)
					pesan = boy+'\n'+tag_nama+'\n'+pantun+'\n'+waktu
					req = requests.post("https://graph.facebook.com/"+(id_post)+"/comments?message="+pesan+"&access_token="+toket)
					bib = json.loads(req.text)
					if 'id' in bib:
						jalan ('\n\033[0;97m{\033[0;92m√\033[0;97m} [\033[0;93m'+str(ju)+'\033[0;97m]\033[0;92m Berhasil')
						jalan ('\033[0;97m{\033[0;93m•\033[0;97m} Link Post \033[0;91m>\033[0;96m www.facebook.com/'+id_post)
						jalan ('\033[0;97m{\033[0;93m•\033[0;97m} Komentar  \033[0;91m>\033[0;93m '+pantun[:15]+'...')
					elif 'error' in bib:
						jalan ('\n\033[0;97m{\033[0;91m×\033[0;97m} [\033[0;93m'+str(ju)+'\033[0;97m]\033[0;91m Gagal')
						jalan ('\033[0;97m{\033[0;93m•\033[0;97m} Link Post \033[0;91m>\033[0;96m www.facebook.com/'+id_post)
						jalan ('\033[0;97m{\033[0;93m•\033[0;97m} Komentar  \033[0;91m>\033[0;93m '+pantun[:15]+'...')
				except:
					pass
					
	th = Run()
	th.start()
	th.join()
	raw_input('\n\033[0;91m [\033[0;97m Tekan Enter Untuk Kembali\033[0;91m ]')
	bot_komen()
		
if __name__ == '__main__':
	menu()
	login()

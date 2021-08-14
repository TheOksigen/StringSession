import asyncio   
import os
import sys
import time
import random
import subprocess

try:
   from telethon import TelegramClient, events, version
   from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
   from telethon.network import ConnectionTcpAbridged
   from telethon.utils import get_display_name
   from telethon.sessions import StringSession
except:
   subprocess.check_call([sys.executable, "-m", "pip", "install", 'telethon'])   
finally:
   from telethon import TelegramClient, events, version
   from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
   from telethon.network import ConnectionTcpAbridged
   from telethon.utils import get_display_name
   from telethon.sessions import StringSession

try:
   import requests
   import bs4
except:
   print("[!] Requests Yüklənir...")
   print("[!] Bs4 Yüklənir...")

   subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
   subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
   import requests
   import bs4

os.system("clear")
def hata (text):
   print("\u001b[31m" + text + "\u001b[0m")
def bilgi (text):
   print("\u001b[34m" + text + "\u001b[0m")
def onemli (text):
   print("\u001b[36;1m" + text + "\u001b[0m\u001b[0m")
def soru (soru):
   return input("\u001b[33m" + soru + "\u001b[0m")

loop = asyncio.get_event_loop()

class InteractiveTelegramClient(TelegramClient):
    # Original Source https://github.com/LonamiWebs/Telethon/master/telethon_examples/interactive_telegram_client.py

    def __init__(self, session_user_id, api_id, api_hash,
                 telefon=None, proxy=None):
        super().__init__(
            session_user_id, api_id, api_hash,
            connection=ConnectionTcpAbridged,
            proxy=proxy
        )
        self.found_media = {}
        bilgi('[i] Telegram serverlərinə bağlanır...')
        try:
            loop.run_until_complete(self.connect())
        except IOError:
            hata('[!] Bağlanarkən xəta baş verdi. Yenidən yoxlanılır...')
            loop.run_until_complete(self.connect())

        if not loop.run_until_complete(self.is_user_authorized()):
            if telefon == None:
               user_phone = soru('[?] Telefon nömrəniz (Nümunə: +994xxxxxxxxx): ')
            else:
               user_phone = telefon
            try:
                loop.run_until_complete(self.sign_in(user_phone))
                self_user = None
            except PhoneNumberInvalidError:
                hata("[!] Səhv telefon nömrənsi! Nömrənizi nümunədə göstərilən şəkildə yazın. Nümunə: +994xxxxxxxxx")
                exit(1)
            except ValueError:
               hata("[!] Səhv telefon nömrənsi! Nömrənizi nümunədə göstərilən şəkildə yazın. Nümunə: +994xxxxxxxxx")
               exit(1)

            while self_user is None:
               code = soru('[?] Telegramdan gələn 5 xanalı kodu yazın: ')
               try:
                  self_user =\
                     loop.run_until_complete(self.sign_in(code=code))
               except PhoneCodeInvalidError:
                  hata("[!] Kodu səhv yazdınız . Yenidən yoxlayın. [Həddindən artıq cəhd etmək ban ilə səbəblənər.]")
               except SessionPasswordNeededError:
                  bilgi("[i] İki addımlı doğrulama tapıldı.")
                  pw = soru('[?] Şifrənizi yazın: ')
                  try:
                     self_user =\
                        loop.run_until_complete(self.sign_in(password=pw))
                  except PasswordHashInvalidError:
                     hata("[!] 2 addımlı doğrulama şifrəsini yalnış yazdız. Xahiş olunur yenidən yoxlayın. [Həddindən artıq yoxlasaz ban ala bilərsiz]")


if __name__ == '__main__':
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   bilgi("N Σ O N String alıcı\nTelegram: N Σ O N\nPython: " + surum + "\nTeleThon: " + version.__version__ + "\nBs4/Requests: ✅\n")
   onemli("[1] Yeni üsul")
   onemli("[2] Köhnə üsul\n")
   
   try:
      secim = int(soru("[?] Seçim edin [1/2]: "))
   except:
      hata("\n[!] Xahiş olunur [1 ya da 2] yazın!")
      exit(1)

   if secim == 2:
      API_ID = soru('[?] API ID\'iniz [Hazır açar\'ları istifadə etmək üçün boş buraxın]: ')
      if API_ID == "":
         bilgi("[i] Hazır açarlar hazırlanır...")
         API_ID = 6
         API_HASH = "eb0"
      else:
         API_HASH = soru('[?] API HASH\'iniz: ')

      client = InteractiveTelegramClient(StringSession(), API_ID, API_HASH)
      bilgi("[i] String Keyiniz aşağıdakıdır!\n\n\n" + client.session.save())
   elif secim == 1:
      numara = soru("[?] Telefon nömrəniz: ")
      try:
         rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
      except:
         hata("[!] Kod göndərilə bilmədi. Telefon nömrənizin düz olduğuna əmin olun.")
         exit(1)
      
      sifre = soru("[?] Telegram'dan gələn kodu yazın: ")
      try:
         cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
      except:
         hata("[!] Böyük ehtimal kodu səhv yazdınız. Yenidən yoxlayın")
         exit(1)
      app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
      soup = bs4.BeautifulSoup(app, features="html.parser")

      if soup.title.string == "Create new application":
         bilgi("[i] Tətbiq yoxdur. yaradılır...")
         hashh = soup.find("input", {"name": "hash"}).get("value")
         AppInfo = {
            "hash": hashh,
            "app_title":"NeonUserBot",
            "app_shortname": "Neon",
            "app_url": "",
            "app_platform": "android",
            "app_desc": ""
         }
         app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
         bilgi("[i] Tətbiq uğurla yaradıldı!")
         bilgi("[i] API ID/HASH alınır...")
         newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
         newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

         g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         bilgi("[i] Məlumatlar gətirildi! Xahiş olunur bunları yadda saxlayın.\n")
         onemli(f"[i] API ID: {app_id}")
         onemli(f"[i] API HASH: {api_hash}\n\n")
         bilgi("[i] String alınır...")
         client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
         print("[i] String Keyiniz aşağıdadır. String kodunuzu güvənilir adamlar ilə paylaşın. Əks halda hesabınızı ələ keçirə bilərlər!\n\n\n" + client.session.save())

      elif  soup.title.string == "App configuration":
         bilgi("[i] Hal-hazırda tətbiq yaratmısız. API ID/HASH alınır...")
         g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         bilgi("[i] Məlumatlar gətirildi!\n")
         onemli(f"[i] API ID: {app_id}")
         onemli(f"[i] API HASH: {api_hash}\n\n")
         bilgi("[i] String hazırlanır...")

         client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
         print("[i] String Keyiniz aşağıdadır. String kodunuzu güvənilir adamlar ilə paylaşın. Əks halda hesabınızı ələ keçirə bilərlər!\n\n\n" + client.session.save())
      else:
         hata("[!] Bir xəta baş verdi!")
         exit(1)
   else:
      hata("[!] Bilinməyən bir seçim etdiniz.")
      exit(1)

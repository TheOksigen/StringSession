MESAJ="N Σ O N String Alıcı"
MESAJ+="\nTelegram: @NEONUserBot"
pkg upgrade
clear
echo -e $MESAJ
echo "Python yüklenir"
pkg install python -y
clear
echo -e $MESAJ
echo "Telethon yüklenilir..."
pip install telethon
echo "Requests/BS4 yüklenilir..."
pip install requests
pip install bs4
clear
echo -e $MESAJ
echo "Fayl yazılır..."
curl "https://raw.githubusercontent.com/TheOksigen/neon_userbot/master/string.py" --output "string.py"
clear
echo -e $MESAJ
echo "Qurulum hazırdır, İndi StringSessionu ala bilersiz"
clear
python string.py

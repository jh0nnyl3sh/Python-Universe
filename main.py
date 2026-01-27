import pywhatkit

# Telefon no, Mesaj, Saat, Dakika
# Örn: Yarın sabah 07:30'da mesaj at
pywhatkit.sendwhatmsg("+905554443322",
                      "Bu mesajı Python gönderiyor, "
                      "ben hala uyuyorum! 😴",
                      22, 20)

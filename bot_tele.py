import re
import telebot

TOKEN = "TOKEN"

USER_ID_TUJUAN = UID

bot = telebot.TeleBot(TOKEN)

def ekstrak_ip(teks: str):
    match = re.search(
        r"IP Penyerang:\s*\[?(\d{1,3}(?:\.\d{1,3}){3})\]?",
        teks
    )
    return match.group(1) if match else None


@bot.message_handler(func=lambda message: True)
def handle_pesan_masuk(message):

    teks_pesan = message.text or ""

    if "WAZUH SECURITY ALERT" in teks_pesan:

        ip_penyerang = ekstrak_ip(teks_pesan)

        if ip_penyerang:
            print(f"[TERDETEKSI] IP Penyerang: {ip_penyerang}")

            bot.send_message(
                USER_ID_TUJUAN,
                f"IP penyerang terdeteksi: {ip_penyerang}"
            )

        else:
            print("Format alert ditemukan, tetapi IP tidak berhasil diekstrak.")


print("Bot sedang berjalan...")
bot.infinity_polling()
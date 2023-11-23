from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Status Bot dan Bot Lainnya ✨", url="https://t.me/ab1ngstore")],
        [
            InlineKeyboardButton("Cara Penggunaan ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Tentang 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Bot yang Lebih Menakjubkan ♥", url="https://t.me/ab1ngstore")],
    ]

    START = """
Hai {}

Selamat Datang di {}

Jika Anda tidak mempercayai bot ini,
1) berhenti membaca pesan ini
2) hapus obrolan ini

Masih membaca?
Anda dapat menggunakan saya untuk menghasilkan pyrogram (bahkan versi 2) dan sesi string telethon. Gunakan tombol di bawah ini untuk mempelajari lebih lanjut!

By @akuab1ng
    """

    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot
/help - Pesan ini
/start - Mulai Botnya
/generate - Hasilkan String
/cancel - Batalkan Proses String
/restart - Batalkan prosesnya
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @akuab1ng

Source Code : [Click Here](https://github.com/sayaAbing/StringSessionBot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @akuab1ng
    """

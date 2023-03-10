from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("π Mulai Membuat string π", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="πΏ Kembali Ke Awal πΏ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("π₯ Ini Grup ku  π₯", url="https://t.me/obrolansuar")],
        [
            InlineKeyboardButton("Cara Pakeknya β", callback_data="help"),
            InlineKeyboardButton("π Apa Masalah Kau π", callback_data="about")
        ],
        [InlineKeyboardButton("π€ Daftar Repo Bot π€", url="https://t.me/Karc0de")],
    ]

    START = """
π·π°π»πΎ {}
ππ΄π»π°πΌπ°π π³π°ππ°π½πΆ π³πΈ {}
πΊπ°π»πΎ πΊπ°π πΆπ°πΊ πΏπ΄ππ²π°ππ° ππ°πΌπ° π±πΎπ πΈπ½πΈ, 
1) πΆπ°πππ°π· π±π°π²π° πΏπ΄ππ°π½ πΈπ½πΈ πΊπΎπ½ππΎπ»
2) π±π»πΎπΊπΈπ π±πΎπ π°ππ°π π³π΄π»π°ππ΄ π²π·π°π πΌπ΄πΌπ΄πΊ
Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih

By @Karc0de
    """

    HELP = """
β¨ **Available Commands** β¨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Source Code : [Click Here](https://github.com/ArmanGG01/karstring)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @PakkPoll
    """

import telebot
from gtts import gTTS

robot = telebot.TeleBot("6306328034:AAEr4XvsEeWRAMT-QyO1rQY6iRvCBzW5fWo")


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard.add("ارسال متن")


@robot.message_handler(commands=['start'])
def send_welcome(message):
    robot.send_message(message.chat.id, "سلام \n \n راهنمای ربات به صورت دستورات زیر است: \n \n /help \n /contact \n /about \n /ersale_matn")


@robot.message_handler(commands=['help'])
def help_me(message):
    robot.reply_to(message, "منو فعال شد", reply_markup= keyboard)


@robot.message_handler(commands=['contact'])
def contact_me(message):
    robot.reply_to(message, "شماره تلفن جهت تماس 09876543210")

@robot.message_handler(commands=['about'])
def about_me(message):
    robot.reply_to(message, "این ربات توسط داود با پایتون نوشته شده است.")


@robot.message_handler(func= lambda m: True)
def info(message):
    if message.text == "ارسال متن":
        global msg
        msg = robot.send_message(message.chat.id, "متن خود را تایپ نمایید: ")
        robot.register_next_step_handler(msg, print_message)
        robot.register_next_step_handler(msg, text_to_voice)


def print_message(message):
    global nm
    nm = message.text
    robot.send_message(message.chat.id, f"متن شما به صورت زیر است:\n \n \n \n \n \n {nm}")


def text_to_voice(message):
    seda = gTTS(message.text)
    seda.save('text_voice.mp3')
    robot.send_audio(message.chat.id, open("F:/python/project-py-bot/text_voice.mp3", 'rb'))


robot.infinity_polling()
import telebot
from telebot import types


TOKEN = ''

bot = telebot.TeleBot(TOKEN, parse_mode=None)

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Yes", callback_data="cb_yes"), types.InlineKeyboardButton("No", callback_data="cb_no"))
    return markup
# bot.send_message(5456208707, 'qqq')
def Send_message(id, answer, q):
    bot.send_message(id, f"Ваш вопрос: {q}\n\nОтвет: {answer}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отправлено.")
        with open("report.txt", "a", encoding="utf-8") as file:
            file.write(f"{call.message.chat.id}||{call.message.chat.first_name}||{call.message.reply_to_message.text}\n")
    elif call.data == "cb_no":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Напишите свой вопрос.")

@bot.message_handler(commands=["start"])
def Hello(message):
    bot.send_message(message.chat.id, text=f'Привет {message.from_user.first_name}')
    bot.send_message(message.chat.id, text=f'Напишите свой вопрос.')


@bot.message_handler(content_types=['text'])
def test(message):
    bot.reply_to(message, text=f'Отпавить ?', reply_markup=gen_markup())


bot.infinity_polling()


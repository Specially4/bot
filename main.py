import telebot
from telebot import types
from datetime import datetime

from markup import create_reply_markup, create_line_markup
from constants import TOKEN
from container import order_service


bot = telebot.TeleBot(TOKEN)  # Create bot

user = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Нажмите:\n'
                                      'Заказ - Для того чтоб заказать работу у автора.\n'
                                      'Портфолио - Для того чтоб увидеть портфолио автора.',
                     reply_markup=create_reply_markup())


@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text.strip() == 'Заказ':
        bot.send_message(message.chat.id, 'Опишите ваш заказ, что хотите получить в какой стилистике?')
        bot.register_next_step_handler(message, reg_order)
    elif message.text.strip() == 'Портфолио':
        answer = 'None'  # Нужно добавить ответ на запрос портфолио. А именно отправить ссылку либо загрузить их.
        bot.send_message(message.chat.id, answer)


# @bot.message_handler(content_types=['document'])
# def handle_docs_photo(message):
#     global order
#     try:
#         chat_id = message.chat.id
#
#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#
#         path = 'D:/Project/bot/' + message.document.file_name
#         order['path'] = path
#         with open(path, 'wb') as new_file:
#             new_file.write(downloaded_file)
#
#         bot.reply_to(message, "Пожалуй, я сохраню это")
#     except Exception as e:
#         bot.reply_to(message, e)

def reg_order(message):
    order_data = {
        'username': '@' + message.from_user.username,
        'chat_id': message.chat.id,
        'description': message.text,
        'create_on': datetime.now()
    }
    order_service.create_order(order_data)

    bot.send_message(message.chat.id, f"Спасибо {message.from_user.first_name}.\nЗаписал ваш заказ."
                                      f"Желаете добавить файл или ссылку?", reply_markup=create_line_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query_handlers(call):
    if call.data == 'url':
        bot.send_message(call.message.chat.id, 'Отправьте пожалуйста ссылку, а я ее сохраню.')
        # bot.register_next_step_handler(call, req_url)
    if call.data == 'path':
        bot.send_message(call.message.chat.id, 'Отправьте пожалуйста документ, а я его сохраню.')
        # bot.register_next_step_handler(call, req_url)


# def req_url(call):
#     data = {
#         'chat_id': call.message.chat.id,
#         call.data: call.message.text
#     }
#     order_service.update_order(data)
#     bot.send_message(call.message.chat.id, "Всё сохранил!")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

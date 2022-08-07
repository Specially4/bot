from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup


def create_reply_markup() -> ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    order_markup = types.KeyboardButton('Заказ')
    portfolio_markup = types.KeyboardButton('Портфолио')
    markup.add(order_markup)
    markup.add(portfolio_markup)

    return markup


def create_line_markup() -> InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    key_url = types.InlineKeyboardButton(text="Ссылка на документ", callback_data='url')
    key_document = types.InlineKeyboardButton(text="Документ", callback_data='path')
    markup.add(key_url)
    markup.add(key_document)

    return markup

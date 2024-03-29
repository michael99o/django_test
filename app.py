import telebot
from config import keys, TOKEN
from extensions import ApiException, CurrencyConvertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Добро пожаловать в валютный бот!\n' \
           'Чтобы воспользоваться ботом введите команду в формате:\n <имя валюты, цену которой вы хотите узнать>\
<имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>\n\
Чтобы узнать информация о всех доступных валютах введите команду /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Вам доступны следующие валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types='text')
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise ApiException('Неверное количество параметров')

        quote, base, amount = values
        total_base = CurrencyConvertor.get_price(quote, base, amount)
    except ApiException as a:
        bot.reply_to(message, f'Ошибка пользователя.\n{a}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
import telebot
from pycoingecko import CoinGeckoAPI


bot = telebot.TeleBot("APNAR FALTU BOT AR TOKEN AI KHANE DAN", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['p'])
def price(message):
    crypto_id_from_user = message.text.split()[1]
    print(crypto_id_from_user)
    try:
        cg = CoinGeckoAPI()
        crypto_data = cg.get_coin_ticker_by_id(crypto_id_from_user)
        name = crypto_data.get('name')
        ticker = crypto_data.get('tickers')[0].get('base')
        price = crypto_data.get('tickers')[0].get('last')
        eth_price = crypto_data.get('tickers')[1].get('converted_last').get('eth')
        usd_volume_24h = crypto_data.get('tickers')[0].get('converted_volume').get('usd')

        bot.reply_to(message, f'{name} || {ticker}\n\n'
                              f'USD: {price}\n'
                              f'ETH: {eth_price}\n'
                              f'Volume(24H): ${usd_volume_24h}')
        print(f'{name} || {ticker}\n\n'
              f'USD: {price}\n'
              f'ETH: {eth_price}\n'
              f'Volume(24H): ${usd_volume_24h}')
    except ValueError:
        print('Invalid Crypto Name')
        bot.reply_to(message, "Coudn't Find What you Asked For")

bot.polling()
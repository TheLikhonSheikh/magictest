from telethon import events, TelegramClient

from pycoingecko import CoinGeckoAPI



API_ID = 6379227

API_HASH = '9b136a4a699c6b6f08c010ba0d238fc5'

BOT_TOKEN = '1970904086:AAGBQ8BgjbSILgg2CA0HEiAPB_O_TG6anCE'



bot = TelegramClient("HCM-PRICE-BOT", API_ID, API_HASH).start(bot_token=BOT_TOKEN)





@bot.on(events.NewMessage(pattern=r"/p"))

async def price(event):

    crypto_id_from_user = "bitcoin"

    try:

        cg = CoinGeckoAPI()

        crypto_data = cg.get_coin_ticker_by_id(crypto_id_from_user)

        name = crypto_data.get('name')

        ticker = crypto_data.get('tickers')[0].get('base')

        price = crypto_data.get('tickers')[0].get('last')

        eth_price = crypto_data.get('tickers')[1].get('converted_last').get('eth')

        usd_volume_24h = crypto_data.get('tickers')[0].get('converted_volume').get('usd')



        await event.reply(f'{name} || {ticker}\n\n'

                              f'USD: {price}\n'

                              f'ETH: {eth_price}\n'

                              f'Volume(24H): ${usd_volume_24h}')

        print(f'{name} || {ticker}\n\n'

              f'USD: {price}\n'

              f'ETH: {eth_price}\n'

              f'Volume(24H): ${usd_volume_24h}')

    except ValueError:

        print('Invalid Crypto Name')

        await event.reply("Coudn't Find What you Asked For")



bot.run_until_disconnected()

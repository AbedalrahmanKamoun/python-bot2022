from telegram.ext import *
import requests
import os

print('Starting Boot...')

TOKEN = '5013549755:AAFmwuoti0k1BkoaWgnFx07xJLm64yeZj4E'
group_chat_id = '-665561748'
PORT = int(os.environ.get('PORT', 80))

def start_command(update, context):
    update.message.reply_text('Send us a message, we will be replying in no time.')

def send_message(update, context):
    if(f'{update.message.chat.type}' == 'private'):
        msg = f'{update.message.from_user.first_name}, {update.message.chat.id}, Text Message: "{update.message.text}"'
        url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage' + '?chat_id=' + group_chat_id + '&text=' + msg
        requests.get(url)
        update.message.reply_text('Your message was recieved. We will be contacting you soon... Thank you!')
    elif(f'{update.message.chat.type}' == 'group'):
        msg = f'Dear {update.message.reply_to_message.text.split(",")[0]}, {update.message.text}'
        url = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage' + '?chat_id=' + f'{update.message.reply_to_message.text.split(",")[1][1:]}' + '&text=' + msg
        requests.get(url)

def main():
    updater = Updater(TOKEN, use_context = True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("start", start_command))
    disp.add_handler(MessageHandler(Filters.text, send_message))

    updater.start_webhook(
        listen = '0.0.0.0',
        port = int(PORT),
        url_path = TOKEN,
        webhook_url = 'https://telegram-bot2022.herokuapp.com/' + TOKEN
    )
    updater.idle()
    
if __name__ == '__main__':
    main()

import time
from discord import Webhook, RequestsWebhookAdapter
url = "https://discordapp.com/api/webhooks/908007946145894400/tWV3jlRjESxknpuXTHoeKjCb8ToBWQCpY6y1gE9Y_mmF7hKGVznLEsrkzfa-hQZDc66C" 
webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

def logit(message):
    webhook.send(message)
    with open('/home/pi/Desktop/AFKZenCoders/PS12/Logs.txt', 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()
        
import time
from discord import Webhook, RequestsWebhookAdapter
url = "https://discord.com/api/webhooks/898895725046427718/ccEL0VVOzKkd6Fz6Z0SSI3xRbGPZyHkR1pYBHa_tFA-DIWje0LjyfZMFCJk3MOBUf2Sh" 
webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

def logit(message):
    webhook.send(message)
    with open('/home/pi/Desktop/AFKZenCoders/PS12/Logs.txt', 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()
        
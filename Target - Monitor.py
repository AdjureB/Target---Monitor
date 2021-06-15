import requests
import dhooks
import json
import time
from dhooks import Embed, Webhook

bruhid = input('What do you want to monitor(pid): ')



availability = False

def monitor():
  url = "https://redsky.target.com/redsky_aggregations/v1/web/pdp_fulfillment_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&tcin=" + str(bruhid) + "&store_id=3267&store_positions_store_id=3267&has_store_positions_store_id=true&zip=94710&state=CA&latitude=37.870&longitude=-122.290&scheduled_delivery_store_id=1926&pricing_store_id=3267"
  payload={}
  headers = {
    'authority': 'redsky.target.com',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'accept': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'origin': 'https://www.target.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.target.com/p/bbb/-/A-' + str(bruhid),
    'accept-language': 'en-US,en;q=0.9',
    'Cookie': 'TealeafAkaSid=IcETvzDQOsOQ43ZWAUJ5cNKaABdWp5kR'
}


  burl = 'https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&tcin=' + str(bruhid) + '&member_id=20044512175&store_id=3267&has_store_id=true&pricing_store_id=3267&scheduled_delivery_store_id=1926&has_scheduled_delivery_store_id=true&has_financing_options=false'

  bpayload={}
  bheaders = {
    'authority': 'redsky.target.com',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'accept': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'origin': 'https://www.target.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.target.com/p/bbb/-/A-' + str(bruhid),
    'accept-language': 'en-US,en;q=0.9',
    'Cookie': 'TealeafAkaSid=IcETvzDQOsOQ43ZWAUJ5cNKaABdWp5kR'
  }

  response = requests.request("GET", url, headers=headers, data=payload).json()
  metadata_response = requests.request("GET", burl, headers=bheaders, data=bpayload).json()

  stocknum = response['data']['product']['fulfillment']['shipping_options']['available_to_promise_quantity']
  print(stocknum)

  prodid = response['data']['product']['fulfillment']['product_id']

  price = metadata_response['data']['product']['price']['formatted_current_price']

  url = metadata_response['data']['product']['item']['enrichment']['buy_url']

  image2 = metadata_response['data']['product']['item']['enrichment']['images']['content_labels'][0]['image_url']

  title = metadata_response['data']['product']['item']['product_description']['title']

#Discord Embed
  hook = Webhook('https://discord.com/api/webhooks/771466332637757440/dcn9IM8PcbK_TN-1nltDRiutEBeNGtLAd8Nk1vg6TrvjOkLGnudb2xEKKQ5hvSPs8MZX')
  hook1 = Webhook('https://discord.com/api/webhooks/812983678623416320/ZVJjTJoK8ZdKAbxLXDD67dXy4gEUixJhw9PCgsPF7siJTCFXrTe6HmvupOWObVuai3Kx')
#bbburl = 

  embed = Embed(description=str(url),
      color=0xFFFDD0,
      timestamp='now')
  image1 = 'https://cdn.discordapp.com/avatars/475038392262983680/a_4d79846ef589aa99773e2f4e51633249.gif?size=2048'

  embed.set_author(name=str(title),url=str(url))
  embed.add_field(name='PID', value=str(prodid))
  embed.set_thumbnail(image2)
  embed.add_field(name='Price', value=str(price))
  embed.add_field(name='Stock', value=str(stocknum))
  embed.set_footer(text='bbb monitors - Target', icon_url=image1)


#Function
  time.sleep(0.5)
  if stocknum > 0.0:
    print("In stock!")
    #hook.send(embed=embed)
    #hook1.send(embed=embed)
    time.sleep(10)
    monitor()
  else:
    monitor()

monitor()

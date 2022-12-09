import requests
import random
#-------------Api call for amazon -------------------|
urlamz = "https://amazon24.p.rapidapi.com/api/todaydeals"

headers = {
	"X-RapidAPI-Key": "f35142ac0emshdb77d77b6e2a12dp1419fcjsncf9fc6296c95",
	"X-RapidAPI-Host": "amazon24.p.rapidapi.com"
}

responseamz = requests.request("GET", urlamz, headers=headers)

tempamz = responseamz.json()
dataamz = tempamz.get("deal_docs")

#----------Ebay API----------------------------------|
urlebay = "https://ebay-data-scraper.p.rapidapi.com/deals/home"

headers = {
	"X-RapidAPI-Key": "f35142ac0emshdb77d77b6e2a12dp1419fcjsncf9fc6296c95",
	"X-RapidAPI-Host": "ebay-data-scraper.p.rapidapi.com"
}

responseebay = requests.request("GET", urlebay, headers=headers)

dataebay = responseebay.json()

def merge(dataamz, dataebay):
    new_data = []
    for item in dataamz:
        avg_price = (item['app_sale_range']['min'] + item['app_sale_range']['max'])/2
        new_data.append({'name':item['deal_title'],'link':item['deal_details_url'],'image':item['deal_main_image_url'],'price':avg_price})
    for item in dataebay:
        if 'product_name' in item and 'price' in item and 'link' in item and 'image' in item:
            new_data.append({'name':item['product_name'],'link':item['link'],'image':item['image'],'price':item['price']})
    return new_data

"counts for number of items"
def count(data):
    counter = 0 
    for x in data: 
        counter += 1 
    return counter
"return random selection from data group"
def randomselect(data): 
   return random.randint(0,count(data)-1)

def related_items(name, data):
    key_words = name.split()
    new_data = []
    for item in data:
        if name != item['name']:
            for key in key_words:
                if key in item['name']:
                    new_data.append(item)
                    break
    return new_data



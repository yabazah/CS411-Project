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


"counts for number of items"
def count(dataamz):
    counter = 0 
    for x in dataamz: 
        counter += 1 
    return counter
"return random selection from data group"
def randomselect(dataamz): 
   return random.randint(0,count(dataamz)-1)

print(dataebay[randomselect(dataebay)]['link'])

"print(data[1]['deal_title'])"



#!/usr/bin/env python3

# install requests module 
# sudo pip install requests
import requests
from bs4 import BeautifulSoup

# set URL to scrape
url = 'https://recruitingbypaycor.com/career/CareerHome.action?clientId=8a7883c66a3387ef016a5183d6f11208'

# use requests module get() method to call URL
r = requests.get(url)

# instansiate a BeautifulSoup object
## pass constructer request response and parsert type
soup = BeautifulSoup(r.content, 'html.parser')

# use soup object select method to select desired element
val = soup.select('[ns-qa="Application Security Engineer"]')

# handle response
print (val)
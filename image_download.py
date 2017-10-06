import random
import urllib.request

def image_downloder(url):
   name = random.randrange(1, 100)
   full_name = str(name)+".jpeg"
   urllib.request.urlretrieve(url, full_name)


image_downloder("https://www.google.co.in/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

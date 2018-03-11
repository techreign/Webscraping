import string
import os
import random
import bs4
from urllib import request

url = "http://reddit.com"
urlPage = request.urlopen(url).read()

soup = bs4.BeautifulSoup(urlPage, "html.parser")
img_list = []

for img in soup.find_all('img'):
	img_item = str(img.get('src')).split('//')
	img_list.append(img_item[1])

#print(img_list)
r = 8
all_chars = string.ascii_letters
# replace this folder_address variable to the directory which you wish to save
# the image files on your computer
folder_address = "C:\\Users\\User\\Documents\\Codes\\Python Scripts\\Reddit\\Pics\\"

for item in img_list:
	request.urlretrieve("http://" + item, 
		+ ''.join(random.choice(all_chars) for x in range(0, r)) + ".jpg")
	
print("finished downloading images")
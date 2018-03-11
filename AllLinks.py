import bs4
from urllib import request

url = "http://reddit.com"
urlPage = request.urlopen(url).read()

soup = bs4.BeautifulSoup(urlPage, "html.parser")
link_list = []

for links in soup.find_all('a'):
	link_item = links.get('href')
	if link_item is not None and link_item not in link_list and link_item.startswith('http'):
		link_list.append(link_item)
		print(link_item)


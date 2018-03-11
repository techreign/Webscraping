from urllib import request
import bs4

url = "http://liquipedia.net/overwatch/Overwatch_League/Season_1/Regular_Season"
sauce = request.urlopen(url).read()
soup = bs4.BeautifulSoup(sauce, "html.parser")

#f = open("overwatchleague.txt", "w+")

results = []
score = []

for tags in soup.find_all('span', attrs={"class": "team-template-text"}):
	results.append(tags.getText())

for tags in soup.find_all('b'):
	score.append(tags.getText())

print("Total Overwatch League Season Standings")
for i in range(0, 12):
	print(results[24 + i] + ' : ' + score[62 + i])


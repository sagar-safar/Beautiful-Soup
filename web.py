from bs4 import BeautifulSoup
import requests



webpage = requests.get('https://news.ycombinator.com/')
data = webpage.text
soup = BeautifulSoup(data, 'html.parser')
print(soup.title)
webLink = soup.select('.titlelink')
upVote = [int(upvote.getText().split()[0]) for upvote in soup.select('.score')]
print(upVote)
max_upvote = max(upVote)

index_ = upVote.index(max_upvote)
print(index_)
print(webLink[index_].getText())
print(webLink[index_].get('href'))

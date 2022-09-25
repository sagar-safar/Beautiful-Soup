from bs4 import BeautifulSoup
import requests
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text
soup = BeautifulSoup(data, 'html.parser')
movies_data = soup.findAll('h3')
movies = [element.getText() for element in movies_data]
n = len(movies)
with open('movies_list.txt', 'w', encoding='utf-8') as f:
    for i in range(n-1, -1, -1):
        f.write(movies[i])
        f.write('\n')



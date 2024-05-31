import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser") #parse the website thr soup
#
'''print(soup.prettify())'''
all_movies = soup.find_all(name="h3", class_="title")
print(all_movies)
movie_titles = [movie.getText() for movie in all_movies] #fetching all the texts
movies = movie_titles[::-1] 
#or can do the code below. it the same
for n in range(len(movie_titles),0,-1):
	print(moveie_titles[n-1])

with open("movies.txt", mode="w") as file: #creating a new file
    for movie in movies:
        file.write(f"{movietitles}\n")#some formatting so that each movie will get its own line

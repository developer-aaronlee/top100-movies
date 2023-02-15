from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.text)

empire_page = response.text
soup = BeautifulSoup(empire_page, "html.parser")

# movie_tags = soup.find_all(name="h3", class_="title")
# all_movies = []
# for x in movie_tags:
#     movie_name = x.getText("h3")
#     if "12:" in movie_name:
#         all_movies.append(movie_name[movie_name.index(":")+2:])
#     else:
#         all_movies.append(movie_name[movie_name.index(")")+2:])
#
# top_movies = all_movies[::-1]
# print(top_movies)
#
# with open("movies.txt", "w") as file:
#     for x in range(len(top_movies)):
#         movie_title = f"{x+1}) {top_movies[x]}\n"
#         file.write(movie_title)


all_movie = soup.find_all(name="h3", class_="title")
movie_titles = [x.getText("h3") for x in all_movie]

movies = movie_titles[::-1]
# movies = []
# for x in range(len(movie_titles)-1, -1, -1):
#     movies.append(movie_titles[x])

with open("movies.txt", "w") as file:
    for x in movies:
        file.write(f"{x}\n")




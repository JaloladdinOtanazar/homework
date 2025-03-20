import requests
import random

api_key = 'd886d73d1edc5413ed8917fcccb2de60'
base_url = 'https://api.themoviedb.org/3'
def get_genres():
    url = f"{base_url}/genre/movie/list?api_key={api_key}"
    res = requests.get(url)
    if res.status_code == 200:
        data =res.json()
        return {genre['id']: genre['name'] for genre in data['genres']}
    else:
        print(f"error accured while fetching(Status Code: {res.status_code})")
def get_movies(genre_id):
     url = f"{base_url}/discover/movie?api_key={api_key}&with_genres={genre_id}"
     res = requests.get(url)
     if res.status_code == 200:
         data  = res.json()
         return data['results']
     else:
         print(f"error while fetching movies: {res.status_code}")
         return []
def main():
    genres = get_genres()
    if not genres:
        return
    print("Available Genres")
    for genre_id, genre_name in genres.items():
        print(f'{genre_id}: {genre_name}')
    genre_choice = int(input("enter a number for a movie: "))
    try: 
        if genre_choice not in genres:
            print('invalid genre choice number')
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    movies = get_movies(genre_choice)
    if movies:
        random_movie = random.choice(movies)
        print(f""" 
        Title: {random_movie['title']}
        Overview: {random_movie['overview']}
        """)
    else:
        print("no movies found")
if __name__ == '__main__':
    main()
    

        



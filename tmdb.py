
import pandas as pd 
import json
from datetime import datetime
import os
print("Saving file at:", os.getcwd())

import requests


def run_tmdb_etl():

    # Your TMDB API key
    api_key = '699c439d55d094a10b8ba2b2dfe84758'

    # TMDB API endpoint (Popular Movies)
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"

    response = requests.get(url)
    data = response.json()
  
    

    movie_list = []

    # Loop through each movie in the results
    for movie in data["results"]:
        refined_movie = {
            "movie_id": movie["id"],
            "title": movie["title"],
            "popularity": movie["popularity"],
            "vote_average": movie["vote_average"],
            "vote_count": movie["vote_count"],
            "release_date": movie.get("release_date", None),
            "original_language": movie["original_language"],
            "overview": movie["overview"]
        }
        movie_list.append(refined_movie)

    # Convert to DataFrame
    df = pd.DataFrame(movie_list)

    # Save to CSV
    df.to_csv("D:/IMP Folder/LPU FOLDER/7th sem/Cluster Computing/updated.csv", index=False)
    print(df.head())



 

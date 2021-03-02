import random
from pprint import pprint

import httpx


async def fetch_movie(config, language):
    client = httpx.AsyncClient()
    year = random.randint(1990, 2021)
    query_params = {
        'api_key': config.TMDB_API_KEY,
        'language': 'en_US',
        'with_original_language': language,
        'include_adult': 'false',
        'primary_release_year': year
    }
    r = await client.get('https://api.themoviedb.org/3/discover/movie', params=query_params)
    pprint(r.json())

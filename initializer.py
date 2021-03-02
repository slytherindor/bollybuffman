import asyncio

from config import load_dot_env_file, load_env_vars_to_config
from fetch_movie import fetch_movie

load_dot_env_file()
config = load_env_vars_to_config()
asyncio.run(fetch_movie(config, 'hi'))
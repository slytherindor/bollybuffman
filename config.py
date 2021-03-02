import os

from dotenv import load_dotenv
from dataclasses import dataclass
from pathlib import Path


def load_dot_env_file(env='dev'):
    try:
        env_file = env + '.env'
        env_path = Path('.') / env_file
        load_dotenv(verbose=True, dotenv_path=env_path)
    except Exception as e:
        print(e)
        return e


@dataclass(frozen=True)
class Config:
    TMDB_API_KEY: str


def load_env_vars_to_config(env='dev') -> Config:
    tmdb_api_key = os.getenv("TMDB_API_KEY")
    if not tmdb_api_key:
        raise Exception("TMDB_API_KEY is mandatory for this program")
    config = Config(TMDB_API_KEY=tmdb_api_key)
    return config

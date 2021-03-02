import asyncio

from config import load_dot_env_file, load_env_vars_to_config
from fetch_movie import fetch_movie
from game import Game
from movie import Movie


def game_run():
    movie = Movie("Hera Pheri")
    game = Game(movie)
    while game.is_playable():
        letter = input("Enter letter:\n")
        game.play(letter)
        print(game)

    print(game.result())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    load_dot_env_file()
    config = load_env_vars_to_config()
    asyncio.run(fetch_movie(config, 'hi'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_run()


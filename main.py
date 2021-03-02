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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_run()

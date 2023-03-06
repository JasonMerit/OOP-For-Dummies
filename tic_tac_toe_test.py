from tic_tac_toe import TicTacToe


if __name__ == "__main__":
    game = TicTacToe()
    done = False
    while not done:
        done = game.random_step()
        game.show()
    print(f"{'X' if not game.turn else 'O'} won!")  # TODO Error: forget not
    game.show()
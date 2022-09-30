from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.letter import Letter


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _guess (str): The letter entered by the user.
        _puzzle (Puzzle): The game puzzle.
        _is_playing (boolean): Whether or not to keep playing.
        _win_loose (str): A letter depending on whether the player won or lost.
        _letter (Letter): The letters of the puzzle.
        _terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._guess = ''
        self._puzzle = Puzzle()
        self._is_playing = True
        self._win_loose = ''
        self._letter = Letter()
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Get the puzzle and the parachute. Prompt the user to enter a letter.

        Args:
            self (Director): An instance of Director.
        """
        puzzle = self._letter.puzzle(self._puzzle)
        parachute = self._puzzle.parachute(self._letter)
        self._terminal_service.write_text(f'\n{puzzle}')
        self._terminal_service.write_text(parachute)
        self._guess = self._terminal_service.get_player_guess(
            "\nGuess a letter [a-z]: ", self._letter)
        print()

    def _do_updates(self):
        """Keep track of the state of the game, win, lose, or not win.

        Args:
            self (Director): An instance of Director.
        """
        self._win_loose = self._puzzle.watch_state_game(
            self._guess, self._letter)

    def _do_outputs(self):
        """See the final state of the game, if it was won or lost.

        Args:
            self (Director): An instance of Director.
        """
        if self._win_loose == 'w' or self._win_loose == 'l':
            puzzle = self._letter.puzzle(self._puzzle)
            parachute = self._puzzle.parachute(self._letter)
            self._terminal_service.write_text(f'\n{puzzle}')
            self._terminal_service.write_text(parachute)
            self._is_playing = False
            if self._win_loose == 'w':
                self._terminal_service.write_text('The game is over, you WON.')
            else:
                self._terminal_service.write_text(
                    'The game is over, you LOST.')

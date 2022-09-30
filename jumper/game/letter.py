class Letter:
    """The letters in the puzzle.

    Letters' responsibility is to keep track of wrong and correct letters that are entered from the terminal.

    Attributes:
        _missed_letters (List[str]): The letters that were entered incorrectly.
        _correct_letters (List[str]): The letters that were entered correctly.
    """

    def __init__(self):
        """Constructs a new Letter.

        Args:
            self (Letter): An instance of Letter.
        """
        self._missed_letters = []
        self._correct_letters = []

    def get_correct_letters(self):
        """Returns the list of correct letters.

        Args:
            self (Letter): An instance of Letter.

        Returns:
            list: A list of correct letters.
        """
        return self._correct_letters

    def get_missed_letters(self):
        """Returns the list of wrong letters.

        Args:
            self (Letter): An instance of Letter.

        Returns:
            list: A list of wrong letters.
        """
        return self._missed_letters

    def set_correct_letters(self, letter):
        """Add a letter to the list of correct words.

        Args:
            self (Letter): An instance of Letter.
            letter: A letter that the user entered.
        """
        self._correct_letters.append(letter)

    def set_missed_letters(self, letter):
        """Add a letter to the list of wrong words.

        Args:
            self (Letter): An instance of Letter.
            letter: A letter that the user entered.
        """
        self._missed_letters.append(letter)

    def puzzle(self, puzzle):
        """Returns a string with letters or underscores.

        Args:
            puzzle (Puzzle): An instance of Puzzle.

        Returns:
            str: A string with letters or underscores.
        """
        secret_word = puzzle.get_word()
        blanks = ['_'] * len(puzzle.get_word())
        for i in range(len(secret_word)):
            if secret_word[i] in self.get_correct_letters():
                blanks[i] = secret_word[i]
        return ' '.join(blanks)

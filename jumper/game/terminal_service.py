class TerminalService:
    """A service that handles terminal operations.

    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def get_player_guess(self, prompt, letters):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        while True:
            letter = input(prompt).lower()
            if len(letter) != 1:
                print('Enter a single letter.')
            elif letter in (letters.get_missed_letters()+letters.get_correct_letters()):
                print('You have already guessed that letter. Choose again.')
            elif not letter.isalpha():
                print('Enter a only LETTERS')
            else:
                return letter

    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

import random


class Puzzle:
    """The puzzle that the user must solve.

    The Puzzle's responsibility is to keep track of the parachute and see if the user won or lost.

    Attributes:
        _parachute (List[str]): The different states of the parachute.
        _word (str): A random word that the user must guess.
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._parachute = [
            r"""
  ___
 /___\
 \   /
  \ /
   O
  /|\
  / \

^^^^^^^^""",
            r"""
  
 /___\
 \   /
  \ /
   O
  /|\
  / \

^^^^^^^^""",
            r"""
  
 
 \   /
  \ /
   O
  /|\
  / \

^^^^^^^^""",
            r"""



  \ /
   O
  /|\
  / \

^^^^^^^^""",
            r"""




   X
  /|\
  / \

^^^^^^^^""",
        ]
        self._word = random.choice('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split())

    def get_parachute(self):
        """Returns the list of parachute states.

        Args:
            self (Puzzle): An instance of Puzzle.

        Returns:
            list: A list of parachute states.
        """
        return self._parachute

    def get_word(self):
        """Returns a random word that the user must guess.

        Args:
            self (Puzzle): An instance of Puzzle.

        Returns:
            str: A word that the user must guess.
        """
        return self._word

    def watch_state_game(self, guess, letter):
        """Returns a word or not depending on whether the player won, or didn't win, or lost.

        Args:
            self (Puzzle): An instance of Puzzle.
            guess (str): A letter that the user has entered.
            letter (Letter): An instance of the Letter object.

        Returns:
            str: A word or not depending on whether the player won, or didn't win, or lost.
        """
        if guess in self._word:
            letter.set_correct_letters(guess)
            found_all_letters = True
            for secret_word_letter in self._word:
                if secret_word_letter not in letter.get_correct_letters():
                    found_all_letters = False
                    break
            if found_all_letters:
                return 'w'
        else:
            letter.set_missed_letters(guess)
            if len(letter.get_missed_letters()) == len(self._parachute)-1:
                return 'l'

    def parachute(self, letter):
        """Returns the state or position of the parachute list, depending on how many wrong letters the user has entered.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter (Letter): An instance of the Letter object.

        Returns:
            str: The last state of the parachute.
        """
        index = len(letter.get_missed_letters())
        parachute = self.get_parachute()
        return parachute[index]

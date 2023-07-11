# BagelsProject
Famous Mystery Command Line Game written in Python. You can check readme.md file to know more about game &amp; rules 

Bagels is a deduction game you can play with a friend. Your friend thinks up a random 3-digit number with no repeating digits, and you try to guess what the number is. After each guess, your friend gives you three types of clues:

·        Bagels – None of the three digits you guessed is in the secret number.

·        Pico – One of the digits is in the secret number, but your guess has the digit in the wrong place.

·        Fermi – Your guess has a correct digit in the correct place.

You can get multiple clues after each guess. If the secret number is 456 and your guess is 546 the clues would be “fermi pico pico”. The 6 provides “fermi” and the 5 and 4 provide “pico pico”.

## [Rules](https://inventwithpython.com/chapter11.html)

# Example Bagels Run
```
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:

  Pico         One digit is correct but in the wrong position.

  Fermi        One digit is correct and in the right position.

  Bagels       No digit is correct.
I have thought up a number. You have 10 guesses to get it.
Guess #1:
123
Fermi
Guess #2:
453
Pico
Guess #3:
425
Fermi
Guess #4:
326
Bagels
Guess #5:
489
Bagels
Guess #6:
075
Fermi Fermi
Guess #7:
015
Fermi Pico
Guess #8:
175
You got it!
Do you want to play again? (yes or no)
no
```

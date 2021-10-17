gameon = False
anime = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

within = False
guessed = []
used = []

guesses = 0
wrong = 0

updatemessage = ""
response = ""

def hangCheckLetter(letter: str):
  global guessed, guesses, wrong, within, response
  if letter.lower() not in used:
    if letter.lower() in letters:
      used.append(letter.lower())
      guesses += 1
      for i in range(len(anime)):
        if anime[i].lower() == letter:
          guessed[i] = True
          within = True
          response = (f"The letter {letter} was in the term. Guess another letter.")
      if within == False:
        wrong += 1
        response =(f"That letter is not in the term.")
    else:
      response = "That is not a letter"
  else:
    response = "You already guessed that letter."
  if wrong > 0:
    wrong += "\nYou have guessed wrong {wrong} times. {6-wrong} more before you lose."

def hangUpdate():
  global updatemessage, anime
  updatemessage = ""
  for i in range(len(anime)):
    if guessed[i] == True:
      updatemessage += anime[i] + ""
    elif anime[i] == " ":
      updatemessage += " "
    else:
      updatemessage += "\_"

def checkCompletion():
  global guessed
  finished = False
  for i in guessed:
    if i == True:
      finished = True
    else:
      finished = False
      break
  if finished == True:
    return True

#check if all of guessed is true
#-hangend command (reset all variables and listening)
#send list of letters used
#reset variables when completed
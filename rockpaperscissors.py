import random
picks = ["rock", "paper", "scissors"]
computer_pick = random.choice(picks)

while True:

  user_pick = raw_input("Let's play rock, paper, scissors! Choose your weapon wisely! ")
  user_pick = user_pick.lower()

  while user_pick not in picks: #checks if input is valid
    print "That is not how you play!"
    user_pick = raw_input("Let's play rock, paper, scissors! Choose your weapon wisely! ")
    user_pick = user_pick.lower()

  if user_pick == computer_pick: #checks who wins
    print "Computer chose %s. It's a draw!" % (computer_pick)
  
  if user_pick == "paper":
    if computer_pick == "scissors":
      print "Computer chose scissors. You lose!"
    elif computer_pick == "rock":
      print "Computer chose rock. You win!"
  
  if user_pick == "rock":
    if computer_pick == "scissors":
      print "Computer chose scissors. You win!"
    elif computer_pick == "paper":
      print "Computer chose paper. You lose!"
  
  if user_pick == "scissors":
    if computer_pick == "rock":
      print "Computer chose rock. You lose!"
    elif computer_pick == "paper":
      print "Computer chose paper. You win!"       

  rematch = raw_input("Do you want to play again? y/n ") #asking user for a rematch
  rematch = rematch.lower()
  
  if rematch == "n":
    break

print "Thanks for playing!"
#https://www.dataquest.io/blog/python-projects-for-beginners/

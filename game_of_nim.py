def main():
  #Initialising the game
  print("Welcome to The Ancient Game of Nimm!")  

  num_stones = 20
  player = 1
    
  print ("There are", num_stones, "left")
    
  #First Move
  stones_removed = int(input(f"Player {player} would you like to remove 1 or 2 stones?"))
  while stones_removed != 1 and stones_removed != 2:
      stones_removed = int(input("Please enter 1 or 2: "))
    
  stones_left = num_stones - stones_removed
    
  #Second Move Onwards
  while stones_left > 0:
      print ()
      print ("There are" , stones_left, "stones left")

      #Switch players
      if player == 1:
          player = 2
      else:
          player = 1

      stones_removed = int(input(f"Player {player} would you like to remove 1 or 2 stones?"))
      while stones_removed != 1 and stones_removed != 2:
          stones_removed = int(input("Please enter 1 or 2: "))
        
    stones_left = stones_left - stones_removed
  print("Game Over!")
  if player == 1:
      print("Player 2 wins!")
  else:
      print("Player 1 wins!")

if __name__ == '__main__':
    main()

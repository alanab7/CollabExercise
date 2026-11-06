## Data and Facts: Alana Burgos
"""
Read building data from file and create database 

Args: 
path(str): path to file containing building data
building_hints(dict): dictionary containing building names and short descriptions

Side effects: 
	Updates the dictionary storing the hints that correspond to a building (the building name will be the key (str) and the hints will be stored as the values (set[str])). 
"""

## Score: Mary Magalski
"""
Calculates and updates the user’s score after each round

Args:
	number_of_hints(int): how many hints did the user need to guess the correct answer
	current_total_score(int): add the scores together across all games. Defaults to 0
	current_best_score(int): what the user’s best score is across all games. Defaults to 0

Returns:

	Tuple[int, int]: 
		score(int): total score added together and returned to the user
best_score(int): after playing multiple games, the best score out of all games played will be returned 

"""

## Motivation: Laila Solomon 
"""
Give the player feedback based on whether their guess was correct or incorrect. also , display how many hints they used. 

Args: 
Is_correct (boolean): True means the player guessed the correct campus building. False means the player guessed incorrectly. 
hints_used: the number of hints the user have used 
Returns: 
Str: A message encouraging the player based on their guess, such as “Good job!” if they are correct or “Keep trying!” if they are incorrect.
"""

## Player: Cassius Waller
"""
Creates and keeps track of new and existing players and their scores.

	Args:
		Name(str): a players name 
		Best_score(int): the players best scores

		
	Return:
	Winner(tuple[name(string),score(int)]): returns the player with the highest score, their name and score 

	Side effects:
		Updates the stored score of a players best score if new score is greater.
"""

## Answer validation: Lily Wang
"""
Check the answer from the input and classify the abbreviated names or lowercase and uppercase condition

Args:
   answer(str): the string contains input answer from the user
   selections(str): 10 options from the data randomly selected
   solution(str): the variable contains the real solution of the guessing.

Returns:
   check_correct(str): the message that indicates the answer is consistent with '
       the solution of the question
   or
  
   check_wrong(str): the message that indicates the answer is not consistent
       with the solution of the question.
"""



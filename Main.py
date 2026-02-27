import README.md
import RUNNER.py
import training_goal_race.py 
import training_plan.py
import WEEK.py
import WORKOUT.py
import README.md
import RUNNER.py
import training_goal_race.py 
import training_plan.py
import WEEK.py

from runner import Runner
from training_goal import TrainingGoal
from training_plan import TrainingPlan


def get_race_choice() -> str:     #asking the user to choose which race they want to run
race_options = {"1": "5k", "2": "10k", "3": "half", "4": "full"}    #associating numbers to distances 

while True: #displays the different race distance allowed and prompts the user to input their choice. It continues to loop until a valid choice is made (1-4).
print("\nSelect your race:")
print("1. 5K")
print("2. 10K")
print("3. Half Marathon")
print("4. Full Marathon")

choice = input("Enter the number of your choice: ").strip() 
if choice in race_options:     #if the user input is unvalid (no picking any), it will return an error message and ask the user to input again until they input 1-4
return race_options[choice]

print("Invalid selection. Please choose 1–4.")


def get_experience_choice() -> str: #asking the user to choose their experience level, which will be used to determine the training plan
exp_options = {"1": "beginner", "2": "intermediate", "3": "expert"}

while True: #displays the experience level options and prompts the user to input their choice. It continues to loop until a valid choice is made (1-3).
print("\nSelect experience level:")
print("1. Beginner")
print("2. Intermediate")
print("3. Expert")

choice = input("Enter the number of your choice: ").strip()
if choice in exp_options:
return exp_options[choice]

print("Invalid selection. Please choose 1–3.") #if the user input is unvalid (no picking any), it will return an error message and ask the user to input again until they input 1-3


def get_positive_int(prompt: str) -> int: #defines a function that prompts the user for a positive integer input
while True:
try:
value = int(input(prompt).strip())
if value > 0:
return value
except ValueError:
pass
print("Please enter a positive whole number.") 


def get_non_negative_float(prompt: str) -> float: #defines a function that prompts the user for a non-negative float input
while True:
try:
value = float(input(prompt).strip())
if value >= 0:
return value
except ValueError:
pass
print("Please enter a number 0 or higher.") #returns an error message if the user input is invalid (not a number or negative) and continues to prompt until a valid input is received





name = input("Runner name: ").strip()  #asks for runner name and experience level, which will be used to create a Runner object. It also asks for the current weekly mileage, which will be used to tailor the training plan.
exp = get_experience_choice() 
mileage = get_non_negative_float("Current weekly mileage in km (enter 0 if unknown): ")

runner = Runner(name, exp, mileage) #creates a Runner object using the provided name, experience level, and current weekly mileage. This object will be used to generate a personalized training plan based on the user's inputs.
goal = TrainingGoal(race, weeks)

plan = TrainingPlan(runner, goal) #creates a TrainingPlan object using the Runner and TrainingGoal objects. This object will generate a training plan tailored to the runner's experience level, current mileage
plan.generate() #generates the training plan based on the runner's information
plan.pretty_print() #prints the generated training plan in a readable format, allowing the user to see their personalized training schedule 





print("niguek")

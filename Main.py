from RUNNER import BeginnerRunner, ExpertRunner, IntermediateRunner, Runner    
from training_goal_race import TrainingGoal
from training_plan import TrainingPlan
from visualization import plot_weekly_mileage


def get_race_choice() -> str:
    race_options = {"1": "5k", "2": "10k", "3": "half", "4": "full"}

    while True:
        print("\nSelect your race:")
        print("1. 5K")
        print("2. 10K")
        print("3. Half Marathon")
        print("4. Full Marathon")
        choice = input("Enter the number of your choice: ").strip()
        if choice in race_options:
            return race_options[choice]
        print("Invalid selection. Please choose 1–4.")


def get_experience_choice() -> str:
    exp_options = {"1": "beginner", "2": "intermediate", "3": "expert"}

    while True:
        print("\nSelect experience level:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Expert")
        choice = input("Enter the number of your choice: ").strip()
        if choice in exp_options:
            return exp_options[choice]
        print("Invalid selection. Please choose 1–3.")


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def get_non_negative_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a number 0 or higher.")

race = get_race_choice()
name = input("Runner name: ").strip()
exp = get_experience_choice()
mileage = get_non_negative_float("Current weekly mileage in km (enter 0 if unknown): ")


if exp == "beginner":
    runner = BeginnerRunner(name, mileage)
elif exp == "intermediate":
    runner = IntermediateRunner(name, mileage)
else:  # expert
    runner = ExpertRunner(name, mileage)

weeks = get_positive_int("Number of weeks for training plan: ")
goal_time = get_positive_int("Goal race time in minutes: ")

goal = TrainingGoal(race, weeks, goal_time)

plan = TrainingPlan(runner, goal)
plan.generate()
plan.pretty_print()
plot_weekly_mileage(plan)

plot_weekly_mileage(plan)
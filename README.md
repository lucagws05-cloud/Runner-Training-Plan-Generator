# Runner-Training-Plan-Generator
Customized training plans for runnners over various distances (5k,10k, Half Marathon, Marathon)

Couch Is Lava: Running Training Plan Generator

This is a program which generates customized running plans for users, based on their own personal goals. Users will be able to choose what race/races they want to train for (5 km, 10 km, half marathon, marathon), and after inputting their name, current experience level and mileage, and the number of weeks remaining before the race, the app will generate a running plan customised to their assessed needs.
The goal of this project is to create personalized training plans that are accessible and adapted to everyone’s routine.

This project came about as all group members are avid runners and preparing for a half-marathon happening later in the year, however faced a distinct lack of options when it came to finding running plans to follow. All present options were either of not sufficient quality, or behind a paywall. Realizing that other runners would likely be facing similar issues, we were motivated to create a program which would generate followable plans based on the personal needs of each user.

Several limitations should be taken into account. This program is based on general running principles so the medical condition of each individual is not taken into consideration. 

A distinct challenge we faced was that no group members had any previous coding experience; we would have to learn python in a very short time frame. Aside from the clear problem that a lack of coding knowledge presents, this also meant it was hard for us to determine the scope of our project, and whether it would be possible to actually create what we hoped to in the time frame we were working with. With no knowledge of coding, we had no sense of what was reasonable or not. Additionally, trying to learn python focusing on object-oriented programming, in such a short time frame meant that we were essentially learning starting from the middle, rather than the beginning.

It is made to make running be fun, while improving. The problem is that usually running apps are too serious and not constructive in a fun way. We aim to solve this problem

For runners to be able to track their running. Help runners of different experience levels achieve their specific race goals in a structured and safe way.

# Installation Instructions:
# Clone the Repository
git clone https://github.com/yourusername/Runner-Training-Plan-Generator.git
# Navigate into the Folder
cd Runner-Training-Plan-Generator
# Run the Program
python main.py

Credits


```python
RUNNER

class Runner: 
    def __init__(self, name, experience_level, weekly_mileage=0):
        self.name = name
        self.experience_level = experience_level  # beginner/intermediate/expert
        self.weekly_mileage = weekly_mileage    # distance they run now per week

    def suggest_plan(self):
        if self.experience_level == "beginner":
            return "Run 3-4 times per week, 10-20km total"
        elif self.experience_level == "intermediate":
            return "Run 4-5 times per week, 20-40m total"
        else:
            return "Run 5-6 times per week, 40-60km total"

    def get_info(self):
        return f"Name: {self.name}, Experience level: {self.experience_level}, Current weekly mileage: {self.weekly_mileage} km"

TRAINING GOAL - RACE

class TrainingGoal:
    def __init__(self, distance_km, duration_weeks):
        self.distance_km = distance_km
        self.duration_weeks = duration_weeks

WORKOUT

class Workout:
    def __init__(self, workout_type, distance, intensity):
        self.workout_type = workout_type  # easy, tempo, long, interval
        self.distance = distance
        self.distance = pace
        self.intensity = intensity

def __str__(self):
    return f"{self.workout_type.title()} run - {self.distance} miles at {self.pace} minutes per kilometer"


TRAINING PLAN

class TrainingPlan:
    def __init__(self):
        self.schedule = {}  # {week: {day: Workout}}

PLAN GENERATOR

class PlanGenerator:
    def generate_plan(self, runner, goal):
        pass

TRAINING PROGRAM

class TrainingProgram:
    def run(self):
        runner = self.create_runner()
        goal = self.choose_goal()
        generator = self.select_generator(runner)
        plan = generator.generate_plan(runner, goal)
        self.display_plan(plan)


Runner ──┐
         ├──> PlanGenerator ───> TrainingPlan ───> Workout
Goal  ───┘






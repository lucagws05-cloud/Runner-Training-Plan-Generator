import README.md

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






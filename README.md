# Runner-Training-Plan-Generator
Customized training plans for runnners over various distances (5k,10k, Half Marathon, Marathon)









```python
RUNNER

class Runner: 
    def __init__(self, name, experience_level, weekly_mileage=0):
        self.name = name
        self.experience_level = experience_level  # beginner/intermediate/expert
        self.weekly_mileage = weekly_mileage    # distance they run now per week

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
        self.intensity = intensity

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






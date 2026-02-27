TRAINING GOAL - RACE

class TrainingGoal:
    def __init__(self, distance_km, duration_weeks):
        self.distance_km = distance_km
        self.duration_weeks = duration_weeks

    def is_realistic(self):
        if self.race_type == "5k":
            return self.duration_weeks >= 6
        elif self.race_type == "10k":
            return self.duration_weeks >= 8
        elif self.race_type == "half":
            return self.duration_weeks >= 12
        elif self.race_type == "full":
            return self.duration_weeks >= 16
        else:
            return False


    race = input("Choose your race (5k, 10k, half, full): ")
weeks = int(input("How many weeks until race day? "))

goal = TrainingGoal(race, weeks)

if goal.is_realistic():
    print("Your goal is realistic 👍")
else:
    print("This goal may not be realistic. Consider more preparation time.")


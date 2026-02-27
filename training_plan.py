from typing import List
from runner import Runner
from training_goal_race import TrainingGoal
from week import Week
from workout import Workout

class TrainingPlan:
    def __init__(self, runner: Runner, goal: TrainingGoal):
        self.runner = runner
        self.goal = goal
        self.weeks: List[Week] = []

    def generate(self) -> None:
        self.weeks.clear()
        start_mileage = self._starting_mileage()

        for wk in range(1, self.goal.duration_weeks + 1):
            mileage = start_mileage * (1 + 0.05 * (wk - 1))  # +5% in mileage per week

            if wk >= self.goal.duration_weeks - 1:  # taper mileage over the last 2 weeks
                mileage *= 0.7

            week = Week(wk, round(mileage, 1))      #Creates a week object with the target mileage for that week
            self._build_week(week)                  #Fills each week with workouts based on previous inputs
            self.weeks.append(week)                 #Adds week to the training plan

    def _starting_mileage(self) -> float:          #Uses their provided weekly mileage or falls back on defaults if non entered
        if self.runner.weekly_mileage > 0:
            return self.runner.weekly_mileage

        return {
            "beginner": 15.0,
            "intermediate": 30.0,
            "expert": 50.0,
        }[self.runner.experience_level]

    def _pace_defaults(self):                   #paces for different workout types based on entered experience level
        if self.runner.experience_level == "beginner":
            return {"easy": 7.0, "long": 7.2, "tempo": 6.2, "interval": 5.8}
        if self.runner.experience_level == "intermediate":
            return {"easy": 6.0, "long": 6.2, "tempo": 5.2, "interval": 4.8}
        return {"easy": 5.3, "long": 5.5, "tempo": 4.6, "interval": 4.2}

    def _build_week(self, week: Week) -> None:    #Builds a week of workouts adding the paces and mileage
        paces = self._pace_defaults()
        mileage = week.target_mileage_km

        quality_type = "tempo" 

        long_km = round(mileage * 0.35, 1)        #Determining how much of the weekly mileage is taken up by each type of run (Idea for this section came from ChatGPT)
        quality_km = round(mileage * 0.20, 1)
        easy_km_total = round(mileage - long_km - quality_km, 1)

        easy1 = round(easy_km_total, 1)
        
        week.add_workout(Workout("easy", easy1, paces["easy"], "low"))             #Uses objects from the workout class to create 7 day plan
        week.add_workout(Workout(quality_type, quality_km, paces[quality_type], "high"))
        week.add_workout(Workout("rest"))
        week.add_workout(Workout("easy", easy1, paces["easy"], "low"))
        week.add_workout(Workout("rest"))
        week.add_workout(Workout("long", long_km, paces["long"], "moderate"))
        week.add_workout(Workout("rest"))

    def pretty_print(self) -> None:
        print(self.runner.get_info())
        print(
            f"Goal race: {self.goal.race_type} ({self.goal.distance_km} km),"
            f"{self.goal.duration_weeks} weeks"
        )
        print(f"Realistic? {'Yes' if self.goal.is_realistic() else 'Maybe not'}")
        print()

        for week in self.weeks:
            print(
                f"Week {week.week_number} "
                f"(target {week.target_mileage_km:.1f} km, actual {week.total_mileage():.1f} km)"
            )
            for i, w in enumerate(week.workouts, start=1):
                print(f"  Day {i}: {w}")
            print(f"  Weekly load: {week.total_load():.2f}")
            print("-" * 40)


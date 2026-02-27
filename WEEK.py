from typing import List
from workout import Workout


class Week:
    def __init__(self, week_number: int, target_mileage_km: float):
        self.week_number = week_number
        self.target_mileage_km = float(target_mileage_km)
        self.workouts: List[Workout] = []

    def add_workout(self, workout: Workout) -> None:
        self.workouts.append(workout)

    def total_mileage(self) -> float:
        return round(sum(w.distance_km for w in self.workouts), 1)

    def total_load(self) -> float:
        return round(sum(w.training_load() for w in self.workouts), 2)
from typing import List
from WORKOUT import Workout


class Week:
    def __init__(self, week_number: int, target_mileage_km: float):
        self._week_number = week_number
        self._target_mileage_km = float(target_mileage_km)
        self._workouts: List[Workout] = []

    @property
    def week_number(self) -> int:
        return self._week_number

    @property
    def target_mileage_km(self) -> float:
        return self._target_mileage_km

    @property
    def workouts(self) -> List[Workout]:
        return self._workouts

    def add_workout(self, workout: Workout) -> None:
        self._workouts.append(workout)

    @property
    def total_mileage(self) -> float:
        return round(sum(w.distance_km for w in self._workouts), 1)
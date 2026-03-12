from typing import List
from WORKOUT import Workout


class Week:
    """Represents a week of training in the running plan.

    The class Week tracks which week number of the training plan it is,
    the target mileage for that week, and the workouts needed for that week.
    """

    def __init__(self, week_number: int, target_mileage_km: float):
        """Initializes a Week object.

        Args:
            week_number: The week number in the training plan being generated
            target_mileage_km: The goal mileage for that week (in kilometers)
        """
        self._week_number = week_number
        self._target_mileage_km = float(target_mileage_km)
        self._workouts: List[Workout] = []

    @property
    def week_number(self) -> int:
        """Returns the week number."""
        return self._week_number

    @property
    def target_mileage_km(self) -> float:
        """Returns the target mileage for that week (km)."""
        return self._target_mileage_km

    @property
    def workouts(self) -> List[Workout]:
        """Returns a list of the workouts for that week."""
        return self._workouts

    def add_workout(self, workout: Workout) -> None:
        """Adds a workout to the list of workouts.

        Args:
            workout: A Workout object to be appended to the list workouts
        """
        self._workouts.append(workout)

    @property
    def total_mileage(self) -> float:
        """Returns the total mileage from all workouts added to the Week."""
        return round(sum(w.distance_km for w in self._workouts), 1)
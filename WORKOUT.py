from typing import Optional


class Workout:
    """
    Represent a workout in the Training Plan.

    Workout class contains all the information regarding a workout,
    including type of workout, distance, pace and intensity.
    It includes validation to ensure data is valid and readable.

    Attributes:
        workout_type (str): Type of workout (easy, tempo, long, interval, rest)
        distance_km (float): Workout distance (in km)
        pace_min_per_km (Optional[float]): Running pace in minutes per kilometer
        intensity (str): Workout intensity level (low, moderate, high)
    """

    Valid_Types = {"easy", "tempo", "long", "interval", "rest"}
    Valid_Intensities = {"low", "moderate", "high"}

    def __init__(
        self,
        workout_type: str,
        distance_km: float = 0.0,
        pace_min_per_km: Optional[float] = None,
        intensity: str = "low",
    ):
        """
        Initializes a Workout object.

        Args:
            workout_type (str): Type of workout, must be from Valid_Types
            distance_km (float, optional): Workout distance (default 0.0)
            pace_min_per_km (Optional[float], optional): Pace in min/km,
                required only for active workouts
            intensity (str): Workout intensity, must be from Valid_Intensities
        """
        self.workout_type = workout_type
        self.distance_km = distance_km
        self.pace_min_per_km = pace_min_per_km
        self.intensity = intensity

    @property
    def workout_type(self) -> str:
        """Returns workout type."""
        return self._workout_type

    @workout_type.setter
    def workout_type(self, value: str):
        """
        Set the workout type value only after validation.

        Args:
            value (str): Workout type

        Raises:
            ValueError: If the workout type is not valid
        """
        value = value.lower().strip()
        if value not in self.Valid_Types:
            raise ValueError(f"workout_type must be one of {sorted(self.Valid_Types)}")
        self._workout_type = value

    @property
    def intensity(self) -> str:
        """Returns the intensity level of the workout."""
        return self._intensity

    @intensity.setter
    def intensity(self, value: str):
        """
        Set the workout intensity only after validation.

        Args:
            value (str): Workout intensity

        Raises:
            ValueError: If the workout intensity is invalid
        """
        value = value.lower().strip()
        if value not in self.Valid_Intensities:
            raise ValueError(
                f"intensity must be one of {sorted(self.Valid_Intensities)}"
            )
        self._intensity = value

    @property
    def distance_km(self) -> float:
        """Returns the distance of the workout in kilometers."""
        return self._distance_km

    @distance_km.setter
    def distance_km(self, value: float):
        """
        Set the workout distance only after validation.

        Args:
            value (float): Workout distance

        Raises:
            ValueError: If the distance is negative
        """
        if value < 0:
            raise ValueError("distance_km cannot be negative")
        self._distance_km = float(value)

    @property
    def pace_min_per_km(self) -> Optional[float]:
        """Returns the pace of the workout in minutes per kilometer."""
        return self._pace_min_per_km

    @pace_min_per_km.setter
    def pace_min_per_km(self, value: Optional[float]):
        """
        Set the workout pace only after validation.

        Active workouts must have a positive pace.
        Rest workouts may have no pace.

        Args:
            value (Optional[float]): Workout pace

        Raises:
            ValueError: If an active workout has no pace or negative pace
        """
        if self.workout_type != "rest":
            if value is None or value <= 0:
                raise ValueError(
                    "Active workouts must have a positive pace (min/km)"
                )
        self._pace_min_per_km = value

    @property
    def duration_minutes(self) -> float:
        """
        Returns the duration of a workout in minutes.

        Duration is calculated as distance * pace.
        Rest workouts have duration 0.

        Returns:
            float: Duration of the workout
        """
        if self.workout_type == "rest":
            return 0.0
        return round(self.distance_km * self.pace_min_per_km, 1)

    def __str__(self) -> str:
        """
        Returns a readable description of the workout.

        Returns:
            str: Description of the workout
        """
        if self.workout_type == "rest":
            return "Rest day"

        return (
            f"{self.workout_type.title()} run - {self.distance_km:.1f} km at "
            f"{self.pace_min_per_km:.2f} min/km ({self.intensity})"
        )
from typing import Optional

class Workout:
    Valid_Types = {"easy", "tempo", "long", "interval", "rest"}
    Valid_Intensities = {"low", "moderate", "high"}

    def __init__(self, workout_type: str, distance_km: float = 0.0,
                 pace_min_per_km: Optional[float] = None, intensity: str = "low"):

        self.workout_type = workout_type
        self.distance_km = distance_km
        self.pace_min_per_km = pace_min_per_km
        self.intensity = intensity


    @property
    def workout_type(self) -> str:
        return self._workout_type

    @workout_type.setter
    def workout_type(self, value: str):
        value = value.lower().strip()
        if value not in self.Valid_Types:
            raise ValueError(f"workout_type must be one of {sorted(self.Valid_Types)}")
        self._workout_type = value


    @property
    def intensity(self) -> str:
        return self._intensity

    @intensity.setter
    def intensity(self, value: str):
        value = value.lower().strip()
        if value not in self.Valid_Intensities:
            raise ValueError(f"intensity must be one of {sorted(self.Valid_Intensities)}")
        self._intensity = value


    @property
    def distance_km(self) -> float:
        return self._distance_km

    @distance_km.setter
    def distance_km(self, value: float):
        if value < 0:
            raise ValueError("distance_km cannot be negative")
        self._distance_km = float(value)


    @property
    def pace_min_per_km(self) -> Optional[float]:
        return self._pace_min_per_km

    @pace_min_per_km.setter
    def pace_min_per_km(self, value: Optional[float]):
        if self.workout_type != "rest":
            if value is None or value <= 0:
                raise ValueError("Active workouts must have a positive pace (min/km)")
        self._pace_min_per_km = value


    @property
    def duration_minutes(self) -> float:
        if self.workout_type == "rest":
            return 0.0
        return round(self.distance_km * self.pace_min_per_km, 1)


    def __str__(self) -> str:
        if self.workout_type == "rest":
            return "Rest day"
        return (
            f"{self.workout_type.title()} run - {self.distance_km:.1f} km at "
            f"{self.pace_min_per_km:.2f} min/km ({self.intensity})"
        )
from typing import Optional


class Workout:
    VALID_TYPES = {"easy", "tempo", "long", "interval", "rest"}
    VALID_INTENSITIES = {"low", "moderate", "high"}

    def __init__(
        self,
        workout_type: str,
        distance_km: float = 0.0,
        pace_min_per_km: Optional[float] = None,
        intensity: str = "low",
    ):
        workout_type = workout_type.lower().strip()
        intensity = intensity.lower().strip()

        if workout_type not in self.VALID_TYPES:
            raise ValueError(f"workout_type must be one of {sorted(self.VALID_TYPES)}")

        if intensity not in self.VALID_INTENSITIES:
            raise ValueError(f"intensity must be one of {sorted(self.VALID_INTENSITIES)}")

        if distance_km < 0:
            raise ValueError("distance_km cannot be negative")

        if workout_type != "rest":
            if pace_min_per_km is None or pace_min_per_km <= 0:
                raise ValueError("Non-rest workouts must include a positive pace_min_per_km")
            if distance_km <= 0:
                raise ValueError("Non-rest workouts must have distance_km > 0")

        self.workout_type = workout_type
        self.distance_km = float(distance_km)
        self.pace_min_per_km = pace_min_per_km
        self.intensity = intensity

    def duration_minutes(self) -> float:
        if self.workout_type == "rest":
            return 0.0
        return round(self.distance_km * self.pace_min_per_km, 1)

    def training_load(self) -> float:
        multipliers = {
            "easy": 1.0,
            "tempo": 1.5,
            "long": 1.3,
            "interval": 2.0,
            "rest": 0.0,
        }
        return round(self.distance_km * multipliers[self.workout_type], 2)

    def is_hard_day(self) -> bool:
        return self.workout_type in {"tempo", "interval"}

    def __str__(self) -> str:
        if self.workout_type == "rest":
            return "Rest day"
        return (
            f"{self.workout_type.title()} run - {self.distance_km:.1f} km at "
            f"{self.pace_min_per_km:.2f} min/km ({self.intensity})"
        )
from typing import Optional

class Workout:
    Valid_Types = {"easy", "tempo", "long", "interval", "rest"}     #types of workouts included
    Valid_Intensities = {"low", "moderate", "high"}                 #intensity levels included

    def __init__(self, workout_type: str, distance_km: float = 0.0, pace_min_per_km: Optional[float] = None, intensity: str = "low",):
        workout_type = workout_type.lower().strip()     #ensures the workout type and intensity are lowercase and whitespace is removed         
        intensity = intensity.lower().strip()             

        if workout_type not in self.Valid_Types:        #checks if the workout type can be found in the valid workout types --> the sections raising ValueErrors were added through the help of ChatGPT
            raise ValueError(f"workout_type must be one of {sorted(self.Valid_Types)}")

        if intensity not in self.Valid_Intensities:     #checks if the intensity type can be found in the valid intensity types
            raise ValueError(f"intensity must be one of {sorted(self.Valid_Intensities)}")

        if distance_km < 0:                             #distance cannot be negative
            raise ValueError("distance_km cannot be negative")

        if workout_type != "rest":                      #if the workout type is not rest, then pace and distance must be positive
            if pace_min_per_km is None or pace_min_per_km <= 0:
                raise ValueError("Active workouts (non-rest days) must have a positive pace (min/km)")
            if distance_km <= 0:
                raise ValueError("Active workouts (non-rest days) must have a distance (km) greater than 0")

        self.workout_type = workout_type    
        self.distance_km = float(distance_km)
        self.pace_min_per_km = pace_min_per_km
        self.intensity = intensity

    def duration_minutes(self) -> float:                #calculates the duration of the workout based on the distance and pace
        if self.workout_type == "rest":
            return 0.0
        return round(self.distance_km * self.pace_min_per_km, 1)

    def __str__(self) -> str:                           #summarizes the workout in a readable format 
        if self.workout_type == "rest":
            return "Rest day"
        return (
            f"{self.workout_type.title()} run - {self.distance_km:.1f} km at "
            f"{self.pace_min_per_km:.2f} min/km ({self.intensity})"
        )
    
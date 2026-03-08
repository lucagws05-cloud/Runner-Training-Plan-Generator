class TrainingGoal:

    # -------------------
    # Class constants
    # -------------------

    RACE_DISTANCES_KM = {  # Race lengths that we support
        "5k": 5.0,
        "10k": 10.0,
        "half": 21.1,
        "full": 42.2,
    }

    MIN_WEEKS = {  # Minimum weeks needed to train for each race
        "5k": 6,
        "10k": 8,
        "half": 12,
        "full": 16,
    }

    # -------------------
    # Initialization
    # -------------------

    def __init__(self, race_type: str, duration_weeks: int, goal_time_min: float):
        self.race_type = race_type
        self.duration_weeks = duration_weeks
        self.goal_time_min = goal_time_min  # goal race time (minutes)

    # -------------------
    # Race type property
    # -------------------

    @property
    def race_type(self) -> str:
        return self._race_type

    @race_type.setter
    def race_type(self, value: str):
        value = value.lower().strip()
        if value not in self.RACE_DISTANCES_KM:
            raise ValueError(
                f"race_type must be one of {list(self.RACE_DISTANCES_KM.keys())}"
            )
        self._race_type = value
        self._distance_km = self.RACE_DISTANCES_KM[value]

    # -------------------
    # Distance property
    # -------------------

    @property
    def distance_km(self) -> float:
        return self._distance_km

    # -------------------
    # Duration property
    # -------------------

    @property
    def duration_weeks(self) -> int:
        return self._duration_weeks

    @duration_weeks.setter
    def duration_weeks(self, value: int):
        if value <= 0:
            raise ValueError("duration_weeks must be positive")
        self._duration_weeks = int(value)

    # -------------------
    # Goal time property
    # -------------------

    @property
    def goal_time_min(self) -> float:
        return self._goal_time_min

    @goal_time_min.setter
    def goal_time_min(self, value: float):
        if value <= 0:
            raise ValueError("goal_time must be positive")
        self._goal_time_min = float(value)

    # -------------------
    # Derived race pace
    # -------------------

    @property
    def race_pace(self) -> float:
        """
        Returns race pace in minutes per km
        """
        return self.goal_time_min / self.distance_km

    # -------------------
    # Pace formatting
    # -------------------

    def pace_str(self) -> str:
        """
        Returns race pace formatted as mm:ss /km
        """
        minutes = int(self.race_pace)
        seconds = int((self.race_pace - minutes) * 60)
        return f"{minutes}:{seconds:02d} /km"

    # -------------------
    # Base training paces
    # -------------------

    @property
    def base_training_paces(self) -> dict:
        """
        Returns a dictionary of recommended paces for different training types
        """
        rp = self.race_pace
        return {
            "easy": rp + 1.2,
            "long": rp + 1.4,
            "tempo": rp - 0.2,
            "interval": rp - 0.5
        }

    # -------------------
    # Realism check
    # -------------------

    def is_realistic(self) -> bool:
        """
        Checks if the training duration is sufficient for the race type
        """
        return self.duration_weeks >= self.MIN_WEEKS[self.race_type]
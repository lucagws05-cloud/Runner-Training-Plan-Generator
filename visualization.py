import matplotlib.pyplot as plt
print("Matplotlib imported successfully.")
from training_plan import TrainingPlan


def plot_weekly_mileage(plan: TrainingPlan) -> None:
    """
    Plot weekly target mileage across the training plan.
    """
    if not plan.weeks:
        print("The training plan is empty. Please generate the training plan first.")
        return

    week_numbers = [week.week_number for week in plan.weeks]
    target_mileages = [week.target_mileage_km for week in plan.weeks]

    plt.figure(figsize=(10, 5))
    plt.plot(week_numbers, target_mileages, marker="o", linewidth=2)
    plt.xlabel("Week")
    plt.ylabel("Goal mileage (km)")
    plt.title(f"Weekly Mileage Progression for {plan.runner.name}")
    plt.xticks(week_numbers)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
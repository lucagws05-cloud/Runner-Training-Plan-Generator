'''Utility for plotting total weekly mileage across all weeks of a training plan using Matplotlib


This module contains a function which visualizes weekly goal mileages of a training plan as a line chart
'''

import matplotlib.pyplot as plt
print("Matplotlib imported successfully.")
from training_plan import TrainingPlan




def plot_weekly_mileage(plan: TrainingPlan) -> None:

    '''Graph the weekly mileage of each of the training plan.


    This function generates a line chart representing the weekly mileage (in km) of the training plan. The x-axis contains the week number of the plan, while the y-axis tracks the goal weekly mileage for that week. If a training plan has no weeks (or does not exist), the function prints a message and does not generate the plot.


    Args:
	    plan(TrainingPlan): Object which contains the information of the training plan,
        which includes weekly goal mileages, and week number
    Returns:
	    None
    '''
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
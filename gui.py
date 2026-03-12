import tkinter as tk            # GUI library for creating the application window and widgets   
from RUNNER import BeginnerRunner, IntermediateRunner, ExpertRunner
from training_goal_race import TrainingGoal
from training_plan import TrainingPlan
from visualization import plot_weekly_mileage
import io
from contextlib import redirect_stdout


def generate_plan():        
    '''
    This method generates a week by week training plan based on the user's input from the GUI, including the runners experience level, current weekly mileage, number of weeks until the race, and the goal race time. 
    The generated plan includes weekly mileage progression different types of running trainings easy runs, long runs, tempo runs and rest days.
    The generated training plan is then displayed in the output text box and the weekly mileage progression is plotted using the plot_weekly_mileage function.
    '''
    try:
        name = name_entry.get()         #Retrieves information about the runner, from the GUI input fields
        mileage = float(mileage_entry.get())
        weeks = int(weeks_entry.get())
        goal_time = int(goal_time_entry.get())

        exp = experience_var.get().lower()      #Drop down selections for the user (experience and race type)
        race = race_var.get().lower()

        if exp == "beginner":           #creates the appropriate runner class based on the user's experience level selection
            runner = BeginnerRunner(name, mileage)
        elif exp == "intermediate":
            runner = IntermediateRunner(name, mileage)
        else:
            runner = ExpertRunner(name, mileage)

        goal = TrainingGoal(race, weeks, goal_time) #creates the training goal class based on the user's selections

        plan = TrainingPlan(runner, goal)       #generates the training plan based on the runner and goal, then displays the plan in the text box and plots the weekly mileage progression
        plan.generate()

        output_box.delete(1.0, tk.END)      #Clears the output box before inserting the new training plan

        result = plan.pretty_print()
        if result is None:
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                plan.pretty_print()
            result = buffer.getvalue()

        output_box.insert(tk.END, result)  #Inserts the generated training plan into the output box for the user to read

        plot_weekly_mileage(plan)       #Plots the weekly mileage progression

    except Exception as e:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, f"Error: {e}")

root = tk.Tk()      #Creates the main application window
root.title("Runner Training Plan Generator") 

tk.Label(root, text="Runner name").pack()   #Adds a label and entry field for the runner's name
name_entry = tk.Entry(root)     
name_entry.pack()   

tk.Label(root, text="Weekly mileage (km)").pack()   #Adds a label and entry field for the runner's current weekly mileage in kilometers
mileage_entry = tk.Entry(root)
mileage_entry.pack()

tk.Label(root, text="Number of Weeks Until Race").pack()    #Adds a label and entry field for the number of weeks until the race
weeks_entry = tk.Entry(root)
weeks_entry.pack()

race_var = tk.StringVar(value="Race Distance")      #Adds a drop down menu for the user to select the race distance they are training for
tk.OptionMenu(root, race_var, "5k", "10k", "half", "full").pack()

experience_var = tk.StringVar(value="Experience Level")     #Adds a drop down menu for the user to select their experience level (beginner, intermediate, expert)
tk.OptionMenu(root, experience_var, "beginner", "intermediate", "expert").pack()

tk.Label(root, text="Goal time (minutes)").pack()       #Adds a label and entry field for the user's goal race time in minutes
goal_time_entry = tk.Entry(root)
goal_time_entry.pack()


tk.Button(root, text="Generate Plan", command=generate_plan).pack()     #Adds a button that, when clicked, calls the generate_plan function to create and display the training plan based on the user's input

output_box = tk.Text(root, height=20, width=60)     #Adds a text box to the GUI where the generated training plan will be displayed for the user to read
output_box.pack()       

root.mainloop()     #Starts the GUI event loop, allowing the application to run and respond to user interactions
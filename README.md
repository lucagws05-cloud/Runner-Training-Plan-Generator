# Runner-Training-Plan-Generator
Customized training plans for runners over various distances (5k,10k, Half Marathon, Marathon)

## Description

This is a program which generates customized running plans for users, based on their own personal goals. Users will be able to choose what race/races they want to train for (5 km, 10 km, half marathon, marathon), and after inputting their name, current experience level and mileage, and the number of weeks remaining before the race, the program will generate a running plan customised to their assessed needs.

# Features
  Generates personal week-by week running plans
  Ensures appropriate training load, and prevents overloading
  Customisable based on different experience levels and race distance
  Day by day workouts with distance and pace specified

# Installation
## Prerequisites
Python 3.10 or higher
Pip

## Check Python Version
```bsh
python --version
```
## Set up

1.) Clone the Repository

```bsh
git clone https://github.com/yourusername/Runner-Training-Plan-Generator.git cd Runner-Training-Plan-Generator
```bsh

2.) Set up a Virtual Environment

Windows
```bsh
python -m venv venv venv\Scripts\activate
```

MacOS/Linux
```bsh
python3 -m venv venv source venv/bin/activate
```

3.) Run the Program
```bsh
Python main.py
```

## Example Workflow
Input experience, race distance and mileage
Inputs are ran to program in main.py
Customised plan is generated

## Example Outputs
<put screenshots of example plans here>

# Project Structure

Runner-Training-Plan-Generator/
│
├── README.md    
├── main.py                            # Entry point of the program
├── RUNNER.py                    # Logic for generating the training plan
├── training_goal_race.py      # Runner data model and attributes
├── training_plan.py               #
├── WEEK.py                         #
└──WORKOUT.py                  #
       
# Contributing Guidelines
To contribute:

Fork the repository and create a feature branch
Follow PEP8 style guidelines with any edits made
Ensure new code runs without errors
Submit a pull request with a clear description

# Licensing

##  License

This project was developed as part of an academic assignment.

Copyright (c) 2026 Luca Gws

This software is provided for educational and academic purposes only.
You may view, study, and modify the source code for learning purposes.

Commercial use, redistribution, or use of this code in submitted academic
work without proper attribution is not permitted.

The software is provided "as is", without warranty of any kind.

# Contact Information

## How to Contact for Questions or Feedback:

Open a GitHub Issue
Contact contributors through university emails provided below

Laurence Pobst - l.pobst@student.maastrichtuniversity.nl
Lou Negras - l.negras@student.maastrichtuniversity.nl
Luca Scanlon - l.scanlon@student.maastrichtuniversity.nl
Zélie Leboucq - z.leboucq@student.maastrichtuniversity.nl

## Additional Credits
    ChatGPT - debugging purposes, syntax errors and idea generation (mentioned)


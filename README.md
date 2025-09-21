#Python Kinematics

Project by Seth Doneux

Python Kinematics is a physics calculator developed by Seth Doneux with the goal of allowing users to enter their known variables and determine their unknown variables using equations from Newtonian Mechanics.
The project is a solo endeavor by Seth Doneux.

##Index:

kinematicsUI.py - A UI-based calculator made in tkinter, allowing users to enter their known variables, and using them to solve any possible other variables, all relative to the core kinematic equations. An additional vector calculator is included to help the user convert from standard and vector notation.

kinematics.py - A user-ready, barebones version of the program. Run with python3. Choose equations from available selections, choose unknown to solve for, and enter knowns.

vectors.py - Borrowed vector solver from my custom-written mathematics library (https://github.com/Doneux/Seth-s-Mathematics-Library) integrated into this calculator for ease of access.

##Setup tutorial:
- Install source code, place in a directory.
- If python is not installed, install python 3.
- Run the included .bat file.

##Kinematics UI Usage:
Enter all known variables and hit solve. With each solve pass, see if any previously unsolved variables are now solved. Repeat this process until no new solutions are found.

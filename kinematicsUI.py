#Seth Doneux
#Python Kinematics GUI Program
#Solo project

from tkinter import *
import math
import vectors #vectors.py is my own vector script. please make sure you have it installed to the same folder as this file.

#main program
try:
    #displacement variables
    Xi = 0
    Xf = 0
    dX = Xf - Xi
    #time
    Ti = 0
    Tf = 0
    dT = Tf - Ti
    #Velocity
    Vi = 0
    Vf = 0
    dV = Vi - Vf
    V = dX / dT
    #Acceleration
    Ai = 0
    Af = 0
    dA = Af - Ai
    A = dV / dT
    #Mass
    M = 0
    #Force
    F = M * A
    #Possible ways to solve for each:
    def solve(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F):
        #solve_acceleration:
        A = dV/dT
        A = F/M
        Af = dA + Ai
        Ai = dA - Af
        #solve_mass:
        M = F / A
        #solve_velocity:
        dV = A * dT
        Vf = dV + Vi
        Vi = dV - Vf
        #solve_force:
        F = M * A
        #solve_displacement:
        dX = V * dT
        Xf = dX + Xi
        Xi = dX - Xf
        #solve_time:
        dT = dX / V
        Tf = dT + Ti
        Ti = dT - Tf
        #continuously run solution functions until no variables have changed
except:
    print("Solutions are still work in progress! See kinematics.py and Seth's Mathematics Library for user-ready tools!")

#window setup
win = Tk()
win.title("Python Kinematics")
win.geometry('250x500')
#Window setup - 9 columns, middle column at 5
title = Label(text="Python Kinematics Solver - Seth Doneux")
title.grid(columnspan=9)
mmenu = Button(command=vectors.vectorsolve, text="Solve Vectors")
mmenu.grid(row=2, column=4)


win.mainloop()

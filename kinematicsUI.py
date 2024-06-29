#Seth Doneux
#Python Kinematics GUI Program
#Solo project

from tkinter import *
import math
import vectors #vectors.py is my own vector script. please make sure you have it installed to the same folder as this file.

#this is currently buggy, as placeholder zeros will cause overwriting in solution process
#will likely add separate solution sections/buttons for each equation, so that the givens themselves are not modified
#but in the meantime i may look for a solution by analyzing what can be solved based on which givens have input and which do not


#main program
#displacement variables
Xi = 0.0
Xf = 0.0
dX = Xf - Xi
#time
Ti = 0.0
Tf = 0.0
dT = Tf - Ti
#Velocity
Vi = 0.0
Vf = 0.0
dV = Vf - Vi
try:
    V = dX / dT
except:
    V = 0.0
#Acceleration
Ai = 0.0
Af = 0.0
dA = Af - Ai
try:
    A = dV / dT
except:
    A = 0.0
#Mass
M = 0.0
#Force
F = M * A
#Possible ways to solve for each:
def solve(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F):
    #put the args in a list
    valuelist = [Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F]
    #save their original values to a new list
    newvaluelist = []
    for i in valuelist:
        newvaluelist.append(i)
    #get differences
    dX = Xf - Xi
    dT = Tf - Ti
    dV = Vf - Vi
    dA = Af - Ai
    #solve_force:
    F = M * A
    #solve_acceleration:
    try:
        A = dV / dT
    except:
        pass
    try:
        A = F/M
    except:
        pass
    Af = dA + Ai
    Ai = dA - Af
    #solve_mass:
    try:
        M = F / A
    except:
        pass
    #solve_velocity:
    dV = A * dT
    Vf = dV + Vi
    Vi = dV - Vf
    try:
        V = dX / dT
    except:
        pass
    #solve_displacement:
    dX = V * dT
    Xf = dX + Xi
    Xi = dX - Xf
    #solve_time:
    try:
        dT = dX / V
    except:
        pass
    Tf = dT + Ti
    Ti = dT - Tf
    #continuously run solution functions until no variables have changed
    for i in range(len(valuelist)):
        if valuelist[i] != newvaluelist[i]:
            solve(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F)
            break
    return Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F

#window setup
win = Tk()
win.title("Python Kinematics")
win.geometry('250x500')
#Window setup - 9 columns, middle column at 5
title = Label(text="Python Kinematics Solver - Seth Doneux")
title.grid(columnspan=9)
mmenu = Button(command=vectors.vectorsolve, text="Solve Vectors")
mmenu.grid(row=2, column=4)
#Actual physics solver setup
kintitle = Label(text="Enter Known Variables")
kintitle.grid(columnspan=9)

#displacement setup
xtitle = Label(text="Displacement X") #overall title
xtitle.grid(columnspan=9)
xititle = Label(text="Xi") #variable title
xititle.grid()
xibox = Entry(width=5) #variable box
xibox.grid(row=5, column=2, columnspan=3) #placed next to title

xftitle = Label(text="Xf")
xftitle.grid(row=5, column=5)
xfbox = Entry(width=5)
xfbox.grid(row=5, column=6, columnspan=3)

dxtitle = Label(text="dX")
dxtitle.grid()
dxbox = Entry(width=5)
dxbox.grid(row=6, column=2, columnspan=3)

#time setup
ttitle = Label(text="Time T") #overall title
ttitle.grid(columnspan=9)
tititle = Label(text="Ti") #variable title
tititle.grid()
tibox = Entry(width=5) #variable box
tibox.grid(row=8, column=2, columnspan=3) #placed next to title

tftitle = Label(text="Tf")
tftitle.grid(row=8, column=5)
tfbox = Entry(width=5)
tfbox.grid(row=8, column=6, columnspan=3)

dttitle = Label(text="dT")
dttitle.grid()
dtbox = Entry(width=5)
dtbox.grid(row=9, column=2, columnspan=3)

#velocity setup
vtitle = Label(text="Velocity V")
vtitle.grid(columnspan=9)
vititle = Label(text="Vi")
vititle.grid()
vibox = Entry(width=5)
vibox.grid(row=11, column=2, columnspan=3)

vftitle = Label(text="Vf")
vftitle.grid(row=11, column=5)
vfbox = Entry(width=5)
vfbox.grid(row=11, column=6, columnspan=3)

dvtitle = Label(text="dV")
dvtitle.grid()
dvbox = Entry(width=5)
dvbox.grid(row=12, column=2, columnspan=3)

vatitle = Label(text="V")
vatitle.grid(row=12, column=5)
vabox = Entry(width=5)
vabox.grid(row=12, column=6, columnspan=3)

#acceleration setup
atitle = Label(text="Acceleration A")
atitle.grid(columnspan=9)
aititle = Label(text="Ai")
aititle.grid()
aibox = Entry(width=5)
aibox.grid(row=14, column=2, columnspan=3)

aftitle = Label(text="Af")
aftitle.grid(row=14, column=5)
afbox = Entry(width=5)
afbox.grid(row=14, column=6, columnspan=3)

datitle = Label(text="dA")
datitle.grid()
dabox = Entry(width=5)
dabox.grid(row=15, column=2, columnspan=3)

aatitle = Label(text="A")
aatitle.grid(row=15, column=5)
aabox = Entry(width=5)
aabox.grid(row=15, column=6, columnspan=3)

#mass
masstitle = Label(text="Mass M")
masstitle.grid(columnspan=9)
mtitle = Label(text="M")
mtitle.grid()
mbox = Entry(width=5)
mbox.grid(row=17, column=2, columnspan=3)

#force
forcetitle = Label(text="Force F")
forcetitle.grid(columnspan=9)
ftitle = Label(text="F")
ftitle.grid()
fbox = Entry(width=5)
fbox.grid(row=19, column=2, columnspan=3)

#Sets values to screen
def display_values(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F):
    xibox.delete(0, END)
    xibox.insert(0, str(Xi))
    xfbox.delete(0, END)
    xfbox.insert(0, str(Xf))
    dxbox.delete(0, END)
    dxbox.insert(0, str(dX))
    tibox.delete(0, END)
    tibox.insert(0, str(Ti))
    tfbox.delete(0, END)
    tfbox.insert(0, str(Tf))
    dtbox.delete(0, END)
    dtbox.insert(0, str(dT))
    vibox.delete(0, END)
    vibox.insert(0, str(Vi))
    vfbox.delete(0, END)
    vfbox.insert(0, str(Vf))
    dvbox.delete(0, END)
    dvbox.insert(0, str(dV))
    vabox.delete(0, END)
    vabox.insert(0, str(V))
    aibox.delete(0, END)
    aibox.insert(0, str(Ai))
    afbox.delete(0, END)
    afbox.insert(0, str(Af))
    dabox.delete(0, END)
    dabox.insert(0, str(dA))
    aabox.delete(0, END)
    aabox.insert(0, str(A))
    mbox.delete(0, END)
    mbox.insert(0, str(M))
    fbox.delete(0, END)
    fbox.insert(0, str(F))

#Call it once in setup for good measure
display_values(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F)

#Solver function
def solve_unknowns():
    Xi = float(xibox.get())
    Xf = float(xfbox.get())
    dX = float(dxbox.get())
    Ti = float(tibox.get())
    Tf = float(tfbox.get())
    dT = float(dtbox.get())
    Vi = float(vibox.get())
    Vf = float(vfbox.get())
    dV = float(dvbox.get())
    V = float(vabox.get())
    Ai = float(aibox.get())
    Af = float(afbox.get())
    dA = float(dabox.get())
    A = float(aabox.get())
    M = float(mbox.get())
    F = float(fbox.get())
    Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F = solve(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F)
    display_values(Xi, Xf, dX, Ti, Tf, dT, Vi, Vf, dV, V, Ai, Af, dA, A, M, F)

solvetitle = Label(text="Solve Unknown Variables")
solvetitle.grid(columnspan= 9)
solvebutton = Button(text="Solve", command=solve_unknowns)
solvebutton.grid(columnspan=9)


win.mainloop()

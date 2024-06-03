import math
restart = 'y'
#While loop controls whether we restart or not. Based on user input at end.
while restart.lower() == 'y':
    print("Choose the equation you want to use:")
    print("1. Velocity (v = d/t)")
    print("2. Acceleration (a = v/t)")
    print("3. Centripetal Acceleration (ac = v^2/r)")
    print("4. Force (f = ma)")
    print("5. Normal Force (n = mg or n = mg*cos(o))")
    print("6. Spring Force (f = -kx)")

    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 1:
        #Velocity Case
        variable = input("Which variable do you want to solve for? (v, d, t): ")
        if variable == 'v':
            d = float(input("Enter displacement (d): "))
            t = float(input("Enter time (t): "))
            v = d / t
            print(f"Velocity (v) = {v}")
        elif variable == 'd':
            v = float(input("Enter velocity (v): "))
            t = float(input("Enter time (t): "))
            d = v * t
            print(f"Displacement (d) = {d}")
        elif variable == 't':
            v = float(input("Enter velocity (v): "))
            d = float(input("Enter displacement (d): "))
            t = d / v
            print(f"Time (t) = {t}")

    elif choice == 2:
        #Acceleration Case
        variable = input("Which variable do you want to solve for? (a, v, t): ")
        if variable == 'a':
            v = float(input("Enter velocity (v): "))
            t = float(input("Enter time (t): "))
            a = v / t
            print(f"Acceleration (a) = {a}")
        elif variable == 'v':
            a = float(input("Enter acceleration (a): "))
            t = float(input("Enter time (t): "))
            v = a * t
            print(f"Velocity (v) = {v}")
        elif variable == 't':
            v = float(input("Enter velocity (v): "))
            a = float(input("Enter acceleration (a): "))
            t = v / a
            print(f"Time (t) = {t}")

    elif choice == 3:
        #Centripetal Acceleration Case
        variable = input("Which variable do you want to solve for? (ac, v, r): ")
        if variable == 'ac':
            v = float(input("Enter velocity (v): "))
            r = float(input("Enter radius (r): "))
            ac = v**2 / r
            print(f"Centripetal Acceleration (ac) = {ac}")
        elif variable == 'v':
            ac = float(input("Enter centripetal acceleration (ac): "))
            r = float(input("Enter radius (r): "))
            v = math.sqrt(ac * r)
            print(f"Velocity (v) = {v}")
        elif variable == 'r':
            ac = float(input("Enter centripetal acceleration (ac): "))
            v = float(input("Enter velocity (v): "))
            r = v**2 / ac
            print(f"Radius (r) = {r}")

    elif choice == 4:
        # Force Case
        variable = input("Which variable do you want to solve for? (f, m, a): ")
        if variable == 'f':
            m = float(input("Enter mass (m): "))
            a = float(input("Enter acceleration (a): "))
            f = m * a
            print(f"Force (f) = {f}")
        elif variable == 'm':
            f = float(input("Enter force (f): "))
            a = float(input("Enter acceleration (a): "))
            m = f / a
            print(f"Mass (m) = {m}")
        elif variable == 'a':
            f = float(input("Enter force (f): "))
            m = float(input("Enter mass (m): "))
            a = f / m
            print(f"Acceleration (a) = {a}")

    elif choice == 5:
        # Normal Force Cases
        sub_choice = int(input("Choose the normal force equation: 1 for n = mg, 2 for n = mg*cos(o): "))
        if sub_choice == 1:
            variable = input("Which variable do you want to solve for? (n, m, g): ")
            if variable == 'n':
                m = float(input("Enter mass (m): "))
                g = 9.8  # Earth's gravitational acceleration, simplified for our case (Early mechanics courses)
                n = m * g
                print(f"Normal Force (n) = {n}")
            elif variable == 'm':
                n = float(input("Enter normal force (n): "))
                g = 9.8
                m = n / g
                print(f"Mass (m) = {m}")
        elif sub_choice == 2:
            variable = input("Which variable do you want to solve for? (n, m, o): ")
            if variable == 'n':
                m = float(input("Enter mass (m): "))
                g = 9.8
                o = float(input("Enter angle (o) in degrees: "))
                n = m * g * math.cos(math.radians(o))
                print(f"Normal Force (n) = {n}")
            elif variable == 'm':
                n = float(input("Enter normal force (n): "))
                g = 9.8
                o = float(input("Enter angle (o) in degrees: "))
                m = n / (g * math.cos(math.radians(o)))
                print(f"Mass (m) = {m}")
            elif variable == 'o':
                n = float(input("Enter normal force (n): "))
                m = float(input("Enter mass (m): "))
                g = 9.8
                # Arccos is used here, and it's a finnicky function, so we use a try-except case to catch errors.
                try:
                    o = math.acos((n / round(m * g, 3))) #Here we use the acos function, as well as the rounding function, to account for floating-point imprecision.
                    print(f"Angle (o) in degrees = {o * 180 / math.pi} (approximately)")
                except:
                    print(f"Error in calculation: arccos({n} / ({m} * {g})) Please check variables.")

    elif choice == 6:
        #Spring Force Case
        variable = input("Which variable do you want to solve for? (f, k, x): ")
        if variable == 'f':
            k = float(input("Enter spring constant (k): "))
            x = float(input("Enter displacement (x): "))
            f = -k * x
            print(f"Spring Force (f) = {f}")
        elif variable == 'k':
            f = float(input("Enter spring force (f): "))
            x = float(input("Enter displacement (x): "))
            k = -f / x
            print(f"Spring Constant (k) = {k}")
        elif variable == 'x':
            f = float(input("Enter spring force (f): "))
            k = float(input("Enter spring constant (k): "))
            x = -f / k
            print(f"Displacement (x) = {x}")
    
    restart = input("Solve more? Y/N: ")
# End While Control

print("The program will now exit.")

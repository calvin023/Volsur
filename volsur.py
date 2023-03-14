import volsurfunc

vChoice = input("2D or 3D?\n")
if vChoice == "2":
    vChoice2 = input(
        "Please select one of the following:\n1. Circle\n2. Triangle\n3. Square\n")
    if vChoice2 == "1":
        vRadius = float(input("Please enter the radius: "))
        print(volsurfunc.sur_circle(vRadius))
    elif vChoice2 == "2":
        vSide1 = float(input("Please enter the length of the first side: "))
        vSide2 = float(input("Please enter the length of the second side: "))
        vAngle = float(input("Please enter the angle of the sides: "))
        print(volsurfunc.sur_triangle(vSide1, vSide2, vAngle))
    elif vChoice2 == "3":
        vSide = float(input("Please enter the length of a side: "))
        print(volsurfunc.sur_square(vSide))
    else:
        print("Wrong input")


elif vChoice == "3":
    vChoice2 = input(
    "Please select one of the following:\n1. Round\n2. Pyramid\n3. Cube\n4. Cone\n")
    if vChoice2 == "1":
        vRoundAuswahl = input("Sphere or Ellipsoid? [S/E]\n")
        if vRoundAuswahl == "s":
            vCirc = float(input("Please enter the circumference of the sphere: "))
            print(volsurfunc.vol_sphere(vCirc))
        elif vRoundAuswahl == "e":
            vHeigth = float(input("Please enter the heigth of the ellipsoid: "))
            vLength = float(input("Please enter the length of the ellipsoid: "))
            vWidth = float(input("Please enter the width of the ellipsoid: "))
            print(volsurfunc.vol_ellipsoid(vHeigth, vLength, vWidth))
    elif vChoice2 == "2":
        vPyramidAuswahl = input("Square or triangle? [S/T]\n")
        if vPyramidAuswahl == "s":
            vLength = float(input("Please enter the length of the base: "))
            vWidth = float(input("Please enter the width of the base: "))
            vHeigth = float(input("Please enter the heigth of the pyramid: "))
            print(volsurfunc.vol_sqr_pyramid(vLength, vWidth, vHeigth))
        elif vPyramidAuswahl == "t":
            vSide1 = float(
                input("Please enter the length of the first side: "))
            vSide2 = float(
                input("Please enter the length of the second side: "))
            vAngle = float(input("Please enter the angle of the sides: "))
            vHeigth = float(input("Please enter the height of the pyramid: "))
            print(volsurfunc.vol_tri_pyramid(vSide1, vSide2, vAngle, vHeigth))
    elif vChoice2 == "3":
        vEdge = float(input("Please enter the length of an edge: "))
        print(volsurfunc.vol_cube(vEdge))
    elif vChoice2 == "4":
        vRadius = float(input("Please enter the radius of the base: "))
        vHeight = float(input("Please enter the height of the cone: "))
        print(volsurfunc.vol_cone(vRadius, vHeight))
    elif vChoice2 == "5":
        vRadius = float(input("Please enter the radius of the base: "))
        vHeight = float(input("Please enter the height of the cylinder: "))
        print(volsurfunc.vol_cylinder(vRadius, vHeight))
    else:
        print("Wrong input")
else:
    print("Wrong input")

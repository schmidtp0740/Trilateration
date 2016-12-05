import math

def trilaterationSolution(pt_a, pt_b, pt_c):
    #determine the coordinate at the origin
    m = 0.0
    n = 0.0
    p = 0.0
    s = 0.0
    q = 0.0
    r = 0.0
    rad_1 = 0.0
    rad_2 = 0.0
    rad_3 = 0.0

    if float(pt_a[0]) == 0.0 and float(pt_a[1]) == 0.0:
        m = (float(pt_a[0]))
        n = (float(pt_a[1]))
        rad_1 = (float(pt_a[2]))

        #determine the coordinate that is on the x axis based on the origin coordinate
        if float(pt_b[1]) == 0.0:
            p = (float(pt_b[0]))
            s = (float(pt_b[1]))
            rad_2 = (float(pt_b[2]))

            #assign the third coordinate as default
            q = (float(pt_c[0]))
            r = (float(pt_c[1]))
            rad_3 = (float(pt_c[2]))

        elif float(pt_c[1]) == 0.0:
            p = (float(pt_c[0]))
            s = (float(pt_c[1]))
            rad_2 = (float(pt_c[2]))

            q = (float(pt_b[0]))
            r = (float(pt_b[1]))
            rad_3 = (float(pt_b[2]))

    elif float(pt_b[0]) == 0.0 and float(pt_b[1]) == 0.0:
        m = (float(pt_b[0]))
        n = (float(pt_b[1]))
        rad_1 = (float(pt_b[2]))

        if float(pt_a[1]) == 0.0:
            p = (float(float(pt_a[0])))
            s = (float(pt_a[1]))
            rad_2 = (float(pt_a[2]))

            q = (float(pt_c[0]))
            r = (float(pt_c[1]))
            rad_3 = (float(pt_c[2]))

        elif float(pt_c[1]) == 0.0:
            p = (float(pt_c[0]))
            s = (float(pt_c[1]))
            rad_2 = (float(pt_c[2]))

            q = (float(pt_a[0]))
            r = (float(pt_a[1]))
            rad_3 = (float(pt_a[2]))

    elif float(pt_c[0]) == 0.0 and float(pt_c[0]) == 0.0:
        m = (float(pt_c[0]))
        n = (float(pt_c[1]))
        rad_1 = (float(pt_c[2]))

        if float(pt_b[1]) == 0.0:
            p = (float(pt_b[0]))
            s = (float(pt_b[1]))
            rad_2 = (float(pt_b[2]))

            q = (float(pt_a[0]))
            r = (float(pt_a[1]))
            rad_3 = (float(pt_a[2]))

        elif float(pt_a[1]) == 0.0:
            p = (float(pt_a[0]))
            s = (float(pt_a[1]))
            rad_2 = (float(pt_a[2]))

            q = (float(pt_b[0]))
            r = (float(pt_b[1]))
            rad_3 = (float(pt_b[2]))


    x = ( rad_1**2 - rad_2**2 + p**2 ) / ( 2*p )
    y = math.sqrt(rad_1**2 - x**2)

    if(rad_3**2 == ( (x - q)**2 + (y - r)**2)):
        print("d_3^2 = {}^2 = ({} - {})^2 + ({} - {}) ^ 2".format(rad_3 ,x , q, y, r))
        print("Radical Center Coordinates: ({}, {})".format(x, y))

    elif( rad_3**2 == ( (x - q)**2 + ((-y) - r)**2 ) ):
        print("d_3^2 = {}^2 = ({} - {})^2 + ({} - {})^2".format(rad_3 ,x , q, -y, r))
        print("Radical Center Coordinates: ({}, {})".format(x, -y))

    else:
        print("d_3^2 = {}^2 = ({} - {})^2 + ({} - {}) ^ 2".format(rad_3 ,x , q, y, r))
        print("{} = {} ^2 + {}^2".format(rad_3**2, x - q, y - r))
        print("{} =  {} \n".format(rad_3**2, (x - q)**2 + (y - r)**2))

        print("d_3 ^ 2 = {}^2 = ({} - {})^2 + ({} - {}) ^ 2".format(rad_3 ,x , q, -y, r))
        print("{} = {} ^2 + {}^2".format(rad_3**2, x - q, -y - r))
        print("{} =  {} \n".format(rad_3**2, (x - q)**2 + (-y - r)**2))

        print("Radical Center Coordinates: ({}, (+-){})".format(x, y))


print("Enter the first coordinate (0, 0):x y radius")
pt_a = input().split()

print("Enter the second Coordinate(0, y):x y radius")
pt_b = input().split()

print("Enter the third Coordinate(x, y):x y radius")
pt_c = input().split()

trilaterationSolution(pt_a, pt_b, pt_c)

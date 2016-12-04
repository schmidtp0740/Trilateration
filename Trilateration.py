import math

def trilaterationSolution(pt_a, pt_b, pt_c):
    #determine the coordinate at the origin
    m, n, p, s, q, r, rad_1, rad_2, rad_3 = 0.0
    if pt_a[0] == 0 and pt_a[1] == 0:
        m = float(pt_a[0])
        n = float(pt_a[1])
        rad_1 = float(pt_a[2])

        #determine the coordinate that is on the x axis based on the origin coordinate
        if pt_b[1] == 0:
            p = float(pt_b[0])
            s = float(pt_b[1])
            rad_2 = float(pt_b[2])

            #assign the third coordinate as default
            q = float(pt_c[0])
            r = float(pt_c[1])
            rad_3 = float(pt_c[2])

        elif pt_c[1] == 0:
            p = float(pt_c[0])
            s = float(pt_c[1])
            rad_2 = float(pt_c[2])

            q = float(pt_b[0])
            r = float(pt_b[1])
            rad_3 = float(pt_b[2])

    elif pt_b[0] == 0 and pt_b[1] == 0:
        m = float(pt_b[0])
        n = float(pt_b[1])
        rad_1 = float(pt_b[2])

        if pt_a[1] == 0:
            p = float(pt_a[0])
            s = float(pt_a[1])
            rad_2 = float(pt_a[2])

            q = float(pt_c[0])
            r = float(pt_c[1])
            rad_3 = float(pt_c[2])

        elif pt_c[1] == 0:
            p = float(pt_c[0])
            s = float(pt_c[1])
            rad_2 = float(pt_c[2])

            q = float(pt_a[0])
            r = float(pt_a[1])
            rad_3 = float(pt_a[2])

    elif pt_c[0] == 0 and pt_c[0] == 0:
        m = float(pt_c[0])
        n = float(pt_c[1])
        rad_1 = float(pt_c[2])

        if pt_b[1] == 0:
            p = float(pt_b[0])
            s = float(pt_b[1])
            rad_2 = float(pt_b[2])

            q = float(pt_a[0])
            r = float(pt_a[1])
            rad_3 = float(pt_a[2])

        elif pt_a[1] == 0:
            p = float(pt_a[0])
            s = float(pt_a[1])
            rad_2 = float(pt_a[2])

            q = float(pt_b[0])
            r = float(pt_b[1])
            rad_3 = float(pt_b[2])


    x = ( math.pow(rad_1, 2) - math.pow(rad_2, 2) + math.pow(p, 2) ) / ( 2*p )
    y = math.sqrt(math.pow(rad_1, 2) - math.pow(x,2) )

    if(math.pow(rad_3, 2) == ( math.pow( (x - q), 2) + math.pow((y - r), 2))):
        print("d_3 ^ 2 = {}^2 = ({} - {})^2 + ({} - {}) ^ 2".format(rad_3 ,x , q, y, r))
        print("Radical Center Coordinates: ({}, {})".format(x, y))

    elif(math.pow(rad_3, 2) == ( math.pow((x - q), 2) + math.pow(( (-y) - r), 2))):
        print("d_3 ^ 2 = {}^2 = ({} - {})^2 + ({} - {}) ^ 2".format(rad_3 ,x , q, -y, r))
        print("Radical Center Coordinates: ({}, {})".format(x, y))

    else:
        print("d_3 ^ 2 = {}^2 = ({} - {})^2 + ( {} - {}) ^ 2".format(rad_3 ,x , q, y, r))
        print(rad_3**2, ' = (', x-q,')^2 + (', y -r,')^2')
        print(rad_3**2, ' = ', (x-q)**2 + (y-r)**2)
        print("\n")
        print("d_3 ^ 2 = {}^2 = ({} - {})^2 + ( -{} - {}) ^ 2".format(rad_3 ,x , q, y, r))
        print(rad_3**2, ' = (', x-q,')^2 + (', -y -r,')^2')
        print(rad_3**2, ' = ', (x-q)**2 + (-y-r)**2)
        print("\n")

        print("Radical Center Coordinates: ({}, (+-){})".format(x, y))


print("Enter the radius of the first coordinate (0, 0):radius")
pt_a = input().split()

print("Enter the Coordinates of the second point(0, y):x y radius")
pt_b = input().split()

print("Enter the Coordinates of the third point(x, y):x y radius")
pt_c = input().split()

trilaterationSolution(pt_a, pt_b, pt_c)

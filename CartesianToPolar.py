# Travis Matthews
import math

def getRadius(x,y):
    # returns the distance of (x,y) from (0,0) and truncates to two decimal places
    return math.sqrt(math.pow(x,2) + math.pow(y,2))

def getTheta(x, y):
    # returns the arctan of y/x and truncates to two decimal places
    if (y == 0):
        if (x >= 0):
            return 0
        if (x < 0):
            return 180
    if (x == 0):
        if (y > 0):
            return 90
        if (y < 0):
            return 270
    theta = math.degrees(math.atan(y/x))
    # quadrant I
    if (x > 0 and y > 0):
        return theta
    # quadrant II
    if (x < 0 and y > 0):
        return theta + 90
    # quadrant III
    if (x < 0 and y < 0):
        return theta + 180
    # quadrant IV
    if (x > 0 and y < 0):
        return math.fabs(theta)


def main():
    # Endless loop
    while(True):
        # takes input for x and y
        # prints the polar values of (x,y)
        try:
            x = float(raw_input('Enter X: '))
            y = float(raw_input('Enter Y: '))
            print
            print '\t(%d, %d)'%(x, y)
            print '\tRadius:\t', getRadius(x, y)
            print '\tTheta:\t', getTheta(x, y)
            print
        except ValueError:
            print "Not a number"

main()

import numpy as np
import math
import sys
from termcolor import cprint

#=====command line arguments
inputX = float(sys.argv[1])
inputY = float(sys.argv[2])
inputC1 = float(sys.argv[3])
inputC2 = float(sys.argv[4])
inputAlphaMax = float(sys.argv[5])

#======assert some global options
# verbose gives debugging output
# info gives minimal informational output
## !verbose and !info gives only results output
# color gives different output different style
# strongWolfe enforces strong wolfe conditions
verbose = False
info = False
color = False
strongWolfe = True

#=====define some helper functions

def myblandprint(x):
    if(verbose or info):
        print(x)

def infoprint(x):
    if(color):
        cprint(x, 'magenta')
    else:
        myblandprint(x)

def myprint(x):
    if(color):
        cprint(x, 'cyan')
    elif(verbose):
        myblandprint(x)

#distance btween two points in 2d space
def ndist( x, y ):
    return math.sqrt( (x.item(0)-y.item(0))**2.0 + (x.item(1)-y.item(1))**2.0 )


infoprint( "numpy version: " + str(np.version.version) )
infoprint( "Strong Wolfe is " + str(strongWolfe) )
infoprint( "\n" )

#=====assert initial values
leftEnd = 0.0
rightEnd = 50.0
phi = (math.sqrt(5.0) + 1.0) / 2.0

#===== BEGIN PRIMARY FUNCTION DEFINITIONS

#this is the concrete function, given in the assignment description
#returns a scalar value
def thisFunction(x, y):
    return ( 100*(y - x**2)**2 + (1-x)**2 )

#this is the gradient of the given function
#returns a 2d matrix
def thisGrad(x, y):
    dx = (-400*x*y) + (400*(x**3)) + (2*x) - 2
    dy = (200*y) - (200*(x**2))
    myprint("this grad is " + str( np.matrix((dx,dy)) ))
    return np.matrix( (dx, dy) )

#this is the phi function
#INPUTS
## xk is the current position
## alpha is the distance from the initial position
## dk is the direction of movement
#returns a scalar value
def phiFunction( xk, alpha, dk ):
    #construct the new point
    point = xk + alpha * dk
    #break down the new point dimension-wise
    x = point.item(0)
    y = point.item(1)
    return thisFunction( x, y )

#this is the gradient of the phi function
#INPUTS
## xk is the current position
## alpha is the distance from the initial position
## dk is the direction of movement
#OUTPUTS the rate of change of phi with respect to alpha
def gradPhi(xk, alpha, dk):
    #construct the new point
    point = xk + alpha * dk
    #break down the new point dimension-wise
    x = point.item(0)
    y = point.item(1)
    slope = thisGrad( x, y )
    #take the dot product of the gradient and the direction of interest dk
    dotprod = slope.item(0) * dk.item(0) + slope.item(1) * dk.item(1)
    return dotprod

#this is the linear function by which sufficient decrease is measured.
#that is, a point occuring *beneath* this line has decreased sufficiently
#INPUTS
## xi is the initial position
## xk is the current position
## alpha is the distance from xi
## dk is the direction of movement
## c1 is the wolfe coefficient
#OUTPUTS the value on this line at distance alpha from xi along direction dk
def elFunction( xk, alpha, dk, c1 ):
    point = phiFunction(xk, 0, dk)
    slope = gradPhi(xk, 0, dk)
    newPoint = point + c1 * slope * alpha
    return newPoint

#this is a boolean-valued function to determine sufficient decrease from the initial position
#INPUTS
## xi is the initial position
## c1 is the wolfe coefficient
## alpha is the distance from xi
## xk is the current position
## dk is the direction of movement
def sufficientDecrease( xk, c1, alpha, dk ):
    term1 = phiFunction(xk, alpha, dk)
    infoprint("phi(alpha) is " + str(term1))
    term2 = elFunction(xk, alpha, dk, c1)
    myprint(term1)
    myprint(term2)
    return ( term1 <= term2 )

#this is a boolean-valued function to determine sufficient progress from the initial position
#this function implements the Strong Wolfe condition by comparing *magnitudes*
#INPUTS
## xi is the initial position
## c2 is the wolfe coefficient
## alpha is the distance from xi
## xk is the current position
## dk is the direction of movement
def sufficientProgress( xi, c2, alpha, dk ):
    term1 = gradPhi(xi, alpha, dk)
    infoprint("phiPrime(alpha) is " + str(term1))
    term2 = (c2 * gradPhi(xi, 0, dk))

    if( strongWolfe ):
        term1 = abs(term1)
        term2 = abs(term2)

    myprint(term1)
    myprint(term2)
    return ( term1 <= term2 ) 

#this is a boolean-valued function to reperesent a stopping condition
#returns true when both sufficientDecrease and sufficientProgress returns true.
#prints explanatory values when a verbose mode is on.
def isStopSatisfied( xi, c1, c2, alpha, dk ):
    if( sufficientDecrease( xi, c1, alpha, dk ) ):
        infoprint("Sufficient Decrease was satisfied.")
        if( sufficientProgress( xi, c2, alpha, dk ) ):
            infoprint("Sufficient Progress was satisfied.")
            #both conditions were met, so we break out and call the algorithm finished
            return True
        else:
            infoprint("Sufficient Progress was NOT satisifed.")
            return False
    else:
        infoprint("Sufficient Decrease was NOT satisfied.")
        if( sufficientProgress( xi, c2, alpha, dk ) ):
            infoprint("Sufficient Progress was satisfied.")
        else:
            infoprint("Sufficient Progress was NOT satisfied.")
        return False

#this is a boolean-valued function to represent a stopping condition
#return true (stop!) when the length of the gradient vector is equal to or less than 0.2
def isGradientSmall( xi ):
    threshold = 0.2
    grad = thisGrad( xi.item(0), xi.item(1) )
    transposeGrad = np.transpose( grad )
    gradientMag = math.sqrt( (grad * transposeGrad) )
    myprint( str(gradientMag) )
    if( gradientMag <= threshold ):
        infoprint("We stop because the gradient magnitude ( " + str(gradientMag) + " ) is smaller than " + str( threshold ) )
        return True
    else:
        return False

#=====BEGIN GOLDEN SEARCH FUNCTIONS


#this is the golden line search using point and direction
#INPUTS
## xi is the initial point
## dk is the direction by which to search
## c1 is the first Wolfe coefficient
## c2 is the second Wolfe coefficient
## alphaMax is the upper distance bound from the initial point
#OUTPUTS the minimizing point as an n-dimensional matrix
#NOTE: assume direction is normalized
def goldenDirectionalSearch( xi, dk, c1, c2, alphaMax ):

    #assert lower bound
    x0 = xi.item(0)
    y0 = xi.item(1)
    a = np.matrix( (x0, y0) )

    #assert upper bound
    xf = x0 + dk.item(0) * alphaMax
    yf = y0 + dk.item(1) * alphaMax
    b = np.matrix( (xf, yf) )

    #assert iteration counter
    i = 0
    while( True ):
        
        global lowLevelIterations 
        lowLevelIterations += 1

        infoprint("This is iteration " + str(i))
        myprint("a is " + str(a))
        myprint("b is " + str(b))
        
        #calculate distance "alpha" from the initial position xi
        alpha = ndist(xi, a) + ndist(a, b)/2.0
        infoprint("alpha is " + str(alpha))

        #check the stopping conditions
        if( isStopSatisfied( xi, c1, c2, alpha, dk ) ):
            break;

        #calculate middle points
        c = b - dk * ndist(a, b)/phi
        cx = c.item(0)
        cy = c.item(1)
        d = a + dk * ndist(a, b)/phi
        dx = d.item(0)
        dy = d.item(1)

        myprint("c is " + str(c))
        myprint("d is " + str(d))

        #evaluate the function at these middle points
        fc = thisFunction( cx, cy )
        myprint("fc is " + str(fc))
        fd = thisFunction( dx, dy )
        myprint("fd is " + str(fd))

        #decide how to adjust the interval
        if( fc < fd ):
            b = d
            myprint("replace b")
        else:
            a = c
            myprint("replace a")

        i += 1
        infoprint("\n")

    #return the middle point of the final interval
    final = a + ndist(a,b)/2.0 * dk
    return final 

#END GOLDEN SECTION DIRECTIONAL SEARCH

#===== BEGIN STEEPEST DESCENT ALGORITHM
#assert intial conditions
Xi = np.matrix( (inputX, inputY) )
Di = (-1) * thisGrad( Xi.item(0), Xi.item(1) )
condition1 = inputC1
condition2 = inputC2
aMax = inputAlphaMax

counter = 0;

#output variable
lowLevelIterations = 0

while( True ):
    counter += 1
    infoprint("\nfx is " + str( thisFunction(Xi.item(0), Xi.item(1) ) ) )
    
    #choose direction (negative gradient)
    Di = (-1) * thisGrad( Xi.item(0), Xi.item(1) )
    myprint("di is " + str(Di))
    #normalize the direction
    origin = np.matrix( (0, 0) )
    magDi = ndist(origin, Di)
    Di = Di / magDi
    myprint("norm di is " + str(Di))

    #perform line search
    Xi = goldenDirectionalSearch(Xi, Di, condition1, condition2, aMax )
    infoprint( "Golden Search yields Xi = " + str(Xi) )

    myprint("Xi is")
    myprint( str(Xi) )

    #maybe exit
    if( isGradientSmall( Xi ) ):
        break;
print "After " + str(counter) + " iterations,"
print "The minimum point was calculated to be " + str(Xi) + "."
print "The function value here is " + str(thisFunction(Xi.item(0), Xi.item(1))) + "."
print "It took " + str(lowLevelIterations) + " low-level iterations."





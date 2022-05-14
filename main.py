# Long winded way of getting a 8x8x8 matrix
mat = []
for i in range(8):
    mat.append([])
    for j in range(8):
        mat[i].append([])
        for k in range(8):
            mat[i][j].append(0)

def senseToPos(gyroX, gyroY, gyroZ, accX, accY, accZ, matIn):
    """
    Here we have a few jobs. We need to take the values from the gyroaccelerometer
    and put them into a vector field that represents movement of the positions of
    the LEDs.
    
    Note: 
        Python happens to be kind of slow and thus in this case it might not be
        the best language to use in this case but this is more of a proof of concept
        at this point

    Args:
        gyroX (float): Gyroscopes angular velocity about the x axis
        gyroY (float): Gyroscopes angular velocity about the y axis
        gyroZ (float): Gyroscopes angular velocity about the x axis
        accX (float): Accelerometer acceleration in the x direction
        accY (float): Accelerometer acceleration in the x direction
        accZ (float): Accelerometer acceleration in the x direction
        matIn (list): 1D array of positions of the LEDs (each value 
        is a float that represents its position) - actually the other
        option here is to say we have lets say 196 LEDs on at any given
        point we can say that we have a 2D array, where the first dims
        index represents the LED, the second dim represents XYZ on that
        LED

    Returns:
        list: 3D array of positions that have LEDs
    """
    
    # The other option here is to store a linear 1D array of 512 float values that are manipulated by 
    # our vector field and then from there we just round the number and thats what we use for the light
    # position while being able to keep the accuracy when we move around (between time instances)
    
    # Things we need to take into account are: Bounce, that being off walls, collisions with each other,
    # gravity...
        
    
    matrix = mat
    return matrix



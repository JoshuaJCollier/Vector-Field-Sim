# Vector-Field-Sim
Code to produce water simulation in LED cube gyroaccelerometer input

Goal here is to take inputs from a gyroaccelerometer, push that into a vector field, and integrate again to get a position field which will be pushed to the LEDs. We also take into account the acceleration in each direction which will help move the particles. 

We do need to manipulate the values of the acceleration by the angles because we are moving the cube with the acelerometer and thus if we say have it sideways, a motion in the downwards direction should cause all of the particles to move respectively to the side with respect to the absolute orientation of the cube. We also ned to account for the constant acceleration downwards due to gravity of the particles. Angles can be used to move the particles around as well as direction the accelerometer directions.

We will represent everything in probably an acceleration field, a vector field and a position field. We will change the acceleration field explicitly based on the inputs from the sensor, this being the accelerations which are manipulated based on the angle of the cube which is calculated with angular velocities and time, this produces absolute angles and therefore we can just use trig to get the changed values of acceleration. From here we integrate it to get the velocity field, 
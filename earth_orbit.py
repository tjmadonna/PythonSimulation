#Simulation of the Earth orbiting the Sun

from visual import *

G = 6.67e-11

# Create the sun
sun = sphere(pos=(0,0,0), radius=696e6, color=color.yellow, mass=333000 * 5.97e24)
sun.velocity = vector(0, 0, 0)

# Create the Earth
earth = sphere(pos=(0,0,149.6e9), radius=696e6, color=color.green, mass=5.97e24, make_trail=True, interval=10, retain=5000)
earth.velocity = vector(30e3, 0, 0)

# Acceleration of an object due to gravitational force
def gravitationalAcceleration(obj1, obj2):
	rVector = obj1.pos - obj2.pos
	acc = -((G * obj2.mass) / rVector.mag2 )
	acc *= rVector.norm()
	return acc

dt = 100

while True:
    rate(1e50)
    
    # Update the Earth's velocity
    earth.velocity += gravitationalAcceleration(earth, sun) * dt

    # Update the Earth's position
    earth.pos += earth.velocity * dt


# Import libraries
import turtle as tu

# Specify the number of digits in the Pi number as lines
lines = 100_000

# Open the text file with Pi digits
with open("1_million_digits_of_pi.txt", "r") as f:
    pi = f.read()

# Set up the graphics properties of the visualisation
tu.mode('logo')
tu.tracer(False)
tu.screensize(1500, 1500, 'black')
tu.colormode(255)

# Run through the digits
for n in range(lines):
    # Make the color variable
    color = int(n/(lines/255))
    tu.pencolor(255, 255-color, color)
    # Make the digits integers
    zahl = int(pi[n])
    # Set up the different angles of rotation
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(2)
    # Update the graphics every 10.000 digits
    if n % 10_000 == 0:
        tu.update()

tu.done()
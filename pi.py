import turtle as tu

lines = 100_000

with open("1_million_digits_of_pi.txt", "r") as f:
    pi = f.read()

tu.mode('logo')
tu.tracer(False)
tu.screensize(1500, 1500, 'black')
tu.colormode(255)

for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255, 255-color, color)
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(2)
    if n % 10_000 == 0:
        tu.update()

tu.done()
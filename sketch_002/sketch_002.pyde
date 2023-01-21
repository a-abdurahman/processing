size(600, 600)
background(0, 0, 40)

radius = 50
x = 300
y = 300

ellipse(x, y, radius, radius)

ellipse(x - 45, y - 1 * radius, radius, radius)
ellipse(x + 1 * radius, y - 45, radius, radius)

ellipse(x + 45, y + 1 * radius, radius, radius)
ellipse(x - 1 * radius, y + 45, radius, radius)

ellipse(x - 1 * radius, y, radius, radius)
ellipse(x + 1 * radius, y, radius, radius)

ellipse(x, y + 1 * radius, radius, radius)
ellipse(x, y - 1 * radius, radius, radius)

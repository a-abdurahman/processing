size(600, 600)
background(0, 0, 40)

rs = 20
x = 300
y = 300

#центр
fill(255, 0, 0)
ellipse(x, y, 2 * rs, 2 * rs)

#верхний, нижний
fill(0, 255, 0)
ellipse(x, y - 1.6 * rs, rs, rs)
ellipse(x, y + 1.6 * rs, rs, rs)

#левый, правый
fill(0, 0, 255)
ellipse(x - 1.6 * rs, y, rs, rs)
ellipse(x + 1.6 * rs, y, rs, rs)

#нижний левый, нижний правый
fill(255, 255, 0)
ellipse(x - 1.1 * rs, y + 1.1 * rs, rs, rs)
ellipse(x + 1.1 * rs, y + 1.1 * rs, rs, rs)

#верхний левый, верхний правый
fill(255, 0, 255)
ellipse(x + 1.1 * rs, y - 1.1 * rs, rs, rs)
ellipse(x - 1.1 * rs, y - 1.1 * rs, rs, rs)

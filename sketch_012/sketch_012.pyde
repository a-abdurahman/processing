def setup():
    size(800, 500)


def draw():
    background(0, 0, 50)
    noFill()
    strokeWeight(20)
    stroke(180, 0, 80)
    arc(width / 2, height / 2, 200, 200, 0, map(second(), 0, 59, 0, 2 * PI))
    stroke(200, 200, 50)
    arc(width / 2, height / 2, 150, 150, 0, map(minute(), 0, 59, 0, 2 * PI))
    stroke(0, 130, 255)
    arc(width / 2, height / 2, 100, 100, 0, map(hour(), 0, 59, 0, 2 * PI))
    
    noStroke()
    strokeWeight(1)  
    fill(255, 0, 0)
    arc(width / 2, height / 2, 300, 300, second() / 2, 0.05 + second() / 2)

    for a_second in range (second() + 1):
        background(0, 0, 54)
        stroke(0, 100, 255)
        x = 100 * cos (a_second * PI / 30)
        y = 100 * sin (a_second * PI / 30)
        line(320,230, 320 + x, 230 + y)

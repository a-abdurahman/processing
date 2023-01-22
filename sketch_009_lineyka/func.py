

def cell():
    for i in range(40):
        stroke(180, 180, 180)
        line(0, 10 + i * 20, width, 10 + i * 20)
        line(20 + i * 20, 0, 20 + i * 20, height)

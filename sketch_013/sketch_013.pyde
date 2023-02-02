from func import *

def setup():
    size(600, 600)
    background(255)

step = 10
circle_scale = 60
step_h = 2
            
def draw():
    background(255)
    global step, circle_scale
    cell(step)
    coordinate(10)
    noFill()
    circle(width / 2, height / 2, circle_scale)
    
def mouseWheel(event):
    global step, circle_scale, step_h
    e = event.getCount()
    if 1 < step < width:
        step += e
        
    if 1 < circle_scale < height:
         circle_scale += e

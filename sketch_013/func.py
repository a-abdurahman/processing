

def cell(step):
    stroke(200)
    for i in range(height / step):
        line(0, step * i, width, step * i)
        
    for i in range(width / step):
        line(step * i, 0, step * i, height)
    stroke(1)
    
def coordinate(step, step_count = 2, step_h = 2):
    line(0, height / 2, width, height / 2)
    line(width / 2, 0, width / 2, height)
    for i in range(width / step + step_count):
        line(i * step * step_count, height / 2 - step_h, i * step * step_count, height / 2 + step_h)
        line(width / 2 - step_h, i * step * step_count, width / 2 + step_h, i * step * step_count)
    
    

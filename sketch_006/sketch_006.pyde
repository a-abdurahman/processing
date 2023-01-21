size(600, 400)
noStroke()
colorMode(HSB, 360)
for i in range(365): 
    for j in range(365): 
        fill(i, j, 360)
        arc(300,200,200,200, radians(i), radians(j))
    

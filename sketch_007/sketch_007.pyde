size(800, 500)

# for i in range(10):
#     if i < 8:
#         rect(10 + i * 60, 10, 50, 50)

# for i in range(10):
#     if i % 2 == 0:
#         rect(10 + i * 60, 10, 50, 50)

# a = 10

# if a < 9:
#     rect(400, 250, 50, 50)
# else:
#     ellipse(400, 250, 50, 50)

for i in range(13):
    for j in range (8):
        if i % 2 == 0:
            fill(int(random(0, 255)), int(random(0, 255)), int(random(0, 255)))
            rect(10 + i * 60, 10 + j * 60, 50, 50)
        else:
            fill(int(random(0, 255)), int(random(0, 255)), int(random(0, 255)))
            circle(35 + i * 60, 35 + j * 60, 50)
            

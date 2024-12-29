#Use colorgram to extract colors from given image

# import colorgram

# colors_from_img= colorgram.extract('spot_painting.jpg',88)
# colors=[]
# for color in colors_from_img:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     colors.append(new_color)
# print(colors)

colors= [(43, 94, 148), (178, 45, 76), (226, 207, 100), (208, 156, 88), (177, 168, 33), (139, 89, 62), (118, 177, 208), (200, 75, 123), (212, 129, 173), (227, 69, 49), (92, 102, 189), (130, 38, 64), (28, 142, 84), (48, 165, 118), (51, 55, 93), (124, 
217, 208), (116, 46, 35), (35, 184, 195), (230, 169, 188), (123, 187, 170), (176, 186, 220), (50, 49, 68), (153, 207, 217), (83, 43, 33), (239, 171, 158), 
(43, 76, 74), (212, 206, 37), (81, 37, 52), (32, 80, 88), (39, 63, 62)]

import turtle as t
from random import choice

kachua=t.Turtle()
kachua.hideturtle()
kachua.penup()
kachua.setx(-150)
kachua.sety(-150)
kachua.screen.colormode(255)

for rows in range(10):
    for columns in range(10):
        kachua.dot(20,choice(colors))
        kachua.forward(50)
    kachua.left(90)
    kachua.forward(50)
    kachua.right(90)
    kachua.back(500)


screen=t.Screen()
screen.exitonclick()



import colorgram

colors = colorgram.extract('image.jpg', 30)

color_tuple = []

for x in range(30):
    r = colors[x].rgb.r
    g = colors[x].rgb.g
    b = colors[x].rgb.b
    color_tuple.append((r, g, b))

print(color_tuple)

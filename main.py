from image_match.goldberg import ImageSignature

gis = ImageSignature()
img = []

for i in range(1, 10):
    img.append(gis.generate_signature('C:/Users/thsxo/Downloads/IMG_1987.JPG'))
    print("%d fin" % i)

distance = gis.normalized_distance(img[0], img[1])
print(distance)

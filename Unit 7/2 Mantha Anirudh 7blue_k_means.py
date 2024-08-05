from PIL import Image
import random
import math
import sys

def vector_quantization(image, number):
    #another way to do is same thing with 2 if statements
    #if 8 ... if 27
    #that is very inefficient to do, getting ^1/3 is much easier
    num_col = 256
    colors = num_col // int(math.pow(number, 1/3))
    image_store = image.load()
    width, height = image.size
    for i in range(width):
        for j in range(height):
            rgb = list(image_store[i,j])
            three = 3
            for k in range(three): rgb[k] = (rgb[k] // colors) * colors
            image_store[i,j] = tuple(rgb)
    # for i in range(width):
    #     for j in range(height):
    #         image_store[i, j] = tuple((c // colors) * colors for c in image_store[i, j])
    image.show()
    return image

def k_means(image, k):
    image_store = image.load()
    width, height = image.size
    #using lambda expression to minimize the creation of another method
    pixel = (0, 0, 0)
    compute_avg_mean = lambda mean: sum((pixel[i] - mean[i]) * (pixel[i] - mean[i]) for i in range(3))
    # Create a list of all the pixels in the image
    points = [image_store[x, y] for x in range(width) for y in range(height)]
    means = random.sample(points, k)
    while True:
        groups = []
        for i in range(k): groups.append([])
        for x in range(width):
            for y in range(height):
                pixel = image_store[x, y]
                #settingn the comparision to the lambda expression
                #first time using lambda, so there may be a more efficient way
                #this is best methodology I read up on
                closest_mean = min(means, key=compute_avg_mean)
                #maybe later take out compute_avg_mean and insert with new lambda??
                groups[means.index(closest_mean)].append(pixel)
        checker = []
        for g in groups:
            store = []
            for i in range(3):
                sumk = 0
                countk = 0
                for p in g:
                    sumk += p[i]
                    countk += 1
                store.append(int(sumk / countk))
            checker.append(tuple(store))

        if checker == means: break
        means = checker
    new_means = []
    for i in means:
        new_tuple = tuple(map(int, i))
        new_means.append(new_tuple)
    means = new_means
    for x in range(width):
        for y in range(height):
            pixel = image_store[x, y]
            #same lambda comparision as before
            closest_mean = min(means, key=compute_avg_mean)
            image_store[x, y] = closest_mean
    return image

#timing is cutting very close to 2 minutes ...

path, k = sys.argv[1:]
k = int(k)
img = Image.open(path)
#image = vector_quantization(img, k)
image = k_means(img, k)

#image.show()
image.save("kmeansout.png")


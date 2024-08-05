from PIL import Image
import random
import math
from collections import defaultdict
#code doesnt work without this
#very wack
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

def k_mean_faster(image, k):
    image_store = image.load()
    width, height = image.size

    # Create a dictionary to store pixel frequencies
    pixel_frequencies = defaultdict(int)
    for x in range(width):
        for y in range(height):
            pixel = image_store[x, y]
            pixel_frequencies[pixel] += 1

    # Convert the dictionary to a list of pixels
    points = list(pixel_frequencies.keys())

    # Initialize k random means
    means = random.sample(points, k)

    # Using lambda expression to minimize the creation of another method
    compute_avg_mean = lambda mean: sum((pixel[i] - mean[i]) ** 2 for i in range(3))

    while True:
        groups = [[] for _ in range(k)]

        for x in range(width):
            for y in range(height):
                pixel = image_store[x, y]
                closest_mean = min(means, key=compute_avg_mean)
                groups[means.index(closest_mean)].append(pixel)

        checker = []

        for g in groups:
            store = []
            for i in range(3):
                sumk = 0
                countk = 0
                for p in g:
                    sumk += p[i] * pixel_frequencies[p]
                    countk += pixel_frequencies[p]
                store.append(int(sumk / countk))
            checker.append(tuple(store))

        if checker == means:
            break

        means = checker

    # Update the image pixels with the closest means
    for x in range(width):
        for y in range(height):
            pixel = image_store[x, y]
            closest_mean = min(means, key=compute_avg_mean)
            image_store[x, y] = closest_mean

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


def returnpointonimage(image):
    width, height = image.size; image_store = image.load()
    point = [image_store[x, y] for x in range(width) for y in range(height)]; pointz = set(point); points = list(pointz)
    def sum_of_values(point):return point[0] + point[1] + point[2]
    points.sort(key=sum_of_values)
    return points


def bottomthing(image, k):
    width, height = image.size; image_store = image.load()
    point = [image_store[x, y] for x in range(width) for y in range(height)]; pointz = set(point); points = list(pointz)
    def sum_of_values(point): return point[0] + point[1] + point[2]
    points.sort(key=sum_of_values)
    pwidth = width // k; retimage = Image.new("RGB", (width, height + pwidth))
    newp = retimage.load()
    for i in range(width):
        for j in range(height): newp[i, j] = image_store[i, j]
    for i in range(k):
        for j in range(pwidth):
            for y in range(pwidth): newp[i * pwidth + j, y + height] = points[i]
    return retimage, points


def fs_dithering(image, palette):
    width, height = image.size;
    image_store = image.load()

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):
            temp_p = image_store[x, y]
            temp_min = 0
            temp_err = 1000000000000000000
            for i, j in enumerate(palette):
                temp_val = (temp_p[0] - j[0]) ** 2 + (temp_p[1] - j[1]) ** 2 + (temp_p[2] - j[2]) ** 2
                if temp_val < temp_err: temp_min = i; temp_err = temp_val

            new_p = palette[temp_min]
            image_store[x, y] = new_p
            #error = [tuple(temp_p[0] - new_p[0]), tuple(temp_p[1] - new_p[1]), tuple(temp_p[2] - new_p[2])]
            error = tuple(temp_p[i] - new_p[i] for i in range(len(new_p)))

            # Floyd-Steinberg matrix
            for i, j, w in ((1, 0, 7 / 16), (-1, 1, 3 / 16), (0, 1, 5 / 16), (1, 1, 1 / 16)):
                nx, ny = x + i, y + j
                if 0 <= nx < width:
                    if 0 <= ny < height:
                        new_p = list(int(image_store[nx, ny][i] + error[i] * w) for i in range(len(new_p)))
                        image_store[nx, ny] = tuple(new_p)
    return image


path, k = sys.argv[1:]
k = int(k)
img = Image.open(path)
img = k_mean_faster(img, k)
palette = returnpointonimage(img)

image = fs_dithering(Image.open(path), list(palette))
image = bottomthing(img, k)[0]
image.save("kmeansout.png")

#http://cs.wellesley.edu/~pmetaxas/ei99.pdf
#https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering


# import cv2 as cv
from PIL import Image


# from matplotlib import pyplot as plt


def pixelated():
    img = Image.open("D:\\Desktop\\claudio-schwarz-_FsiDUMyAJg-unsplash.jpg")
    block_size = 50
    width, height = img.size
    img_array = img.load()
    # print(img_array[200, 500])
    # cordinate = x, y = 150, 59
    # print(img.getpixel(cordinate))
    max_width = width + block_size
    max_height = height + block_size
    # x and y are the index of the end point(the point of bottom right corner of the area  of each pixel block
    # The reason is to add a additional loop to deal with the possible "Incomplete part"
    for x in range(block_size - 1, max_width, block_size):
        for y in range(block_size - 1, max_height, block_size):
            if x == max_width - max_width % block_size - 1:
                x = width - 1
            if y == max_height - max_height % block_size - 1:
                y = height - 1
            refill(x, y, block_size, img_array)
            y += block_size
        x += block_size

    img.save("D:\\Desktop\\refill.png")


def refill(x, y, block_size, img_array):
    color_dict = {}
    block_pixel_list = []
    # Record the coordinates of each pixel in each block
    for pixel_x in range(-block_size + 1, 1):
        for pixel_y in range(-block_size + 1, 1):
            block_pixel_list.append([x + pixel_x, y + pixel_y])
    # Record the color dictionary of each block(pixel information and number)
    for pixel in block_pixel_list:
        if not str(img_array[pixel[0], pixel[1]]) in color_dict.keys():
            color_dict[str(img_array[pixel[0], pixel[1]])] = 1
        else:
            color_dict[str(img_array[pixel[0], pixel[1]])] += 1
    # Invert the keys and values of original dictionary will be easier to use it later
    temp_dict = {v: k for k, v in color_dict.items()}
    # Find the main color of the block
    main_color = temp_dict[max(color_dict.values())]
    for pixel in block_pixel_list:
        img_array[pixel[0], pixel[1]] = tuple(list(map(int, main_color[1:len(main_color) - 1].split(","))))


if __name__ == "__main__":
    pixelated()

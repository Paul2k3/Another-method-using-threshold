import cv2
import numpy as np
import math

image = cv2.imread('watermarked.bmp')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)



prime = 0

ext = np.empty((512, 512, 1), np.uint8)

threshold = 5000
for i in range(512):
    for j in range(512):
        ext[i][j] = 0


for i in range(64):
    if (prime == 3):
        break
    for j in range(64):
        average = 0
        for k in range(8):
            for m in range(8):
                average += image[i * 8 + k][j * 8 + m]
        variation = 0
        average = average / 64
        if (prime == 0):
            for k in range(8):
                for m in range(8):
                    if(image[8 * i + k][8 * j + k] > average):
                        variation += (image[8 * i + k][8 * j + k] - average) ** 2
                    else:
                        variation += (average - image[8 * i + k][8 * j + k]) ** 2
            variation = variation / 64
            if (variation > threshold):
                for k in range(8):
                    for m in range(8):
                        ext[i * 8 + k][j * 8 + m] = image[i * 8 + k][j * 8 + m]  % 2
                prime = prime + 1
                print(i * 8, j * 8)
        elif (prime == 1):
            for k in range(8):
                for m in range(8):
                    if(image[8 * i + k][8 * j + k] > average):
                        variation += (image[8 * i + k][8 * j + k] - average) ** 2
                    else:
                        variation += (average - image[8 * i + k][8 * j + k]) ** 2
            variation = variation / 64
            if (variation > threshold):
                for k in range(8):
                    for m in range(8):
                        ext[i * 8 + k][j * 8 + m] = image[i * 8 + k][j * 8 + m]  % 2
                prime = prime + 1
                print(i * 8, j * 8)
        elif(prime == 2):
            for k in range(8):
                for m in range(8):
                    if(image[8 * i + k][8 * j + k] > average):
                        variation += (image[8 * i + k][8 * j + k] - average) ** 2
                    else:
                        variation += (average - image[8 * i + k][8 * j + k]) ** 2
            variation = variation / 64
            if (variation > threshold):
                for k in range(8):
                    for m in range(8):
                        ext[i * 8 + k][j * 8 + m] = image[i * 8 + k][j * 8 + m]  % 2
                prime = prime + 1
                print(i * 8, j * 8)
        if (prime == 3):
            break


for i in range(512):
    for j in range(512):
        ext[i][j] = ext[i][j] * 255


cv2.imshow('few', ext)

cv2.imwrite('watermark.bmp', ext)

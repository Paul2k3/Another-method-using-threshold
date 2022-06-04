import cv2
import numpy as np
import math

image = cv2.imread('gray.bmp')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
fortest = cv2.imread('gray.bmp')
fortest = cv2.cvtColor(fortest,cv2.COLOR_BGR2GRAY)


prime = 0

sample = np.empty((512, 512, 1), np.uint8)

threshold = 5000
for i in range(512):
    for j in range(512):
        sample[i][j] = 0


for i in range(64):
    if (prime == 3):
        break
    for j in range(64):
        average = 0
        variance = 0
        for k in range(8):
            for m in range(8):
                if(fortest[i * 8 + k][j * 8 + m] % 2 == 1):
                    fortest[i * 8 + k][j * 8 + m] = fortest[i * 8 + k][j * 8 + m] - 1
        if (prime == 0):
            fortest[8 * i + 1][8 * j + 1] += 1
            fortest[8 * i + 1][8 * j + 6] += 1
            fortest[8 * i + 6][8 * j + 1] += 1
            fortest[8 * i + 6][8 * j + 6] += 1
            for k in range(8):
                for m in range(8):
                    average += fortest[i * 8 + k][j * 8 + m]
            average = average / 64
            for k in range(8):
                for m in range(8):
                    if(fortest[8 * i + k][8 * j + k] > average):
                        variance += (fortest[8 * i + k][8 * j + k] - average) ** 2
                    else:
                        variance += (average - fortest[8 * i + k][8 * j + k]) ** 2
            variance = variance / 64
            if (variance > threshold):
                for k in range(8):
                    for m in range(8):
                        image[i * 8 + k][j * 8 + m] = fortest[i * 8 + k][j * 8 + m]  
                sample[8 * i + 1][8 * j + 1] = 255
                sample[8 * i + 1][8 * j + 6] = 255
                sample[8 * i + 6][8 * j + 1] = 255
                sample[8 * i + 6][8 * j + 6] = 255
                prime = prime + 1
                print(i * 8, j * 8)
        elif (prime == 1):
            fortest[8 * i + 1][8 * j + 1] += 1
            fortest[8 * i + 1][8 * j + 6] += 1
            fortest[8 * i + 6][8 * j + 1] += 1
            fortest[8 * i + 6][8 * j + 6] += 1
            fortest[8 * i + 2][8 * j + 2] += 1
            fortest[8 * i + 2][8 * j + 5] += 1
            fortest[8 * i + 5][8 * j + 2] += 1
            fortest[8 * i + 5][8 * j + 5] += 1
            for k in range(8):
                for m in range(8):
                    average += fortest[i * 8 + k][j * 8 + m]
            average = average / 64
            for k in range(8):
                for m in range(8):
                    if(fortest[8 * i + k][8 * j + k] > average):
                        variance += (fortest[8 * i + k][8 * j + k] - average) ** 2
                    else:
                        variance += (average - fortest[8 * i + k][8 * j + k]) ** 2
            variance = variance / 64
            if (variance > threshold):
                for k in range(8):
                    for m in range(8):
                        image[i * 8 + k][j * 8 + m] = fortest[i * 8 + k][j * 8 + m]
                sample[8 * i + 1][8 * j + 1] = 255
                sample[8 * i + 1][8 * j + 6] = 255
                sample[8 * i + 6][8 * j + 1] = 255
                sample[8 * i + 6][8 * j + 6] = 255
                sample[8 * i + 2][8 * j + 2] = 255
                sample[8 * i + 2][8 * j + 5] = 255
                sample[8 * i + 5][8 * j + 2] = 255
                sample[8 * i + 5][8 * j + 5] = 255
                prime += 1
                print(i * 8, j * 8)
            
        elif(prime == 2):
            fortest[8 * i + 1][8 * j + 1] += 1
            fortest[8 * i + 1][8 * j + 6] += 1
            fortest[8 * i + 6][8 * j + 1] += 1
            fortest[8 * i + 6][8 * j + 6] += 1
            fortest[8 * i + 2][8 * j + 2] += 1
            fortest[8 * i + 2][8 * j + 5] += 1
            fortest[8 * i + 5][8 * j + 2] += 1
            fortest[8 * i + 5][8 * j + 5] += 1
            fortest[8 * i + 3][8 * j + 3] += 1
            fortest[8 * i + 3][8 * j + 4] += 1
            fortest[8 * i + 4][8 * j + 3] += 1
            fortest[8 * i + 4][8 * j + 4] += 1
            for k in range(8):
                for m in range(8):
                    average += fortest[i * 8 + k][j * 8 + m]
            average = average / 64
            for k in range(8):
                for m in range(8):
                    if(fortest[8 * i + k][8 * j + k] > average):
                        variance += (fortest[8 * i + k][8 * j + k] - average) ** 2
                    else:
                        variance += (average - fortest[8 * i + k][8 * j + k]) ** 2
            variance = variance / 64
            if (variance > threshold):
                for k in range(8):
                    for m in range(8):
                        image[i * 8 + k][j * 8 + m] = fortest[i * 8 + k][j * 8 + m]
                sample[8 * i + 1][8 * j + 1] = 255
                sample[8 * i + 1][8 * j + 6] = 255
                sample[8 * i + 6][8 * j + 1] = 255
                sample[8 * i + 6][8 * j + 6] = 255
                sample[8 * i + 2][8 * j + 2] = 255
                sample[8 * i + 2][8 * j + 5] = 255
                sample[8 * i + 5][8 * j + 2] = 255
                sample[8 * i + 5][8 * j + 5] = 255
                sample[8 * i + 3][8 * j + 3] = 255
                sample[8 * i + 3][8 * j + 4] = 255
                sample[8 * i + 4][8 * j + 3] = 255
                sample[8 * i + 4][8 * j + 4] = 255
                prime = prime + 1
                print(i * 8, j * 8)
        if (prime == 3):
            break

                
cv2.imshow('few', sample)
cv2.imwrite('watermarksholdbe(threshold = 5000).bmp', sample)
cv2.imwrite('watermarked.bmp', image)

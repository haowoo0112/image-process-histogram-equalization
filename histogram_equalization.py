import cv2
import numpy as np
import matplotlib.pyplot as plt

class histogram_equalization:
    """histogram equalization operation

    Attributes:
        image: original image
        image_r: how many rows in original image
        image_c: how many colums in original image
        q0: the lowest value in the result image
        qk: the highest value in the result image
        h: the histogram of original image
        q: the equation of tranformation
        result: the result of histogram equalization
    """
    def __init__(self, image):
        """read a photo, set q0 and qk value and show the histogram"""
        self.image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        self.image_r, self.image_c = self.image.shape
        self.qo = 0
        self.qk = 255
        self.show_histogram(self.image)
        cv2.imwrite('input.jpg', self.image)

    def histogram(self):
        """generate the histogram of original image"""
        self.h = np.zeros(256)
        for i in range(self.image_r):
            for j in range(self.image_c):
                self.h[self.image[i][j]] = self.h[self.image[i][j]] + 1
        
    def equalization(self):
        """histogram equalization"""
        self.result = np.zeros(shape = (self.image_r, self.image_c))
        coe = (self.qk - self.qo) / (self.image_r*self.image_c) # coe = (qk-q0)/N^2

        self.q = np.zeros(256)
        self.q[0] = self.qo
        self.q[1] = coe*(self.h[0] + self.h[1]) + self.qo
        for i in range(2, 256):
            self.q[i] = self.q[i-1] + coe * self.h[i]  # q[i] = q[i-1]+coe*h[i]
        
        for i in range(self.image_r):
            for j in range(self.image_c):
                self.result[i][j] = self.q[self.image[i][j]]

        self.show_histogram(self.result)
        self.save_image()

    def show_histogram(self, image):
        """show histogram"""
        plt.hist(image.ravel(),256,[0,256]); 
        plt.show()

    def save_image(self):
        """output image"""
        cv2.imwrite('output.jpg', self.result)

if __name__ == "__main__":
    Histogram_Equalization = histogram_equalization("input.jpg")
    Histogram_Equalization.histogram()
    Histogram_Equalization.equalization()
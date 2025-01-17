import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class ImageProcessor():

    @staticmethod
    def load(path):
        img = mpimg.imread(path)
        s = img.shape
        print("Loading image of dimensions " + str(s(0)) + " x " + str(s(1)))
        return np.array(img)

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    IP = ImageProcessor()
    imp = IP.load("42AI.png")
    print(imp)
    imp = 1 - imp
    IP.display(imp)

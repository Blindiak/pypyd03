import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class ImageProcessor():

    def load(self, path):
        img = mpimg.imread(path)
        print("Loading image of dimensions " + str(len(img)) + " x "
              + str(len(img[0])))
        return np.array(img)

    def display(self, array):
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    IP = ImageProcessor()
    imp = IP.load("42AI.png")
    print(imp)
    imp = 1 - imp
    IP.display(imp)

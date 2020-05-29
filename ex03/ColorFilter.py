import numpy as np


class ColorFilter:
    @staticmethod
    def invert(a):
        return 1 - a

    @staticmethod
    def to_blue(a):
        s = a.shape
        z = np.zeros(s)
        for x in range(s[0]):
            for y in range(s[1]):
                z[x][y][2] = a[x][y][2]
        return z

    @staticmethod
    def to_green(a):
        return a * [0.0, 1.0, 0.0]

    @staticmethod
    def to_red(a):
        b = ColorFilter.to_blue(a)
        g = ColorFilter.to_green(a)
        r = a - b - g
        return r

    @staticmethod
    def celluloid(a, g=5):
        ls = np.linspace(0, 1, g)
        s = a.shape
        for x in range(s[0]):
            for y in range(s[1]):
                for z in range(3):
                    for i in range(g):
                        if a[x][y][z] < ls[i]:
                            a[x][y][z] = ls[i]
                            break
        return a

    @staticmethod
    def to_grayscale(a, f):
        s = a.shape
        if f == 'w' or f == 'weighted':
            g = [0.299, 0.587, 0.114]
            for x in range(s[0]):
                for y in range(s[1]):
                    a[x][y] = (a[x][y] * g).sum()
            return a
        if f == 'm' or f == 'mean':
            for x in range(s[0]):
                for y in range(s[1]):
                    a[x][y] = a[x][y].sum() / 3
            return a


if __name__ == "__main__":
    from ImageProcessor import ImageProcessor

    cf = ColorFilter()
    IP = ImageProcessor()
    img = IP.load("elon.png")
    IP.display(img)

    img_i = cf.invert(img)
    IP.display(img_i)

    img_g = cf.to_green(img)
    IP.display(img_g)

    img_r = cf.to_red(img)
    IP.display(img_r)

    img_b = cf.to_blue(img)
    IP.display(img_b)

    img_cl = cf.celluloid(img)
    IP.display(img_cl)

    img_w = cf.to_grayscale(img, 'w')
    IP.display(img_w)

    img_w2 = cf.to_grayscale(img, 'w')
    IP.display(img_w2)

import numpy as np


class ScrapBooker():
    def crop(self, arr, dimensions, position=(0, 0)):
        if (arr.shape[0] < (dimensions[0] + position[0]) or
                arr.shape[1] < (dimensions[1] + position[1])):
            print("Error bad size")
            raise ValueError("bad size")
        a = arr[position[0]:dimensions[0] + position[0],
                position[1]:dimensions[1] + position[1]]
        return np.array(a)

    def thin(self, arr, n, axis):
        s = arr.shape
        if axis == 0:
            size = s[0]
        else:
            size = s[1]
        r = range(n - 1, size, n)
        arr = np.delete(arr, r, axis)
        return arr

    def juxtapose(self, arr, n, axis):
        r = [arr for i in range(n)]
        return np.concatenate(r, axis)

    def mosaic(self, arr, dimension):
        sb = ScrapBooker()
        arr = sb.juxtapose(arr, dimension[0], 1)
        arr = sb.juxtapose(arr, dimension[1], 0)
        return arr


if __name__ == "__main__":
    sb = ScrapBooker()
    a = np.random.rand(4, 4)
    print(a, '\n')
    a = sb.crop(a, (2, 2))
    print(a, '\n')
    a = sb.juxtapose(a, 3, 1)
    print(a, '\n')
    a = sb.thin(a, 3, 1)
    print(a, '\n')
    a = sb.crop(a, (1, 1))
    print(a, '\n')
    a = sb.mosaic(a, (2, 3))
    print(a, '\n')

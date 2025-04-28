import matplotlib.pyplot as plt
import numpy as np


def flood_fill(picture, x_coord, y_coord):
    if x_coord < 0 or x_coord >= picture.shape[1] or y_coord < 0 or y_coord >= picture.shape[0]:
        return picture
    elif picture[y_coord, x_coord] == 0 or picture[y_coord, x_coord] == 2:
        return picture
    elif picture[y_coord, x_coord] == 1:
        picture[y_coord, x_coord] = 2
        flood_fill(picture, x_coord + 1, y_coord)
        flood_fill(picture, x_coord - 1, y_coord)
        flood_fill(picture, x_coord, y_coord + 1)
        flood_fill(picture, x_coord, y_coord - 1)
        return picture






def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()

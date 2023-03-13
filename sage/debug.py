import numpy as np
import cv2, click

def imshow(x):
    cv2.imshow("image", x)
    cv2.waitKey(0)

def debug(key, value):
    if type(value) in [np.array, np.ndarray, np.matrix]:
        print(f'{click.style(key, fg="green")} type={type(value)} shape={value.shape} dtype={value.dtype} min={value.min()} max={value.max()}')
        print(value)
    else:
        print(f'{click.style(key, fg="yellow")} = {value} {type(value)}')

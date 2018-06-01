import numpy as np
import pyscreenshot as ImageGrab
import cv2
import time
import pyautogui


def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked


def process_image(original_image):
    original_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    original_image = cv2.Canny(original_image, threshold1=200, threshold2=300)
    vertices = np.array([[10, 500], [10, 300], [300, 200], [
                        500, 200], [800, 300], [800, 500]])
    original_image = roi(original_image, [vertices])
    return original_image


def main():
    last = time.time()
    while(True):
        printscreen_pil = ImageGrab.grab(bbox=(160, 300, 800, 600))
        new_image = process_image(np.array(printscreen_pil))

        print('Velocity frame: {}'.format(time.time(), -last))
        last = time.time()

        # pyautogui.keyDown('space')
        # pyautogui.keyUp('space')

        cv2.imshow('window', new_image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()

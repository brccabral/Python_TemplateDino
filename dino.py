from time import time

import cv2
from templateplay import TemplatePlay


def main():
    region = (1113, 118, 1725, 350)  # X1, Y1, X2, Y2

    tp = TemplatePlay()

    template_images = tp.load_templates("assets")
    # tp.init_control_gui()
    # HMin = 0
    # SMin = 0
    # VMin = 153

    # HMax = 0
    # SMax = 0
    # VMax = 172

    # SAdd = 0
    # SSub = 255
    # VAdd = 0
    # VSub = 0

    tp.hsv_filter["HMin"] = 0
    tp.hsv_filter["SMin"] = 0
    tp.hsv_filter["VMin"] = 153
    tp.hsv_filter["HMax"] = 0
    tp.hsv_filter["SMax"] = 0
    tp.hsv_filter["VMax"] = 172
    tp.hsv_filter["SAdd"] = 0
    tp.hsv_filter["SSub"] = 255
    tp.hsv_filter["VAdd"] = 0
    tp.hsv_filter["VSub"] = 0

    loop_time = time()
    while tp.running:
        screen = tp.window.screenshot(region)
        processed = tp.apply_hsv_filter(screen)
        cv2.imshow("Processed", processed)
        template_positions = tp.find_templates(screen, template_images)
        screen = tp.draw_rectangles(screen, template_positions)

        print(f"FPS {1/(time()-loop_time):.2f}")
        loop_time = time()


if __name__ == "__main__":
    main()

import cv2
import templateplay as tp

region = (960, 150, 1850, 350)  # X1, Y1, X2, Y2

template_images = tp.load_templates("assets")
window_capture = tp.WindowCapture()

count = 0
while tp.running:
    screen = window_capture.screenshot(region)
    template_positions = tp.find_templates(screen, template_images)
    tp.show(screen, template_positions)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        tp.running = False

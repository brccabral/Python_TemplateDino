import templateplay as tp

region = (960, 150, 1920, 350)  # X1, Y1, X2, Y2

template_images = tp.load_templates("assets")
window_capture = tp.WindowCapture()

count = 0
while tp.running:
    screen = window_capture.screenshot(region)
    template_positions = tp.find_templates(screen, template_images)
    tp.show(screen, template_positions)
    count += 1
    print(count)
    if count >= 20:
        tp.running = False

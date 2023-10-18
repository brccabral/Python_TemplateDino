import templateplay as tp

region = (10, 10, 300, 200)

template_images = tp.load("assets")

count = 0
while tp.running:
    screen = tp.screenshot(region)
    template_positions = tp.find_templates(screen, template_images)
    tp.show(screen, template_positions)
    count += 1
    if count >= 2:
        tp.running = False

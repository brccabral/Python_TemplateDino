import templateplay as tp

region = (960, 150, 960, 200)

template_images = tp.load_templates("assets")

count = 0
while tp.running:
    screen = tp.screenshot(region)
    template_positions = tp.find_templates(screen, template_images)
    tp.show(screen, template_positions)
    count += 1
    print(count)
    if count >= 20:
        tp.running = False

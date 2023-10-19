from templateplay import TemplatePlay

region = (1113, 118, 1725, 350)  # X1, Y1, X2, Y2

tp = TemplatePlay()

template_images = tp.load_templates("assets")

count = 0
while tp.running:
    screen = tp.window.screenshot(region)
    template_positions = tp.find_templates(screen, template_images)
    screen = tp.draw_rectangles(screen, template_positions)

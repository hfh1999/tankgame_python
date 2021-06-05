from pygame import display


# some bug
class Display:
    def __init__(self):
        pass

    def init(self):
        display.init()

    def quit(self):
        display.quit()

    def get_init(self):
        return display.get_init()

    def set_mode(self, size=(0, 0), flags=0, depth=0, display=0, vsync=0):
        display.set_mode(size, flags, depth, display, vsync)

    def get_surf(self):
        return display.get_surface()

    def flip(self):
        display.flip()

    def update(self):
        display.update()

    def get_driver(self):
        return display.get_driver()

    def get_wm_info(self):
        return display.get_wm_info()

    def list_modes(self):
        return display.list_modes()

    def mode_ok(self, size, flags=0, depth=0, display=0):
        display.mode_ok(size, flags, depth, display)

    def gl_get_attribute(self, flag):
        return display.gl_get_attribute(flag)

    def gl_set_attribute(self, flag, value):
        display.gl_set_attribute(flag, value)

    def get_active(self):
        return display.get_active()

    def iconify(self):
        return display.iconify()

    def toggle_fullscreen(self):
        return display.toggle_fullscreen()

    def set_gamma(self, red, green=None, blue=None):
        return display.set_gamma(red, green, blue)

    def set_gamma_ramp(self, red, green, blue):
        return display.set_gamma_ramp(red, green, blue)

    def set_icon(self, Surface):
        display.set_icon(Surface)

    def set_caption(self, title, icontitle=None):
        display.set_caption(title, icontitle)

    def get_caption(self):
        return display.get_caption()

    def set_palette(self, palette=None):
        display.set_palette(palette)

    def get_num_displays(self):
        return display.get_num_displays()

    def get_window_size(self):
        return display.get_window_size()

    def get_allow_screensaver(self):
        return display.get_allow_screensaver()

    def set_allow_screensaver(self, value):
        display.set_allow_screensaver(value)


GameDisplay = Display()

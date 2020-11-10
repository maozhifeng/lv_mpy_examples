#!/opt/bin/lv_micropython
# change the above to the path of your lv_micropython unix binary
#
import time
#
# initialize lvgl
#
import lvgl as lv
import init_gui
from lv_colors import *

LV_USE_GAUGE=1
style = lv.style_t()
style.init()

# Set a background color and a radius
style.set_radius(lv.STATE.DEFAULT, 5)
style.set_bg_opa(lv.STATE.DEFAULT, lv.OPA.COVER)
style.set_bg_color(lv.STATE.DEFAULT, LV_COLOR_SILVER)

# Set some paddings
style.set_pad_inner(lv.STATE.DEFAULT, 20)
style.set_pad_top(lv.STATE.DEFAULT, 20)
style.set_pad_left(lv.STATE.DEFAULT, 5)
style.set_pad_right(lv.STATE.DEFAULT, 5)

style.set_scale_end_color(lv.STATE.DEFAULT, LV_COLOR_RED)
style.set_line_color(lv.STATE.DEFAULT, LV_COLOR_WHITE)
style.set_scale_grad_color(lv.STATE.DEFAULT, LV_COLOR_BLUE)
style.set_line_width(lv.STATE.DEFAULT, 2)
style.set_scale_end_line_width(lv.STATE.DEFAULT, 4)
style.set_scale_end_border_width(lv.STATE.DEFAULT, 4)

# Gauge has a needle but for simplicity its style is not initialized here
if LV_USE_GAUGE:
    # Create an object with the new style*/
    obj = lv.gauge(lv.scr_act(), None)
    obj.add_style(lv.gauge.PART.MAIN, style)
    obj.align(None, lv.ALIGN.CENTER, 0, 0)

while True:
     lv.task_handler()
     time.sleep_ms(10)
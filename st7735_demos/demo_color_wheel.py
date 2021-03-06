#!//opt/bin/lv_micropython
import lvgl as lv
import init_gui
from utime import sleep
from math import sin,cos,pi
from lv_colors import LV_COLOR_MAKE

CANVAS_WIDTH  = 240
CANVAS_HEIGHT = 240

HALF_WIDTH = CANVAS_WIDTH // 2
HALF_HEIGHT = CANVAS_HEIGHT // 2 
CENTER_X = CANVAS_WIDTH // 2 -1
CENTER_Y = CANVAS_HEIGHT // 2 -1
ANGLE_STEP_SIZE = 0.05  # Decrease step size for higher resolution
PI2 = pi * 2

def clear():
    canvas.fill_bg(lv_colors.BLACK, lv.OPA.COVER)
    
def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB (based on colorsys.py).

        Args:
            h (float): Hue 0 to 1.
            s (float): Saturation 0 to 1.
            v (float): Value 0 to 1 (Brightness).
    """
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6

    v = int(v * 255)
    t = int(t * 255)
    p = int(p * 255)
    q = int(q * 255)

    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

def draw_filledCircle(canvas, x0, y0, r, color):
    """Draw a filled circle.
    
    Args:
       x0 (int): X coordinate of center point.
       y0 (int): Y coordinate of center point.
       r (int): Radius.
       color (int): RGB565 color value.
    """
    p1=lv.point_t()
    p2=lv.point_t()
    point_array=[p1,p2]
    
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.color = color;
    line_dsc.opa = lv.OPA.COVER
    
    f = 1 - r
    dx = 1
    dy = -r - r
    x = 0
    y = r
    p1.x = x0
    p1.y = y0 - r
    p2.x = p1.x
    p2.y = p1.y + 2 * r + 1
    canvas.draw_line(point_array,2, line_dsc)
    while x < y:
        if f >= 0:
            y -= 1
            dy += 2
            f += dy
        x += 1
        dx += 2
        f += dx
        p1.x = x0 + x
        p1.y = y0 - y
        p2.x = p1.x
        p2.y = p1.y +  2 * y + 1
        canvas.draw_line(point_array,2,line_dsc)
        p1.x = x0 - x
        p2.x = p1.x
        canvas.draw_line(point_array,2,line_dsc)
        p1.x = x0 - y
        p1.y = y0 - x
        p2.x = p1.x
        p2.y = p1.y + 2 * x + 1
        canvas.draw_line(point_array,2,line_dsc)
        p1.x = x0 + y
        p2.x = p1.x
        canvas.draw_line(point_array,2,line_dsc)
        
def test():
    """Test code."""
    cbuf=bytearray(CANVAS_WIDTH * CANVAS_HEIGHT * 4)
    # create a canvas
    canvas = lv.canvas(lv.scr_act(),None)
    canvas.set_buffer(cbuf,CANVAS_WIDTH,CANVAS_HEIGHT,lv.img.CF.TRUE_COLOR)
    canvas.align(None,lv.ALIGN.CENTER,0,0)
    
    p1=lv.point_t()
    p2=lv.point_t()
    point_array=[p1,p2]
    
    p2.x = CENTER_X
    p2.y = CENTER_Y
    line_dsc = lv.draw_line_dsc_t()
    line_dsc.init()
    line_dsc.opa = lv.OPA.COVER
    x, y = 0, 0
    angle = 0.0
    
    #  Loop all angles from 0 to 2 * PI radians
    while angle < PI2:
        # Calculate x, y from a vector with known length and angle
        x = int(CENTER_X * sin(angle) + HALF_WIDTH)
        y = int(CENTER_Y * cos(angle) + HALF_HEIGHT)
        color = LV_COLOR_MAKE(*hsv_to_rgb(angle / PI2, 1, 1))
        line_dsc.color = color;
        p1.x = x
        p1.y = y
        canvas.draw_line(point_array,2, line_dsc)
        angle += ANGLE_STEP_SIZE

    sleep(5)
    '''
    clear()
    for r in range(CENTER_X, 0, -1):
        color = color565(*hsv_to_rgb(r / HALF_WIDTH, 1, 1))
        display.draw_filledCircle(CENTER_X, CENTER_Y, r, color)
    sleep(9)
    '''

test()

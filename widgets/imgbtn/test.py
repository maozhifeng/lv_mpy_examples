#!/opt/ucc/micros/esp32/lilygo-ttgo-twatch-2020-micropython/ports/unix/micropython-dev
# init
import time
import lvgl as lv

lv.init()


class driver:
    def init_gui_SDL(self):

        import SDL

        SDL.init()

        # Register SDL display driver.

        disp_buf1 = lv.disp_buf_t()
        buf1_1 = bytearray(480*10)
        disp_buf1.init(buf1_1, None, len(buf1_1) // lv.color_t.SIZE)
        disp_drv = lv.disp_drv_t()
        disp_drv.init()
        disp_drv.buffer = disp_buf1
        disp_drv.flush_cb = SDL.monitor_flush
        disp_drv.hor_res = 480
        disp_drv.ver_res = 320
        disp_drv.register()

        # Register SDL mouse driver

        indev_drv = lv.indev_drv_t()
        indev_drv.init()
        indev_drv.type = lv.INDEV_TYPE.POINTER
        indev_drv.read_cb = SDL.mouse_read
        indev_drv.register()
        
    def init_gui_esp32(self):

        import lvesp32
        import ILI9341 as ili

        # Initialize ILI9341 display

        disp = ili.display(miso=5, mosi=18, clk=19, cs=13, dc=12, rst=4, backlight=2)
        disp.init()

        # Register display driver

        disp_buf1 = lv.disp_buf_t()
        buf1_1 = bytearray(480*10)
        disp_buf1.init(buf1_1, None, len(buf1_1) // lv.color_t.SIZE)
        disp_drv = lv.disp_drv_t()
        disp_drv.init()
        disp_drv.buffer = disp_buf1
        disp_drv.flush_cb = disp.flush
        disp_drv.hor_res = 240
        disp_drv.ver_res = 320
        disp_drv.register()

        # Register raw resistive touch driver

        import rtch

        touch = rtch.touch(xp=32, yp=33, xm=25, ym=26, touch_rail=27, touch_sense=33)
        touch.init()
        indev_drv = lv.indev_drv_t()
        indev_drv.init()
        indev_drv.type = lv.INDEV_TYPE.POINTER
        indev_drv.read_cb = touch.read
        indev_drv.register()

    def init_gui_stm32(self):
        import rk043fn48h as lcd
        import lvstm32

        hres = 480
        vres = 272

        # Register display driver
        tick = lvstm32.lvstm32()
        lcd.init(w=hres, h=vres)
        disp_buf1 = lv.disp_buf_t()
        buf1_1 = lcd.framebuffer(1)
        buf1_2 = lcd.framebuffer(2)
        disp_buf1.init(buf1_1, buf1_2, len(buf1_1) // lv.color_t.SIZE)
        disp_drv = lv.disp_drv_t()
        disp_drv.init()
        disp_drv.buffer = disp_buf1
        disp_drv.flush_cb = lcd.flush
        disp_drv.gpu_blend_cb = lcd.gpu_blend
        disp_drv.gpu_fill_cb = lcd.gpu_fill
        disp_drv.hor_res = hres
        disp_drv.ver_res = vres
        disp_drv.register()

        # Register touch sensor
        indev_drv = lv.indev_drv_t()
        indev_drv.init()
        indev_drv.type = lv.INDEV_TYPE.POINTER
        indev_drv.read_cb = lcd.ts_read
        indev_drv.register()

    def init_gui(self):

        # Identify platform and initialize it

        try:
            self.init_gui_esp32()
        except ImportError:
            pass

        try:
            self.init_gui_SDL()
        except ImportError:
            pass

        try:
            self.init_gui_stm32()
        except ImportError:
            pass


drv = driver()
drv.init_gui()

# Image data

with open('blue_flower_32.bin','rb') as f:
    img_data = f.read()

# Create a screen with a draggable image

scr = lv.obj()
img = lv.img(scr)
img.align(scr, lv.ALIGN.CENTER, 0, 0)
img_dsc = lv.img_dsc_t(
    {
        "header": {"always_zero": 0, "w": 100, "h": 75, "cf": lv.img.CF.TRUE_COLOR_ALPHA},
        "data_size": len(img_data),
        "data": img_data,
    }
)

img.set_src(img_dsc)
img.set_drag(True)
print("Image size: ",img_dsc.data_size)
# Load the screen and display image

lv.scr_load(scr)
while True:
    lv.task_handler()
    time.sleep(5)

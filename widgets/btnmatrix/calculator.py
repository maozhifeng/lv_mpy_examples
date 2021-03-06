#!/opt/bin/lv_micropython
import time
import lvgl as lv
import init_gui

def event_handler(source,evt):
    if evt == lv.EVENT.VALUE_CHANGED:
        print("Toggled")
        txt = source.get_active_btn_text()
        print("%s was pressed"%txt)


btnm_map = ["7","8", "9", "/", " ","\n",
            "4", "5", "6", "x", "bsp", "\n",
            "1", "2", "3","+","=","\n",
            "c","0",".","-"," ",""]

btnm_ctlr_map = [lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.HIDDEN,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.NO_REPEAT,
                 lv.btnmatrix.CTRL.HIDDEN]

# create a button matrix
btnm = lv.btnmatrix(lv.scr_act(),None)
btnm.set_map(btnm_map)
btnm.set_ctrl_map(btnm_ctlr_map)
btnm.set_width(226)
btnm.align(None,lv.ALIGN.CENTER,0,0)
# attach the callback
btnm.set_event_cb(event_handler)

while True:
    lv.task_handler()
    time.sleep_ms(5)

from mirela_sdk.image_processing.camera.oakd_cam import OakdCam
from tkinter import *
from tkinter import ttk
import threading
import cv2

class OakdInterface():

    def __init__(self, root: Tk, oakd: OakdCam):
        self.root = root
        self.oakd = oakd
        self.root_background = "#929ca9"
        self.font = ("Times New Roman", 11, "bold")
        self.set_screen_master()
        self.widgets()
        self.set_modes_combobox()

    def set_screen_master(self) -> None:

        self.root.configure(background = self.root_background)
        self.root.title("OAK-D Interface")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.maxsize(width = 600, height = 600)
        self.root.minsize(width=300, height = 300)

    def widgets(self) -> None:

        self.ajuste = 10
        self.initial_x = 30
        self.initial_y = 30 + self.ajuste
        self.pos_y = 0
        self.step = 35
        self.widgets_list = list()

        scale_ten = [OakdCam.BRIGHTNESS, OakdCam.CONTRAST, OakdCam.SATURATION]
        scale_four = [OakdCam.SHARPNESS, OakdCam.LUMA_DENOISE, OakdCam.CHROMA_DENOISE]
        
        self.generate_scale_widgets(scale_ten, (-10, 10), self.oakd.set_control)

        self.initial_x = 170
        self.initial_y = 30 + self.ajuste
        self.pos_y = 0
        self.generate_scale_widgets(scale_four, (0, 4), self.oakd.set_control)

        self.initial_x = 310
        self.initial_y = 100 + self.ajuste
        self.pos_y = 0
        self.generate_scale_widgets([OakdCam.AE_COMP], (-9, 9), self.oakd.set_control)

    def generate_scale_widgets(self, widgets: list, scale: tuple, func: callable) -> None:

        from_, to = scale

        for i in range(len(widgets)):
            
            self.label = Label(self.root, text = widgets[i].capitalize(), 
                               font = self.font, background = self.root_background, 
                               justify="left", anchor="w")
            self.label.place(x = self.initial_x, y = self.initial_y + self.pos_y, width = 115, height = 30)

            self.scale = Scale(self.root,
                               from_= from_, 
                               to=to, 
                               resolution=1, 
                               length=100, 
                               orient=HORIZONTAL, 
                               state=NORMAL, 
                               command = lambda value, widget = widgets[i]: func(widget, int(value)))
            self.widgets_list.append(self.scale)
            
            
            self.scale.place(x = self.initial_x, y = self.initial_y + self.pos_y + 25,
                             width=110, height=33)
            self.pos_y += 2*self.step

    def set_modes_combobox(self) -> None:
        
        initial_y = 250
        self.configure_combobox(self.oakd.EFFECT_MODE, "Effect Mode", self.oakd.effect_modes, 
                                initial_x = 30, initial_y = initial_y)
        self.configure_combobox(self.oakd.ANTI_BANDING_MODE, "Anti Banding", self.oakd.antband_modes, 
                                initial_x = 140, initial_y = initial_y)
        self.configure_combobox(self.oakd.AWB_MODE, "Auto White Balance", self.oakd.awb_modes,
                                initial_x = 250, initial_y = initial_y)
        self.configure_combobox(self.oakd.AUTOFOCUS, "Auto Focus", self.oakd.aut_foc_modes, 
                                initial_x = 360, initial_y = initial_y)
        

    def configure_combobox(self, 
                           mode_type: str, 
                           control: str, 
                           dictionary: dict, 
                           initial_x: int, 
                           initial_y: int) -> None:

        mode = "OFF"
        mode_label = Label(self.root, text = control, font = self.font,
                                       justify = "left", anchor = "w", background = self.root_background)
        mode_label.place(x = initial_x, y = initial_y, width = 90, height = 30)

        dict_modes = dictionary
        modes = [name for name, _ in dict_modes.items() if name.isupper()]

        combobox = ttk.Combobox(
            self.root,
            values = modes,
            width=10,
            justify="center",
            style="TCombobox",
            
        )
        combobox.place(x = initial_x, y = initial_y + 25, width = 100, height = 20)
        combobox.set(mode)
        okay_mode_button = Button(self.root, text = "Ok", 
                                  command = lambda :self.oakd.set_control(mode_type,
                                                                    mode = dict_modes.get(combobox.get())))
        
        okay_mode_button.place(x = initial_x + 25, y = initial_y + 50, width = 50, height = 20)


def call_interface(oakd: OakdCam):
    root = Tk()
    interface = OakdInterface(root, oakd)
    mainloop()


def main():

    oakd = OakdCam()
    oakd.setup_camera(1)

    call_interface(oakd)
    # oakd.init_cam()

    # queue = oakd.getQueue_CamType()
    # thread_interface = threading.Thread(target=lambda :call_interface(oakd))

    # key = -1

    # while key & 0xFF != ord("q"):

    #     frame = oakd.getFrame(queue)
    #     key = cv2.waitKey(1)

    #     if key & 0xFF == ord("i"): thread_interface.start()

    #     cv2.imshow("Oakd", frame)

    # oakd.clean()
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
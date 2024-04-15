import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style
from ControlUnit import ControlUnit
import time


def background_app(cud, cu):
    pm = cu.get_pm()
    htp = cu.get_htp()

    cud.set_pm10(pm[1])
    cud.set_pm2p5(pm[0])

    cud.set_t(htp[0])
    cud.set_p(htp[2])
    cud.set_h(htp[1])

    cud.set_gps("Non2")
    App.after(500, background_app, cud, cu)


class CU_Data:
    def __init__(self):
        self.pm10 = 0
        self.pm2p5 = 0
        self.t = 0
        self.p = 0
        self.h = 0
        self.gps = 0

    def get_pm10(self):
        return self.pm10

    def get_pm2p5(self):
        return self.pm2p5

    def get_t(self):
        return self.t

    def get_p(self):
        return self.p

    def get_h(self):
        return self.h

    def get_gps(self):
        return self.gps

    def set_pm10(self, p):
        self.pm10 = p

    def set_pm2p5(self, p):
        self.pm2p5 = p

    def set_t(self, p):
        self.t = p

    def set_p(self, p):
        self.p = p

    def set_h(self, p):
        self.h = p

    def set_gps(self, p):
        self.gps = p


class MainWindowApp(ttk.Frame):
    def __init__(self, container, cud):
        super().__init__(container)
        Style(theme='darkly')
        row_index = 0
        self.counter = 0
        self.cud = cud
        self.pm10 = 0
        self.pm2p5 = 0
        self.t = 0
        self.p = 0
        self.h = 0
        self.gps = 0

        self.image = Image.open('assets/loghino.drawio7.drawio.png')
        self.python_image = ImageTk.PhotoImage(self.image)

        self.rowconfigure(0, weight=3)
        self.img_label = ttk.Label(self, image=self.python_image, )
        self.img_label.grid(column=0, row=row_index, columnspan=10, sticky="nsew")

        row_index += 1
        self.pm_entry = ttk.Label(self, text="-- PARTICLE MATTER --")
        self.pm_entry.grid(column=0, row=row_index, columnspan=10, sticky='w')

        row_index += 1
        self.labelframe_pm10 = ttk.LabelFrame(self, text="PM10 [ppm]", labelanchor="nw")
        self.labelframe_pm10.grid(column=1, row=row_index, columnspan=3, sticky="nsew")

        self.labelframe_pm2p5 = ttk.LabelFrame(self, text="PM2.5  [ppm]", labelanchor="nw")
        self.labelframe_pm2p5.grid(column=6, row=row_index, columnspan=3, sticky="nsew")

        self.label_pm10 = ttk.Label(self.labelframe_pm10, text=self.pm10)
        self.label_pm10.pack(padx=10, pady=10)

        self.label_pm2p5 = ttk.Label(self.labelframe_pm2p5, text=self.pm2p5)
        self.label_pm2p5.pack(padx=10, pady=10)

        row_index += 1

        self.pm_entry = ttk.Label(self, text="-- ENVIRONMENT --")
        self.pm_entry.grid(column=0, row=row_index, columnspan=10, sticky='w')

        row_index += 1
        self.labelframe_T = ttk.LabelFrame(self, text="T [°C]", labelanchor="nw")
        self.labelframe_T.grid(column=1, row=row_index, columnspan=2, sticky="nsew")

        self.labelframe_P = ttk.LabelFrame(self, text="P [Pa]", labelanchor="nw")
        self.labelframe_P.grid(column=4, row=row_index, columnspan=2, sticky="nsew")

        self.labelframe_H = ttk.LabelFrame(self, text="H  [%]", labelanchor="nw")
        self.labelframe_H.grid(column=7, row=row_index, columnspan=2, sticky="nsew")

        self.label_t = ttk.Label(self.labelframe_T, text=self.t)
        self.label_t.pack(padx=10, pady=10)

        self.label_p = ttk.Label(self.labelframe_P, text=self.p)
        self.label_p.pack(padx=10, pady=10)

        self.label_h = ttk.Label(self.labelframe_H, text=self.h)
        self.label_h.pack(padx=10, pady=10)

        row_index += 1
        self.pm_entry = ttk.Label(self, text="-- GPS --")
        self.pm_entry.grid(column=0, row=row_index, columnspan=10, sticky="nsew")

        row_index += 1
        self.labelframe_latlon = ttk.LabelFrame(self, text="GPS  [Lat/Lon]", labelanchor="nw", borderwidth=5)
        self.labelframe_latlon.grid(column=1, row=row_index, columnspan=8, sticky="nsew")

        self.label_gps = ttk.Label(self.labelframe_latlon, text=self.gps)
        self.label_gps.pack(padx=10, pady=10)
        self.update()

    def update(self):
        self.label_pm10.configure(text=self.cud.get_pm10())
        self.label_pm2p5.configure(text=self.cud.get_pm2p5())

        self.label_t.configure(text=self.cud.get_t())
        self.label_p.configure(text=self.cud.get_p())
        self.label_h.configure(text=self.cud.get_h())

        self.label_gps.configure(text=self.cud.get_gps())

        self.after(1000, self.update)


class Window(tk.Tk):
    def __init__(self, cud, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # self.after(0, background_app)
        self.wm_title("Test Application")
        self.geometry("617x684")
        f = MainWindowApp(self, cud)
        f.grid(column=0, row=0)


if __name__ == "__main__":
    cud = CU_Data()
    cu = ControlUnit("192.168.1.5")

    App = Window(cud)
    App.after(1000, background_app, cud, cu)
    App.mainloop()

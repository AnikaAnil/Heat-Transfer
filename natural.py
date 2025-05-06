import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

class HeatTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEAT TRANSFER MADE FUN")
        self.step = 0

        self.title_label = tk.Label(root, text="Welcome to HEAT TRANSFER MADE FUN", font=("Arial", 20))
        self.title_label.pack(pady=20)

        self.text_display = tk.Label(root, text="", font=("Arial", 14), wraplength=600, justify="left")
        self.text_display.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_step)
        self.next_button.pack(pady=10)

        self.observations = {}

    def next_step(self):
        if self.step == 0:
            self.text_display.config(text="AIM:\nThe aim of the experiment is to determine the natural convection heat transfer coefficient of a vertical heated tube kept in air, experimentally and by using empirical correlation.")
        elif self.step == 1:
            self.text_display.config(text="SPECIFICATIONS:\nLength of the tube = 0.5 m\nDiameter of the tube = 0.05 m\nDuct size = 0.2 x 0.2 x 0.5 m")
        elif self.step == 2:
            self.text_display.config(text="THEORY:\nIn natural convection, fluid motion is caused by density differences due to temperature gradients.\nWhen the surface is hot, the fluid rises; when cold, the fluid sinks.\nThis creates a cycle that transfers heat from the surface to the air.")
            self.display_animation()
        elif self.step == 3:
            self.get_observations()
        elif self.step == 4:
            self.display_summary()
        self.step += 1

    def display_animation(self):
        img = Image.open("/mnt/data/natural_convection_demo.jpg")
        img = img.resize((400, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        panel = tk.Label(self.root, image=photo)
        panel.image = photo
        panel.pack()

    def get_observations(self):
        self.observations['time'] = simpledialog.askstring("Observation", "Enter the time of reading (e.g., 5 min):")
        for i in range(1, 8):
            t = simpledialog.askfloat("Temperature Reading", f"Enter surface temperature T{i} (in °C):")
            self.observations[f'T{i}'] = t
        self.observations['T_ambient'] = simpledialog.askfloat("Ambient Temperature", "Enter ambient temperature (in °C):")
        messagebox.showinfo("Observations Saved", "All observations recorded successfully!")

    def display_summary(self):
        summary = "OBSERVATIONS:\n"
        for key, value in self.observations.items():
            summary += f"{key}: {value}\n"
        self.text_display.config(text=summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = HeatTransferApp(root)
    root.mainloop()

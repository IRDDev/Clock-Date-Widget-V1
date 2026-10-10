import tkinter as tk
from datetime import datetime


# ============================================================
# CONFIGURATION
# Ubah pengaturan V1 langsung di bagian ini
# ============================================================

WIDTH = 220
HEIGHT = 80

POS_X = 100
POS_Y = 100

BG_COLOR = "#121212"
TEXT_COLOR = "#ffffff"

CLOCK_FONT = ("Segoe UI", 22, "bold")
DATE_FONT = ("Segoe UI", 11)

TRANSPARENCY = 0.85


# ============================================================
# APPLICATION
# ============================================================

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root

        self.init_window()

    # ========================================================
    # WINDOW
    # ========================================================

    def init_window(self):
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", TRANSPARENCY)

        self.root.config(bg=BG_COLOR)
        self.root.geometry(
            f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}"
        )

        # ====================================================
        # DRAG WINDOW
        # ====================================================

        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)

        # ====================================================
        # CLOCK
        # ====================================================

        self.lbl_clock = tk.Label(
            self.root,
            font=CLOCK_FONT,
            fg=TEXT_COLOR,
            bg=BG_COLOR
        )

        self.lbl_clock.pack(
            side="top",
            pady=(8, 0)
        )

        # ====================================================
        # DATE
        # ====================================================

        self.lbl_date = tk.Label(
            self.root,
            font=DATE_FONT,
            fg=TEXT_COLOR,
            bg=BG_COLOR
        )

        self.lbl_date.pack(
            side="top",
            pady=(0, 5)
        )

        # ====================================================
        # UPDATE
        # ====================================================

        self.update_data()

    # ========================================================
    # DRAG START
    # ========================================================

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    # ========================================================
    # DRAG WINDOW
    # ========================================================

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y

        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay

        self.root.geometry(f"+{x}+{y}")

    # ========================================================
    # CLOCK + DATE UPDATE
    # ========================================================

    def update_data(self):
        now = datetime.now()

        self.lbl_clock.config(
            text=now.strftime("%H:%M:%S")
        )

        self.lbl_date.config(
            text=now.strftime("%d-%m-%Y")
        )

        self.root.after(1000, self.update_data)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()

    app = SystemMonitorApp(root)

    root.mainloop()

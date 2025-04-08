import tkinter as tk
from threading import Thread
import time
import math
from pynput.mouse import Controller, Button

running = True
tracking_active = False
fullscreen = False
center_x, center_y = 0, 0
deadzone_size = 50  # Default dead zone size
view_cone_threshold = 200  # Used for visualization only
mouse_controller = Controller()
click_triggered = False

def track_movement(canvas, state_label, debug_readout):
    global tracking_active, running, center_x, center_y, deadzone_size, view_cone_threshold, click_triggered
    while running:
        if tracking_active:
            x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
            offset_x, offset_y = x - center_x, y - center_y

            canvas.delete("all")
            canvas.create_oval(
                center_x - deadzone_size, center_y - deadzone_size,
                center_x + deadzone_size, center_y + deadzone_size,
                outline="red", width=2
            )
            for angle in range(0, 360, 45):
                rad = math.radians(angle)
                end_x = center_x + view_cone_threshold * math.cos(rad)
                end_y = center_y - view_cone_threshold * math.sin(rad)
                canvas.create_line(center_x, center_y, end_x, end_y, fill="orange", width=1)
            canvas.create_line(center_x, center_y, x, y, fill="blue", width=2)
            canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="green", outline="green")

            # Check if the cursor is outside the deadzone
            if abs(offset_x) > deadzone_size or abs(offset_y) > deadzone_size:
                if not click_triggered:
                    mouse_controller.click(Button.left, 1)
                    click_triggered = True
                state_label.config(text="State: OUTSIDE")
            else:
                click_triggered = False
                state_label.config(text="State: INSIDE")

            debug_readout.delete(1.0, tk.END)
            debug_readout.insert(tk.END,
                f"Mouse Pos: ({x}, {y})\n"
                f"Offset: ({offset_x}, {offset_y})\n"
                f"Deadzone: {deadzone_size}px\n"
                f"View Cone: {view_cone_threshold}px\n"
            )
        time.sleep(0.05)

def toggle_fullscreen(root):
    global fullscreen, center_x, center_y
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    if not fullscreen:
        root.geometry("800x600")
    center_x, center_y = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2

def start_tracking():
    global tracking_active
    tracking_active = True

def stop_tracking():
    global tracking_active
    tracking_active = False

def quit_program(root):
    global running
    running = False
    root.destroy()

def adjust_deadzone(value):
    global deadzone_size
    deadzone_size = int(value)

def adjust_view_cone(value):
    global view_cone_threshold
    view_cone_threshold = int(value)

def create_gui():
    global center_x, center_y
    root = tk.Tk()
    root.title("CBOMC")
    root.geometry("800x600")
    root.configure(bg="black")
    center_x, center_y = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2

    tk.Label(root, text="(C.B.O.M.C) Click-Based Oriented Movement Control", 
             font=("Arial", 24, "bold"), fg="white", bg="black").pack(pady=10)

    state_label = tk.Label(root, text="State: INSIDE", font=("Arial", 16), fg="yellow", bg="black")
    state_label.pack(pady=10)

    control_frame = tk.Frame(root, bg="black")
    control_frame.pack()
    tk.Button(control_frame, text="START TRACKING", command=start_tracking,
              font=("Arial", 12), fg="white", bg="green", width=15).grid(row=0, column=0, padx=5)
    tk.Button(control_frame, text="STOP TRACKING", command=stop_tracking,
              font=("Arial", 12), fg="white", bg="red", width=15).grid(row=0, column=1, padx=5)
    tk.Button(control_frame, text="TOGGLE FULLSCREEN", command=lambda: toggle_fullscreen(root),
              font=("Arial", 12), fg="white", bg="blue", width=15).grid(row=0, column=2, padx=5)
    tk.Button(control_frame, text="QUIT", command=lambda: quit_program(root),
              font=("Arial", 12), fg="white", bg="gray", width=15).grid(row=0, column=3, padx=5)

    tk.Label(root, text="Deadzone Size", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
    slider_deadzone = tk.Scale(root, from_=1, to=800, orient="horizontal",
                               command=adjust_deadzone, bg="black", fg="white", troughcolor="gray")
    slider_deadzone.set(deadzone_size)
    slider_deadzone.pack()

    tk.Label(root, text="View Cone Threshold", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
    slider_view_cone = tk.Scale(root, from_=1, to=2000, orient="horizontal",
                                command=adjust_view_cone, bg="black", fg="white", troughcolor="gray")
    slider_view_cone.set(view_cone_threshold)
    slider_view_cone.pack()

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    debug_readout = tk.Text(root, height=4, width=30, bg="black", fg="white", font=("Arial", 10))
    debug_readout.place(x=10, y=10)

    Thread(target=track_movement, args=(canvas, state_label, debug_readout), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    create_gui()

import tkinter as tk
from threading import Thread
import time
import math

# Global variables
running = True
tracking_active = False
fullscreen = False
center_x, center_y = 0, 0
deadzone_size = 50  # Default dead zone size
view_cone_threshold = 200  # Default distance for pizza slice segments
current_direction = ""  # Current tracking direction

# Function to track mouse movement
def track_movement(canvas, direction_label, debug_readout):
    global tracking_active, running, center_x, center_y, deadzone_size, view_cone_threshold, current_direction
    while running:
        if tracking_active:
            # Get mouse position
            x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()

            # Calculate offset from the center
            offset_x, offset_y = x - center_x, y - center_y

            # Clear the canvas
            canvas.delete("all")

            # Draw the dead zone circle
            canvas.create_oval(
                center_x - deadzone_size, center_y - deadzone_size,
                center_x + deadzone_size, center_y + deadzone_size,
                outline="red", width=2
            )

            # Draw pizza slices (cross lines for 8-way movement)
            for angle in range(0, 360, 45):  # 8 segments, each 45 degrees apart
                rad = math.radians(angle)
                end_x = center_x + view_cone_threshold * math.cos(rad)
                end_y = center_y - view_cone_threshold * math.sin(rad)
                canvas.create_line(center_x, center_y, end_x, end_y, fill="orange", width=1)

            # Draw a line from the center to the cursor position
            canvas.create_line(center_x, center_y, x, y, fill="blue", width=2)

            # Draw the cursor position dot
            canvas.create_oval(
                x - 5, y - 5, x + 5, y + 5,
                fill="green", outline="green"
            )

            # Determine direction only if outside the dead zone
            direction = ""
            if abs(offset_x) > deadzone_size or abs(offset_y) > deadzone_size:
                angle = math.degrees(math.atan2(-offset_y, offset_x)) % 360
                if 337.5 <= angle or angle < 22.5:
                    direction = "D"  # Right
                elif 22.5 <= angle < 67.5:
                    direction = "WD"  # Up-Right
                elif 67.5 <= angle < 112.5:
                    direction = "W"  # Up
                elif 112.5 <= angle < 157.5:
                    direction = "WA"  # Up-Left
                elif 157.5 <= angle < 202.5:
                    direction = "A"  # Left
                elif 202.5 <= angle < 247.5:
                    direction = "SA"  # Down-Left
                elif 247.5 <= angle < 292.5:
                    direction = "S"  # Down
                elif 292.5 <= angle < 337.5:
                    direction = "SD"  # Down-Right

            # Update the direction label if the direction changes
            if direction and direction != current_direction:
                current_direction = direction
                direction_label.config(text=f"Direction: {current_direction}")

            # Update debug readout with current information
            debug_readout.delete(1.0, tk.END)
            debug_readout.insert(
                tk.END,
                f"Mouse Position: ({x}, {y})\n"
                f"Offset: ({offset_x}, {offset_y})\n"
                f"Direction: {current_direction}\n"
                f"Deadzone Size: {deadzone_size}px\n"
                f"View Cone Threshold: {view_cone_threshold}px\n"
            )

        time.sleep(0.05)  # Smooth tracking

# Function to toggle fullscreen
def toggle_fullscreen(root):
    global fullscreen, center_x, center_y
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    if not fullscreen:
        root.geometry("800x600")
    center_x, center_y = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2

# Function to start tracking
def start_tracking():
    global tracking_active
    tracking_active = True

# Function to stop tracking
def stop_tracking():
    global tracking_active
    tracking_active = False

# Function to quit the program
def quit_program(root):
    global running
    running = False
    root.destroy()

# Function to adjust the dead zone size
def adjust_deadzone(value):
    global deadzone_size
    deadzone_size = int(value)

# Function to adjust view cone threshold
def adjust_view_cone(value):
    global view_cone_threshold
    view_cone_threshold = int(value)

# Main GUI function
def create_gui():
    global center_x, center_y
    root = tk.Tk()
    root.title(" DMOML")
    root.geometry("800x600")
    root.configure(bg="black")

    # Calculate center coordinates
    center_x, center_y = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2

    # Big Logo
    tk.Label(
        root,
        text=" (D.M.O.M.L) By:Risk",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="black",
    ).pack(pady=10)

    # Live Tracking Result Label
    direction_label = tk.Label(
        root,
        text="Direction: None",
        font=("Arial", 16),
        fg="yellow",
        bg="black"
    )
    direction_label.pack(pady=10)

    # Control Buttons
    control_frame = tk.Frame(root, bg="black")
    control_frame.pack()

    tk.Button(
        control_frame,
        text="START TRACKING",
        command=start_tracking,
        font=("Arial", 12),
        fg="white",
        bg="green",
        width=15,
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        control_frame,
        text="STOP TRACKING",
        command=stop_tracking,
        font=("Arial", 12),
        fg="white",
        bg="red",
        width=15,
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        control_frame,
        text="TOGGLE FULLSCREEN",
        command=lambda: toggle_fullscreen(root),
        font=("Arial", 12),
        fg="white",
        bg="blue",
        width=15,
    ).grid(row=0, column=2, padx=5)

    tk.Button(
        control_frame,
        text="QUIT",
        command=lambda: quit_program(root),
        font=("Arial", 12),
        fg="white",
        bg="gray",
        width=15,
    ).grid(row=0, column=3, padx=5)

    # Deadzone Adjustment Slider
    tk.Label(
        root,
        text="Deadzone Size",
        font=("Arial", 12),
        fg="white",
        bg="black",
    ).pack(pady=10)

    slider_deadzone = tk.Scale(
        root,
        from_=1, to=800,
        orient="horizontal",
        command=adjust_deadzone,
        bg="black",
        fg="white",
        troughcolor="gray",
    )
    slider_deadzone.set(deadzone_size)
    slider_deadzone.pack()

    # View Cone Adjustment Slider
    tk.Label(
        root,
        text="View Cone Threshold",
        font=("Arial", 12),
        fg="white",
        bg="black",
    ).pack(pady=10)

    slider_view_cone = tk.Scale(
        root,
        from_=1, to=2000,
        orient="horizontal",
        command=adjust_view_cone,
        bg="black",
        fg="white",
        troughcolor="gray",
    )
    slider_view_cone.set(view_cone_threshold)
    slider_view_cone.pack()

    # Canvas for debug visuals
    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Mini Readout Display
    debug_readout = tk.Text(
        root, height=4, width=30, bg="black", fg="white", font=("Arial", 10)
    )
    debug_readout.place(x=10, y=10)  # Positioned at the top-left corner

    # Start the tracking thread
    Thread(target=track_movement, args=(canvas, direction_label, debug_readout), daemon=True).start()

    # Start the GUI loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()

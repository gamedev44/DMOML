# DMOML (Directional Mouse-Oriented Movement Lock) With the New (Optional) CBOMC (Click Based Oriented Movement Control)

DMOML is a Python-based utility designed by **Asterisk** to enhance directional movement in **top-down MOBAs** and similar games. It tracks mouse movement relative to the screen's center and maps this input to 8-way WASD controls, allowing for precise and intuitive gameplay.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Use DMOML](#how-to-use-dmoml)
- [Additional Script: CBOMC](#additional-script-cbomc)
- [Compatibility](#compatibility)
  - [DMOML Compatibility](#dmoml-compatibility)
  - [CBOMC Compatibility](#cbomc-compatibility)
- [Support and Contribution](#support-and-contribution)

---

## Features

- **Accurate Direction Detection**:  
  Divides the screen into 8 distinct "pizza slices" for accurate directional inputs, including diagonal movement.
  
- **Customizable Dead Zone**:  
  Adjust the inactive area around the center to suit your responsiveness preferences.

- **Dynamic View Cone Threshold**:  
  Fine-tune the sensitivity and range of the directional segments.

- **Real-Time Debug Visualization**:  
  Observe live mouse position, directional zones, and the current active slice.

- **Fullscreen Mode**:  
  Debug efficiently with an immersive fullscreen experience.

- **Game-Agnostic**:  
  Works with a variety of games requiring precise directional control.

---

## Requirements

- **Python 3.8 or higher**
- **Tkinter**: Typically included with Python installations.
- **pynput**: Required for input emulation. Install via:
  ```bash
  pip install pynput
  ```

---

## Installation

1. **Install Python**:  
   Download Python 3.8+ from [https://www.python.org/downloads/](https://www.python.org/downloads/) and ensure you select "Add Python to PATH" during installation.

2. **Clone or Download the Repository**:  
   Clone the repository via Git:
   ```
   git clone https://github.com/gamedev44/DMOML.git
   ```
   Or download the ZIP from the same GitHub repository.

3. **Install Dependencies**:  
   Open a terminal or command prompt and run:
   ```
   pip install pynput
   ```

4. **Run the Programs**:  
   Navigate to the script's directory and execute:
   - For directional WASD-based control:
     ```
     python DMOML.py
     ```
   - For point-and-click RTS/top-down control:
     ```
     python CBOMC.py
     ```

---

## How to Use DMOML

1. **Launch the Program**:  
   Open the DMOML script following the installation steps above.

2. **Customize Settings**:  
   - Adjust the **Dead Zone Size** slider to define the inactive area near the center.  
   - Use the **View Cone Threshold** slider to fine-tune the directional sensitivity.

3. **Start Tracking**:  
   Click **START TRACKING** to enable mouse-based directional movement.

4. **Use Fullscreen Mode**:  
   Toggle fullscreen for distraction-free debugging.

5. **Quit When Done**:  
   Stop tracking with **STOP TRACKING** or exit the program with **QUIT**.

---

## Additional Script: CBOMC

**CBOMC (Click-Based Oriented Movement Control)** is a new utility included in this repository for users who prefer point-and-click navigation for RTS and top-down games. Instead of emulating WASD keystrokes, CBOMC listens for mouse movement beyond a customizable dead zone and automatically triggers a left mouse click at that position.

- **Key Features**:
  - Monitors mouse movement relative to the screen center.
  - Activates a left click when the pointer exits the dead zone.
  - Shares similar customization settings as DMOML (dead zone size and view cone threshold).
  - Ideal for point-and-click RTS/top-down gameplay.

*Run CBOMC with:*
```
python CBOMC.py
```

---

## Compatibility

### DMOML Compatibility
DMOML is optimized for precise WASD-based directional control and works well with games such as:
- [Supervive](https://www.supervivegame.com/)
- [League of Legends (ARAM mode)](https://www.leagueoflegends.com/)
- [Battlerite](https://store.steampowered.com/app/504370/Battlerite/)
- [Heroes of the Storm](https://heroesofthestorm.com/)
- [Diablo III](https://diablo3.blizzard.com/)
- [Dota 2](https://store.steampowered.com/app/570/Dota_2/)

### CBOMC Compatibility
CBOMC is designed for point-and-click, top-down, and RTS style games. Some compatible titles include:
- [StarCraft II](https://starcraft2.com/en-us/) – A fast-paced RTS with a point-and-click interface.
- [Age of Empires II](https://www.ageofempires.com/games/aoeii/) – A classic RTS with intricate mouse-based controls.
- [Company of Heroes](https://www.companyofheroes.com/) – A tactical RTS that benefits from quick, precise clicking.
- [Command & Conquer: Red Alert 3](https://www.ea.com/games/command-and-conquer/command-and-conquer-red-alert-3) – Combines traditional RTS elements with point-and-click navigation.

---

## Support and Contribution

For bug reports, feature requests, or contributions, please visit the GitHub repository and submit an issue or pull request. Enhance your gameplay precision with DMOML and CBOMC, and enjoy intuitive, mouse-driven control!
```

# DMOML (Directional Mouse-Oriented Movement Lock)

DMOML is a Python-based utility designed by **Asterisk** to enhance directional movement in **top-down MOBAs** and similar games. It tracks mouse movement relative to the screen's center and maps this input to 8-way WASD controls, allowing for precise and intuitive gameplay.

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
- **pynput**: Required for WASD emulation. Install via:
  ```bash
  pip install pynput
  ```

---

## Installation

1. **Install Python**:  
   Download Python 3.8+ from [https://www.python.org/downloads/](https://www.python.org/downloads/) and ensure you select "Add Python to PATH" during installation.

2. **Clone or Download the Script**:  
   Clone the repository via Git:
   ```
   git clone https://github.com/gamedev44/DMOML.git
   ```
   Or download the ZIP from the same GitHub repository.

3. **Install Dependencies**:  
   Open a terminal or command prompt and run the following to install required libraries:
   ```
   pip install pynput
   ```

4. **Run the Program**:  
   Navigate to the script's directory and execute:
   ```
   python DMOML.py
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

## Compatibility

DMOML is ideal for **top-down MOBAs** or any game requiring precise WASD-based directional control. Examples include:

- [Supervive](https://www.supervivegame.com/)
- [League of Legends (ARAM mode)](https://www.leagueoflegends.com/)
- [Battlerite](https://store.steampowered.com/app/504370/Battlerite/)
- [Heroes of the Storm](https://heroesofthestorm.com/)
- [Diablo III](https://diablo3.blizzard.com/)
- [Dota 2](https://store.steampowered.com/app/570/Dota_2/)

---

## Support and Contribution

For bug reports, feature requests, or contributions, visit the GitHub repository and submit an issue or pull request. Enhance your gameplay precision with DMOML and enjoy intuitive, mouse-driven directional controls!
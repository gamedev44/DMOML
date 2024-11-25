# DMOML (Directional Mouse-Oriented Movement Lock)

DMOML is a Python-based tool designed by:Asterisk to enhance directional movement in **top-down MOBAs** and similar games. It provides a live, visualized movement system based on mouse position relative to the screen center, making 8-way directional controls more intuitive and responsive.

---

## Features

- **Precise Direction Detection**: 
  Splits the screen into 8 precise "pizza slices" for highly accurate 8-way and diagonal movement, ensuring seamless control.

- **Customizable Dead Zone**: 
  Adjust the inactive central area to match your preferred playstyle and responsiveness.

- **View Cone Threshold**: 
  Dynamically control the extent of the directional segments, keeping them equidistant and perfectly aligned for fine-tuned movement.

- **Live Debug Visualization**: 
  Access real-time debug data, including mouse position, directional lines, and the currently active slice.

- **Fullscreen Mode**: 
  Toggle fullscreen mode with ease for an immersive and distraction-free experience.

- **Works Across Games**: 
  Optimized for **Supervive** and other popular **top-down MOBAs**, enhancing gameplay precision.


---

## Requirements

- **Python 3.8 or higher**
- **Tkinter** (included with most Python installations)

---

## Installation Instructions

1. **Download Python**:  
   [Download Python](https://www.python.org/downloads/)  
   Ensure you check the box to **Add Python to PATH** during installation.

2. **Clone or Download the DMOML Script**:
   - **Clone the repository** using Git:
     ```bash
     git clone https://github.com/gamedev44/DMOML.git
     cd DMOML
     ```
   - **Or download the ZIP**:
     - Go to [https://github.com/gamedev44/DMOML](https://github.com/gamedev44/DMOML).
     - Click the green **Code** button and select **Download ZIP**.
     - Extract the ZIP file to a folder of your choice.


3. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the folder where the script is located.
   - Run the script with:
     ```bash
     python dmoml.py
     ```

---

## How to Use DMOML

1. **Start the Program**:
   - Launch the program using the steps above.
   - The GUI will open with a live visualization canvas and control sliders.

2. **Adjust the Settings**:
   - **Deadzone Size**: Use the slider to define the inactive central area where no directional input is triggered.
   - **View Cone Threshold**: Adjust the size of the directional slices to suit your gameplay.

3. **Begin Tracking**:
   - Click **START TRACKING** to enable mouse tracking.
   - Move the mouse to observe real-time directional updates and debug information.

4. **Fullscreen Mode**:
   - Toggle fullscreen mode with the **TOGGLE FULLSCREEN** button for a debugger with a distraction-free experience.

5. **Stop or Exit**:
   - Pause tracking with **STOP TRACKING**.
   - Quit the program with the **QUIT** button.

---

## Supported Games

DMOML was created to improve gameplay in **top-down MOBAs** and other games requiring precise directional movement. It is particularly useful for games that rely on **mouse-based movement and targeting**.

### Examples of Supported Games:
- **[Supervive](https://www.supervivegame.com/)**: A fast-paced competitive top-down MOBA.
- **[League of Legends](https://www.leagueoflegends.com/) (ARAM mode)**: Precise movement helps in tight situations.
- **[Battlerite](https://store.steampowered.com/app/504370/Battlerite/)**: Ideal for executing quick, accurate movements in team fights.
- **[Heroes of the Storm](https://heroesofthestorm.com/)**: Improve positioning and movement precision.
- **[Diablo III](https://diablo3.blizzard.com/)**: Enhance control for skill-based movement and dodging.
- **[Dota 2](https://store.steampowered.com/app/570/Dota_2/)**: Master movement and positioning in this globally popular MOBA.


---

## Links to Resources

1. **Download Python**:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Learn Python Basics**:  
   - [Official Python Tutorial](https://docs.python.org/3/tutorial/)
   - [W3Schools Python Tutorial](https://www.w3schools.com/python/)

3. **Links to Games this is Most Usefull With**:
   - [Supervive](https://www.supervivegame.com/)
   - [Battlerite](https://store.steampowered.com/app/504370/Battlerite/)
   - [League of Legends](https://www.leagueoflegends.com/)
   - [Heroes of the Storm](https://heroesofthestorm.com/)
   - [Diablo III](https://diablo3.blizzard.com/)
   - [Dota 2](https://store.steampowered.com/app/570/Dota_2/)


---

## Support and Contribution

If you encounter any issues, have feature requests, or want to contribute, please open an issue or submit a pull request on the GitHub repository.

Enjoy seamless directional control and improved gameplay with DMOML! Have Fun!!!

# DMOML (Directional Mouse-Oriented Movement Lock)

DMOML is a Python-based tool designed by:Asterisk to enhance directional movement in **top-down MOBAs** and similar games. It provides a live, visualized movement system based on mouse position relative to the screen center, making 8-way directional controls more intuitive and responsive.

---

## Features

- **Precise Direction Detection**: Splits the screen into 8 "pizza slices" for highly accurate 8-way and diagonal movement.
- **Customizable Dead Zone**: Adjust the inactive central area to suit your playstyle.
- **View Cone Threshold**: Dynamically control the extent of the directional segments for fine-tuned movement while keeping them equadistant from one another.
- **Live Debug Visualization**: View real-time debug data, including mouse position, directional lines, and active slice.
- **Fullscreen Mode**: Toggle fullscreen mode for a better gaming experience.
- **Works Across Games**: Designed for **Supervive** and other **top-down MOBAs**.

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
   - Clone the repository:
     ```bash
     git clone https://github.com/your-repository/dmoml.git
     cd dmoml
     ```
   - Or download the ZIP from GitHub and extract it.

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

---

## Links to Resources

1. **Download Python**:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Learn Python Basics**:  
   - [Official Python Tutorial](https://docs.python.org/3/tutorial/)
   - [W3Schools Python Tutorial](https://www.w3schools.com/python/)

3. **Games this tool is most useful for**:
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

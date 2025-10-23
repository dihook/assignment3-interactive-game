# 🚀 UFO Invasion - Interactive Shooting Game

## Assignment 3: Responding to the User
**Course:** SD5913 - Programming for Art and Design  
**Student:** Yu Wenlong  
**Date:** October 2025

---

## 📝 Project Description

**UFO Invasion** is an interactive arcade-style shooting game built with Python and Pygame. Players control a spaceship defending Earth from an increasingly aggressive alien invasion. The game features dynamic difficulty scaling, particle explosion effects, background music, and a comprehensive scoring system.

This project demonstrates interactive design principles by responding to multiple forms of user input (keyboard and mouse) and providing real-time visual and audio feedback.

---

## 🎮 How to Play

### Controls:
- **A** - Move left
- **D** - Move right  
- **SPACE** - Shoot bullets
- **Q** - Quit game
- **Mouse Click** - Start game (on start screen)

### Objective:
- Destroy as many UFOs as possible
- Avoid getting hit by UFO bullets
- Your score increases with each UFO destroyed (+5 points)
- UFO speed increases over time for added challenge
- Try to survive as long as possible and get a high score!

---

## ✨ Features

### User Interaction:
- **Keyboard Input:** Real-time movement and shooting controls
- **Mouse Input:** Interactive start screen with clickable button
- **Multiple Input Types:** Demonstrates varied user interaction methods

### Game Mechanics:
- **Dynamic Difficulty:** UFO spawn rate and movement speed increase over time
- **Collision Detection:** Bullets vs UFOs, UFO bullets vs player
- **State Management:** Start screen, game loop, game over states
- **Scoring System:** Real-time score tracking displayed on screen
- **Timer:** Live gameplay duration counter

### Visual Design:
- **Particle Effects:** Explosion animations when UFOs are destroyed
- **Fullscreen Display:** Immersive gaming experience
- **Custom Graphics:** Airplane and UFO sprite assets
- **Color-coded Elements:** Player bullets (red), UFO bullets (green)

### Audio:
- **Background Music:** Looping ambient soundtrack
- **Dynamic Volume Control:** Balanced audio levels (30%)

---

## 🛠️ Installation & Setup

### Prerequisites:
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/dihook/pfad.git
cd pfad/assignment2_interactive_game
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Assets
Ensure the following files are in the correct locations:
```
assignment2_interactive_game/
├── interactive_game.py
├── airplane.bmp
├── ufo.bmp
└── assets/
    └── background_music.wav/
        └── Audio_MainMenu.WAV
```

### Step 4: Run the Game
```bash
python interactive_game.py
```

---

## 📁 Project Structure

```
assignment2_interactive_game/
│
├── interactive_game.py          # Main game code
├── requirements.txt              # Python dependencies
├── README.md                     # This file
│
├── airplane.bmp                  # Player spaceship sprite
├── ufo.bmp                       # Enemy UFO sprite
│
└── assets/
    └── background_music.wav/     # Background music folder
        └── Audio_MainMenu.WAV    # Background music file
```

---

## 🎯 Assignment Requirements Met

### ✅ Primary Requirements:
- [x] Written primarily in Python
- [x] Includes user input (keyboard: A/D/SPACE/Q, mouse: click)
- [x] Provides feedback/response to input (visual, audio, scoring)
- [x] Interactive experience (game responds dynamically to player actions)

### ✅ Design Elements:
- [x] **Logic & State Management:** Game states, collision detection, score tracking
- [x] **User Experience:** Clear instructions, intuitive controls, progressive difficulty
- [x] **Aesthetic Design:** Particle effects, color palette, fullscreen presentation
- [x] **Creative Coding:** Custom particle system, dynamic difficulty scaling

### ✅ Technical Implementation:
- [x] Real-time input handling
- [x] Frame-rate independent movement
- [x] Sprite management and collision detection
- [x] Audio integration
- [x] Visual feedback systems

---

## 🎨 Design Decisions

### Difficulty Scaling:
The game gradually increases UFO movement speed over time, creating an escalating challenge that keeps players engaged without overwhelming beginners.

### Particle System:
Custom explosion effects provide satisfying visual feedback when UFOs are destroyed, enhancing the game's aesthetic appeal and user satisfaction.

### Audio Design:
Background music is set to 30% volume to provide atmosphere without overwhelming sound effects or distracting from gameplay.

### Visual Hierarchy:
- Score and timer positioned in upper corners for easy visibility
- Player bullets (red) and enemy bullets (green) use contrasting colors
- Start screen provides clear instructions before gameplay begins

---

## 🔧 Technical Details

### Libraries Used:
- **pygame** - Game engine and graphics rendering
- **sys** - System operations and exit handling
- **time** - Timer and difficulty scaling
- **random** - UFO spawn positions and movement patterns
- **math** - Particle trajectory calculations

### Key Classes & Functions:
- `show_start_screen()` - Interactive game introduction
- `Particle` - Explosion effect system
- `UfoBullet` - Enemy projectile management
- `create_random_ufo()` - Dynamic enemy spawning

---

## 🐛 Known Issues & Future Improvements

### Potential Enhancements:
- Add pause functionality
- Implement high score saving system
- Add power-ups and special weapons
- Include sound effects for shooting and explosions
- Create multiple difficulty levels
- Add boss battles at certain score thresholds

---

## 📸 Screenshots

![Game Start Screen](screenshots/start_screen.png)
*Interactive start screen with instructions*

![Gameplay](screenshots/gameplay.png)
*Active gameplay with UFOs and particle effects*

---

## 🙏 Credits

### Assets:
- Background Music: [Source/Attribution if needed]
- Graphics: Custom BMP files

### Development:
- Framework: Pygame Community
- Course: SD5913 - Programming for Art and Design

---

## 📄 License

This project is created for educational purposes as part of SD5913 coursework.

---

## 🎓 Reflection

This project explores interactive design through game mechanics, demonstrating how user input can drive dynamic, responsive systems. By implementing real-time collision detection, particle effects, and progressive difficulty scaling, the game creates an engaging loop where player actions have immediate and meaningful consequences.

The combination of visual feedback (explosions, score updates), audio feedback (background music), and mechanical feedback (collision, game over) creates a cohesive interactive experience that responds to and anticipates user behavior.

---

**Enjoy the game! 🚀👾**

# 🧠 Fruit Memory Puzzle Game

A single-player **Memory Puzzle Game** developed in **Python** using **Tkinter**.  
The game challenges players to match pairs of fruit cards across multiple levels with increasing difficulty.

This project was created as part of a **Stage 3 University AI / Programming course** and demonstrates rule-based AI logic, modular design, and GUI development.

---

## 🎮 Game Overview

The Fruit Memory Puzzle Game presents a grid of face-down cards.  
Each card hides a fruit image, and every fruit appears exactly **twice**.

The player flips two cards at a time to find matching pairs.  
The goal is to match all pairs **before the timer runs out**.

---

## 🎯 Objectives

- Improve memory and concentration skills
- Match all card pairs in the shortest time possible
- Complete all levels to win the game

---

## 📜 Game Rules

- Only **two cards** can be flipped at a time
- If the cards match, they remain visible
- If they do not match, they flip back
- Each level has a **time limit**
- The number of cards increases with each level
- The game includes:
  - ⏸ Pause / Resume
  - 💡 Hint system
  - 🔇 Mute sound option
  - 🔁 Replay functionality
- If time runs out, the game restarts from **Level 1**

---

## 🧠 AI Logic Used

The game uses **rule-based AI logic**, not machine learning.

### Key AI Features:
- Random card shuffling
- Game state tracking (revealed, matched, hidden)
- Match-checking logic
- Hint detection algorithm
- Level progression logic
- Timer-based decision making

This approach simulates intelligent behavior through **conditions and rules**, making it suitable for puzzle-based games.

---

## 🔄 Game Flow (Algorithm Summary)

1. Start the game
2. Initialize level and timer
3. Shuffle cards randomly
4. Display cards face-down
5. Player flips two cards
6. Check for a match
7. Update game state
8. Check win or time-out condition
9. Move to next level or restart
10. End game after final level

---

## 🛠 Technologies Used

- **Python 3**
- **Tkinter** – Graphical User Interface
- **Pillow (PIL)** – Image handling
- **winsound** – System sound feedback (Windows)
- Built-in modules: `random`, `os`, `time`

---
## 👥 Team Members & Contributions

This project was developed as a **group project** by four students.  
Each team member was responsible for a specific part of the Memory Puzzle Game to ensure effective collaboration and fair distribution of work.

### 👤 Team Members:

- **Lawa**
  - Project idea and overall coordination  
  - Core game logic (card matching rules, levels, game flow)  
  - Integration of all game components  

- **Mhamad**
  - Graphical User Interface (GUI) design using Tkinter  
  - Card layout, buttons, and screen design  
  - Visual enhancements and animations  

- **Warida**
  - Timer implementation and level progression  
  - Hint system functionality  
  - Game testing and bug fixing  

- **Dene**
  - Sound effects integration  
  - Pause and resume functionality  
  - Project documentation (README and report support)  

### 🤝 Teamwork Statement

All team members worked collaboratively, shared ideas, tested the application, and contributed to the successful completion of the project.

## 📁 Project Structure

| File / Folder | Description |
|--------------|-------------|
| aigameee/ | Main project folder |
| main.py | Main game controller and entry point |
| ui_design.py | Handles all UI layout and widgets |
| ui_animations.py | Card flip and win animations |
| game_logic.py | Card generation and shuffle logic |
| hint_logic.py | Hint detection logic |
| timer_logic.py | Game timer management |
| sound.py | Sound effects and audio feedback |
| sound_control.py | Mute and sound control |
| constants.py | Global constants and asset paths |
| README.md | Project documentation |
| assets/ | Game assets folder |
| assets/images/ | Fruit and card images |
| assets/sounds/ | Sound effect files |

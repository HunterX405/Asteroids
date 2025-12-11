Here’s a **clean, simple, and professional README** for your Boot.dev Asteroids project, with instructions for running the game using **uv**.

You can paste this directly into your `README.md`:

---

# Asteroids (Python + Pygame)

This repository contains a simple Asteroids-style game built with **Python** and **Pygame** as part of the **Boot.dev “Build Asteroids in Python” guided project**.
The project focuses on game loops, object movement, collision detection, and basic game structure using Pygame.

---

## Features

* Player-controlled spaceship
* Asteroid spawning and movement
* Basic collision system
* Game loop architecture
* Clean and modular Python code
* Uses Pygame for rendering and input

---

## Getting Started

### 1. Install `uv` (if not already installed)

**Linux/macOS**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 2. Clone the repository

```bash
git clone https://github.com/yourusername/asteroids
cd asteroids
```

---

### 3. Create virtual environment & install dependencies

Simply run:

```bash
uv sync
```

This will:

* Create the `.venv` environment
* Install Pygame and all required dependencies
* Ensure the correct Python version is used

---

### 4. Run the game

```bash
uv run main.py
```

Or, if you want to activate the environment manually:

**Linux/macOS:**

```bash
source .venv/bin/activate
python main.py
```

**Windows:**

```powershell
.\.venv\Scripts\activate
python main.py
```

---

## Controls

* **Arrow Keys / WASD:** Move the ship
* **Spacebar:** Shoot
* **Escape:** Quit game
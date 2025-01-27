# test_click

# Automated Clicking Script with Reload Functionality

This Python script automates mouse clicks at user-defined points with periodic reload actions. It allows for pausing and stopping via keyboard shortcuts, ensuring flexible control during execution.

## Features
- **Reload Point**: A specific point on the screen to simulate a "reload" action.
- **Click Points**: Up to 10 user-defined points for automated clicking.
- **Keyboard Controls**:
  - `F9`: Pause/Resume execution.
  - `F11`: Stop execution.
- **Randomized Behavior**: Clicking intervals and sequences are randomized to mimic human-like behavior.
- **Execution Limit**: Automatically stops after 110,000 clicks.

## Requirements
- Python 3.8 or higher
- Required libraries:
  - `pyautogui`
  - `pynput`

Install dependencies with:
```bash
pip install pyautogui pynput

# Clock + Date Widget V1

A minimal desktop clock and date widget built with Python and Tkinter for Windows.

## Overview

Clock + Date Widget V1 is a lightweight desktop utility that displays the current time and date in a compact, movable window.

The project focuses on simplicity, minimal resource usage, and straightforward source-code configuration without an additional settings interface.

## Features

- Displays the current time in 24-hour format, including seconds.
- Displays the date in `DD-MM-YYYY` format.
- Borderless window design.
- Always stays on top of other windows.
- Movable window using the left mouse button.
- Adjustable window dimensions and initial position.
- Configurable background color, text color, fonts, and transparency.
- Automatically updates the clock and date every second.

## Built With

- Python 3
- Tkinter
- Python `datetime` module

## Requirements

- Windows
- Python 3.x with Tkinter available

No additional third-party Python packages are required.

## Getting Started

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the application:

   ```bash
   python main.py
   ```

## Configuration

The widget can be customized by editing the configuration constants at the beginning of `main.py`.

| Setting | Description |
|---|---|
| `WIDTH` | Window width |
| `HEIGHT` | Window height |
| `POS_X` | Initial horizontal position |
| `POS_Y` | Initial vertical position |
| `BG_COLOR` | Background color |
| `TEXT_COLOR` | Text color |
| `CLOCK_FONT` | Clock font and size |
| `DATE_FONT` | Date font and size |
| `TRANSPARENCY` | Window opacity, from `0.0` to `1.0` |

This version does not include a graphical settings interface. Configuration is performed directly in the source code.

## Project Background

This project began as a practical solution for displaying the time and date on the desktop in a simple, compact window.

It represents an early step in developing small desktop utilities based on everyday needs.

## Project Status

Version 1 — Minimal clock and date widget.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
 

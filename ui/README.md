#  Fuzzy Logic Based Car Speed Control System

##  Overview

This project implements an intelligent car speed control system using **Fuzzy Logic** with real-time visualization.

The system automatically adjusts vehicle speed based on:

*  Distance from the vehicle ahead
*  Road condition (Wet / Normal / Dry)
*  Traffic light signal (Red / Yellow / Green)

It also includes a **real-time animated dashboard**, making it an interactive and visually appealing simulation.

---

##  Features

###  Fuzzy Logic System

* 3 Inputs:

  * Distance (0–100)
  * Road Condition (0–10)
  * Traffic Light (0–10)
* 1 Output:

  * Speed (0–120 km/h)
* 16+ fuzzy rules
* Centroid defuzzification

---

###  Real-Time Simulation (Pygame)

* Multi-lane road animation
* Moving front vehicle
* Dynamic speed-based motion
* Rain effect (for wet roads)
* Day/Night mode with headlights

---

###  Dashboard & UI

* Circular speedometer
* Speed vs Time graph
* Distance indicator bar
* Rule activation visualization
* Traffic signal mini UI

---

###  Sound Effects

* Engine sound (based on speed)
* Warning beep (when distance is low)

---

###  Data Analytics

* Real-time graph plotting
* CSV logging for:

  * Distance
  * Speed
  * Road condition
  * Traffic light

---

##  Technologies Used

* Python
* pygame
* numpy
* scikit-fuzzy

---


## ▶ How to Run

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/fuzzy-car-speed-control.git
cd fuzzy-car-speed-control
```

### 2. Install dependencies

```
pip install pygame numpy scikit-fuzzy
```

### 3. Run the project

```
python main.py
```

---

##  Controls

| Key   | Action                       |
| ----- | ---------------------------- |
| ↑ / ↓ | Increase / Decrease Distance |
| W     | Wet Road                     |
| N     | Normal Road                  |
| D     | Dry Road                     |
| R     | Red Light                    |
| Y     | Yellow Light                 |
| G     | Green Light                  |
| T     | Toggle Day/Night             |

---

##  Fuzzy Logic Rules

The system uses 16+ rules combining:

* Traffic signals
* Distance
* Road conditions

Example:

* IF Light is RED → Speed is SLOW
* IF Distance is FAR & Road is DRY → Speed is FAST
* IF Road is WET → Reduce speed

---

##  Output

* Real-time speed control
* Visual dashboard
* Logged CSV data for analysis

---

##  Academic Relevance

This project demonstrates:

* Soft Computing (Fuzzy Logic)
* Real-time system simulation
* Intelligent decision-making
* Human-like reasoning in control systems

---

##  Future Improvements

* Automatic traffic light system
* AI-based adaptive learning
* Collision avoidance system
* Integration with real sensor data

---

## Author

Khushboo Yadav

---

## ⭐ If you like this project, give it a star!

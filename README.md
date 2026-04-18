#  Fuzzy Logic Based Car Speed Control System

An intelligent driving simulation system that uses **Fuzzy Logic** to control vehicle speed based on real-world conditions such as traffic signals, road quality, distance from vehicles, and speed limits.

---

##  Overview

This project simulates how a smart vehicle makes driving decisions similar to a human driver. Instead of using strict rules, it applies **fuzzy logic** to handle uncertainty and provide smoother, safer speed control.

The system continuously analyzes multiple inputs and dynamically adjusts the vehicle's speed in real-time.

---

##  Objectives

* To design an intelligent speed control system using fuzzy logic
* To simulate real-world driving conditions
* To improve safety through adaptive decision-making
* To visualize fuzzy logic behavior using graphs and rule activation

---

##  Key Concept: Fuzzy Logic

Unlike traditional logic (true/false), fuzzy logic works with **degrees of truth**.

Example:

* Distance is not just “close” or “far”
* It can be **partially close and partially medium at the same time**

This allows smoother and more human-like decisions.

---

##  System Inputs

The system takes the following inputs:

### 1.  Distance from Front Vehicle

* Close
* Medium
* Far

 Helps prevent collisions and maintain safe spacing.

---

### 2.  Road Condition

* Wet
* Normal
* Dry

 Affects braking and safe speed.

---

### 3.  Traffic Signal

* Red
* Yellow
* Green

 Highest priority input for decision making.

---

### 4.  Speed Limit

* School Zone
* City
* Highway

 Ensures legal and safe driving speeds.

---

##  Output

###  Vehicle Speed

* Slow
* Medium
* Fast

The system calculates a smooth speed value using fuzzy inference.

---

##  Features

###  Real-Time Simulation

* Moving road and vehicles
* Dynamic environment

### Speedometer

* Visual representation of current speed

###  Membership Graphs

* Shows fuzzy values for inputs (distance, road, etc.)

###  Rule Activation Panel

* Displays which fuzzy rules are active in real-time

###  Fuel System

* Simulates fuel consumption based on speed
* Includes fuel bar and consumption graph

###  Brake Warning System

* Alerts when distance is too low

###  Day/Night Mode

* Simulates visibility changes

###  Rain Simulation

* Affects driving conditions and speed decisions

###  Data Logging

* Stores simulation data in CSV format for analysis

---

##  Fuzzy Rule System

The system uses a set of **IF–THEN rules** to make decisions.

Examples:

* IF signal is RED → speed is SLOW
* IF distance is FAR and road is DRY → speed is FAST
* IF road is WET and distance is CLOSE → speed is SLOW

These rules mimic real human driving behavior.

---

##  How It Works

1. Inputs are collected (distance, road, signal, speed limit)
2. Inputs are converted into fuzzy values (fuzzification)
3. Rules are applied to determine output behavior
4. Final speed is calculated (defuzzification)
5. Vehicle speed is updated smoothly

---

##  Controls

| Key       | Function                              |
| --------- | ------------------------------------- |
| ↑ / ↓     | Increase / Decrease distance          |
| W / N / D | Wet / Normal / Dry road               |
| R / Y / G | Traffic signal                        |
| 1 / 2 / 3 | Speed limit (School / City / Highway) |
| T         | Toggle Day/Night mode                 |
| F         | Refuel                                |

---

##  Visualization

* Speed trend graph
* Fuel consumption graph
* Distance safety bar
* Rule activation strength

---

##  Project Structure

```
fuzzy/
  └── fuzzy_logic.py

simulation/
  ├── car.py
  ├── road.py
  ├── rain.py
  └── fuel.py

ui/
  ├── gauge.py
  ├── dashboard.py
  ├── bars.py
  └── rules_panel.py

utils/
  └── logger.py

main.py
config.py
```

---

##  Future Improvements

* Add AI-based learning (adaptive rules)
* Add obstacle detection
* Improve physics realism
* Add lane changing logic

---

##  Conclusion

This project demonstrates how fuzzy logic can be used to build intelligent, adaptive systems that behave more like humans. It highlights the importance of handling uncertainty in real-world decision-making.

---

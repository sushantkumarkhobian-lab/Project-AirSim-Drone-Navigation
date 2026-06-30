# Project AirSim Drone Navigation

Autonomous drone navigation, environment simulation, and flight analytics system built using **Project AirSim by IAMAI**, **Python**, and **Unreal Engine 5**.

This project enables autonomous drone navigation through waypoints and predefined paths while collecting detailed flight analytics for performance evaluation and comparison. The system supports physical wind simulation via external force, weather visual effects, yaw control, time-synchronized flight, smooth takeoff and landing, automated reporting, and navigation performance comparison.

---

# Repository

```bash
git clone https://github.com/sushantkumarkhobian-lab/Project-AirSim-Drone-Navigation.git
cd Project-AirSim-Drone-Navigation
```

---

# Project Overview

The project is divided into three major modules:

## 1. Navigation Module (`navigation.py`)

Handles:

- Autonomous drone takeoff
- Waypoint navigation
- Square path navigation
- Rectangle path navigation
- Circular path navigation
- Yaw control
- Time-synchronized navigation
- Adaptive velocity control
- Wind compensation
- Smooth landing
- Flight analytics logging

---

## 2. Environment Module (`environment.py`)

Handles:

- Wind simulation (physical force via `set_external_force`)
- Rain simulation
- Fog simulation
- Snow simulation
- Dust simulation
- Storm simulation
- Clear environment reset

Allows testing navigation performance under different environmental conditions.

---

## 3. Analysis Module (`analysis.py`)

Handles:

- Flight log comparison
- Performance analysis
- Automated reporting
- Radar chart generation
- Graph generation
- Navigation accuracy evaluation
- Controller performance comparison

---

# Features

## Navigation Features

✔ Autonomous Waypoint Navigation

✔ Square Path Navigation

✔ Rectangle Path Navigation

✔ Circular Path Navigation

✔ Time-Synchronized Flight

✔ Adaptive Velocity Control

✔ Wind Compensation

✔ Yaw Control

✔ Smooth Takeoff

✔ Smooth Landing

✔ Persistent Mission Loop (runs until Exit selected)

---

## Environment Features

✔ Clear Environment

✔ Wind Simulation

✔ Rain Simulation

✔ Fog Simulation

✔ Snow Simulation

✔ Dust Simulation

✔ Storm Simulation

---

## Analytics Features

✔ CSV Flight Logging

✔ Position Error Analysis

✔ Time Error Analysis

✔ Speed Analysis

✔ Battery Usage Estimation

✔ Path Efficiency Analysis

✔ Performance Comparison Reports

✔ Radar Chart Visualization

✔ Automated Winner Selection

---

# Technologies Used

- Python 3.11
- Project AirSim by IAMAI
- Unreal Engine 5
- NumPy
- Pandas
- Matplotlib

---

# Repository Structure

```text
Project-AirSim-Drone-Navigation/
│
├── navigation.py
├── environment.py
├── analysis.py
│
├── requirements.txt
├── README.md
│
├── sample_data/
│   ├── advanced_drone_navigation_analytics1.csv
│   └── advanced_drone_navigation_analytics3.csv
│
├── sample_results/
    └── results13/
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/sushantkumarkhobian-lab/Project-AirSim-Drone-Navigation.git
cd Project-AirSim-Drone-Navigation
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
projectairsim
numpy
pandas
matplotlib
```

---

# Project AirSim Setup

## Step 1: Download Project AirSim Blocks

Download the pre-built Blocks environment from the official Project AirSim releases page:

https://github.com/iamaisim/ProjectAirSim/releases

Download:

```text
Blocks-Windows-UE5.2-PAS_v0.2.0.zip
```

Direct link:

https://github.com/iamaisim/ProjectAirSim/releases/download/v0.2.0/Blocks-Windows-UE5.2-PAS_v0.2.0.zip

Extract the ZIP file.

---

## Step 2: Locate Blocks.exe

After extraction:

```text
Downloads
└── ProjectAirsim-Blocks-Windows
    └── Windows
        └── Blocks.exe
```

Example:

```text
C:\Users\<YourUsername>\Downloads\ProjectAirsim-Blocks-Windows\Windows\Blocks.exe
```

Launch:

```text
Blocks.exe
```

Wait for the simulation to load completely.

---

## Step 3: Clone Official Project AirSim Repository

Clone the official IAMAI Project AirSim repository:

```bash
git clone https://github.com/iamaisim/ProjectAirSim.git
```

This provides the Python client library and the `example_user_scripts` folder where the scripts must be placed.

---

## Step 4: Place Scripts

Copy `navigation.py`, `environment.py`, and `analysis.py` into:

```text
ProjectAirSim\client\python\example_user_scripts\
```

Final structure:

```text
ProjectAirSim
└── client
    └── python
        └── example_user_scripts
            ├── navigation.py
            ├── environment.py
            └── analysis.py
```

The scripts must be placed here to correctly resolve the `projectairsim` Python client library.

---

## Step 5: Verify Simulation Config

Ensure the following folder exists inside your Project AirSim installation:

```text
ProjectAirSim
└── client
    └── python
        └── example_user_scripts
            └── sim_config
```

Inside this folder, the required scene configuration files should be present, such as:

```text
scene_basic_drone.jsonc
```

These configuration files are loaded automatically by the Project AirSim client during runtime.


---

## Step 6: Verify Connection

Launch the simulation, then run:

```bash
python navigation.py
```

Expected output:

```text
Connecting to Project AirSim...
[INFO] Connection opened.
[INFO] World object updated for the loaded scene '/Sim/SceneBasicDrone'.
[INFO] Drone 'Drone1' initialized for World scene '/Sim/SceneBasicDrone'
Connected to Project AirSim successfully.
```

---

# Navigation Modes

## Waypoint Navigation

Predefined mission:

```text
(10,  0, -5)
(10, 10, -5)
( 0, 10, -5)
( 0,  0, -5)
```

---

## Square Path Navigation

User Inputs:

- Height
- Side Length

Drone automatically generates a square trajectory.

---

## Rectangle Path Navigation

User Inputs:

- Height
- Length
- Breadth

Drone automatically generates a rectangular trajectory.

---

## Circular Path Navigation

User Inputs:

- Height
- Radius
- Total Time

Drone automatically generates a circular trajectory.

---

# Environment Simulation

Weather and wind conditions can be set using `environment.py`.

Supported environments:

- Clear
- Windy
- Rainy
- Foggy
- Snowy
- Dusty
- Storm

The script keeps running until you select Exit, so you can change conditions between missions without restarting.

Wind is applied as a physical external force on the drone using `drone.set_external_force()`, meaning it actually affects flight behavior — not just visuals.

---

# Running Navigation

Launch the Project AirSim simulation, then run:

```bash
python navigation.py
```

Menu:

```text
1 -> Waypoint Navigation
2 -> Path Navigation
3 -> Exit
```

Path Navigation Menu:

```text
1 -> Square Path
2 -> Rectangle Path
3 -> Circle Path
4 -> Back
```

The script keeps running after each mission completes. Select Exit (option 3) to stop.

Before each mission, press **T** in the Unreal window to enable the drone flight trail, then return to the terminal and press Enter to start.

---

# Environment Simulation

Launch the Project AirSim simulation, then run:

```bash
python environment.py
```

Menu:

```text
1 -> Clear Environment
2 -> Windy Environment
3 -> Rainy Environment
4 -> Foggy Environment
5 -> Snowy Environment
6 -> Dusty Environment
7 -> Storm Environment
8 -> Exit
```

The selected environment remains active in the scene even after exiting the script.

---

# Flight Analytics

The system automatically records:

- Target Position
- Actual Position
- Desired Time
- Actual Time
- Time Error
- Mission Elapsed Time
- Real World Clock Time
- Distance Travelled
- Average Speed
- Yaw Information
- Final Position Error
- Maximum Position Error
- Estimated Wind Disturbance
- Battery Usage Estimate
- Path Efficiency

Generated output files:

```text
advanced_drone_navigation_analytics1.csv
advanced_drone_navigation_analytics2.csv
advanced_drone_navigation_analytics3.csv
...
```

Each run automatically generates a new numbered CSV file.

---

# Running Analysis

```bash
python analysis.py
```

Example:

```text
Enter first file number: 1
Enter second file number: 2
```

Generated folder:

```text
results12/
```

---

# Analysis Outputs

## Reports

```text
clean_comparison_summary.csv
performance_scorecard.csv
analysis_report.txt
```

## Graphs

```text
actual_time_comparison.png
time_error_comparison.png
final_position_error_comparison.png
max_position_error_comparison.png
average_speed_comparison.png
battery_remaining_comparison.png
average_metric_comparison_bar.png
performance_radar_chart.png
```

---

# Example Workflow

1. Launch Project AirSim
2. Run `environment.py` to set weather conditions
3. Run `navigation.py`
4. Press T in Unreal window to enable flight trail
5. Complete a flight mission
6. CSV is auto-saved
7. Run another mission (different environment if desired)
8. Run `analysis.py`
9. Compare both flight logs
10. Review generated reports and graphs

---

# Sample Data and Results

The repository includes:

```text
sample_data/
```

Sample flight logs recorded from Project AirSim.

```text
sample_results/
```

Example comparison reports and generated graphs.

---

# Key Differences from Legacy AirSim Version

| Feature | Legacy AirSim | Project AirSim |
|---|---|---|
| Client | `airsim.MultirotorClient()` | `ProjectAirSimClient()` + `World()` + `Drone()` |
| Flight API | Blocking `.join()` | `async/await` |
| Weather API | `simSetWeatherParameter()` | `world.set_weather_visual_effects_param()` |
| Wind | `simSetWind()` | `drone.set_external_force()` |
| State | `getMultirotorState()` | `drone.get_ground_truth_kinematics()` |
| Engine | Unreal Engine 4 | Unreal Engine 5 |

---

# Demo

<table>
<tr>
<td align="center">

## Weather Control Menu

<a href="https://youtu.be/M3eCAiOqtdU" target="_blank">
  <img width="1904" height="966" alt="Screenshot 2026-06-30 181920" src="https://github.com/user-attachments/assets/6f7de78f-846a-4af2-9baf-a5ba1ebf31c1" />
</a>

</td>

<td align="center">

## Navigation Menu

<a href="https://youtu.be/UQrnSosRddU" target="_blank">
  <img width="1903" height="969" alt="Screenshot 2026-06-30 181753" src="https://github.com/user-attachments/assets/d4675599-2ada-4ed3-966d-3af40c071450" />
</a>

</td>
</tr>
</table>

<p align="center">
Click any thumbnail to watch the demo on YouTube.
</p>

# Future Improvements

- Custom Unreal Engine 5 Environments
- Multiple Drone Models
- Obstacle Avoidance
- Dynamic Path Planning
- Multi-Drone Coordination
- Advanced PID Controller Tuning
- Real-Time Dashboard Integration
- GPS-Based Navigation
- Real Drone Deployment

---

# Author

**Sushant Kumar Khobian**

B.E. Computer Science & Engineering (IoT, Blockchain & Cybersecurity)

Xavier Institute of Engineering

Mumbai, India

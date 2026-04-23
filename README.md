# Intensity-plotter-for-Malus-Law
The given code takes the intensity variation data with time and plots the intensity variation with angular displacement.

🔧 Features
Reads StarLab .txt log files (UTF-16 encoded)
Automatically filters out headers, comments, and invalid rows
Converts time → angular position using rotation speed
Plots intensity vs angle for multiple polarization states
Supports comparison of multiple datasets in a single graph
📁 Input Data Format

Each input file should:

Be a StarLab-exported .txt file
Contain two columns:
Timestamp (seconds)
Intensity (W)

The script automatically ignores:

Header lines (;, !, etc.)
Non-numeric entries
⚙️ How It Works
The analyzer (polarizer) is rotated at a constant speed

Time values from the log file are converted to angle using:

θ=time×rotation speed
Intensity is plotted as a function of angle

The resulting curves should follow Malus’ Law:

I(θ)=I
0
	​

cos
2
(θ)
▶️ Usage

Update the file names and labels in the script:

files = [
    "NoHWP_0_updated.txt",
    "NoHWP_45_updated.txt",
    "NoHWP_90_updated.txt",
    "NoHWP_-45_updated.txt"
]

labels = ["0°", "45°", "90°", "-45°"]

Set rotation speed (degrees per second):

rotation_speed = 5

Then run:

python script_name.py
📈 Output
A plot of Intensity vs Angle (0–360°)
Multiple polarization states plotted together for comparison
Useful for verifying polarization behavior and Malus’ Law experimentally

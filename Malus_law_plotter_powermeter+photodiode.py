import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# USER INPUT: StarLab log files for 4 polarizer states
# -------------------------------------------------
files = [
    "NoHWP_0_updated.txt",
    "NoHWP_45_updated.txt",
    "NoHWP_90_updated.txt",
    "NoHWP_-45_updated.txt"
]

labels = ["0°", "45°", "90°", "-45°"]

# Analyzer rotation speed
rotation_speed = 5  # degrees per second


# -------------------------------------------------
# Function to read StarLab log file
# -------------------------------------------------
def read_starlab_txt(filename):
    time_vals = []
    intensity_vals = []

    with open(filename, "r", encoding='utf-16') as f:
        for line in f:
            line = line.strip()

            # Skip header / comments / empty lines
            if (
                not line
                or line.startswith(";")
                or line.startswith("!")
                or "Timestamp" in line
            ):
                continue

            parts = line.split()

            # Keep only lines with two numeric columns
            if len(parts) >= 2:
                try:
                    t = float(parts[0])
                    I = float(parts[1])

                    time_vals.append(t)
                    intensity_vals.append(I)
                except ValueError:
                    continue

    return np.array(time_vals), np.array(intensity_vals)


# -------------------------------------------------
# Plotting
# -------------------------------------------------
plt.figure()

for file, label in zip(files, labels):

    time, intensity = read_starlab_txt(file)

    # Convert time → angle
    angle = time * rotation_speed

    plt.plot(angle, intensity, label=f"Polarizer@ {label}")


# -------------------------------------------------
# Graph formatting
# -------------------------------------------------
plt.xlabel("Angle (degrees)")
plt.ylabel("Intensity (W)")
plt.title("Malus Law (With Polarizer)")
plt.xlim(0, 360)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
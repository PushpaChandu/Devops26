import numpy as np
import matplotlib.pyplot as plt

# Time axis (abstract units)
t = np.linspace(0, 1, 5000)

# Idealized "GPS-like" signal (weak by design)
gps_signal = 0.3 * np.sin(2 * np.pi * 5 * t)

# Interference strength ramp (simulates jamming onset)
interference_power = np.linspace(0, 2.0, len(t))
interference = interference_power * np.random.normal(0, 1, len(t))

# Thermal noise
noise = np.random.normal(0, 0.05, len(t))

# Received signal at the receiver
received_signal = gps_signal + interference + noise

# Estimate signal-to-interference ratio (SIR)
sir = np.var(gps_signal) / np.var(interference + noise)

# ---- Plotting ----
plt.figure(figsize=(12, 7))

plt.subplot(3, 1, 1)
plt.plot(t, gps_signal, color='green')
plt.title("Ideal Navigation Signal (No Interference)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, received_signal, color='red')
plt.title("Received Signal Under Increasing Interference")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, interference_power, color='purple')
plt.title("Interference Strength Over Time (Simulation)")
plt.xlabel("Time")
plt.ylabel("Relative Power")

plt.tight_layout()
plt.show()

print(f"Estimated Signal-to-Interference Ratio (abstract): {sir:.4f}")


import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Fourier Series Visualization
# ==========================================

# Signal parameters
T = 4.0
f0 = 1 / T
w0 = 2 * np.pi / T

DC = 1.0
A = 1.0

# Time axis
t = np.linspace(-T, 2*T, 2000)

# Number of harmonics
N = 9

# ==========================================
# Individual components
# ==========================================

components = []

for n in range(1, N + 1):
    component = (4*A / (np.pi*n)) * np.sin(
        n * w0 * t
    ) if n % 2 == 1 else np.zeros_like(t)

    components.append(component)

# ==========================================
# Fourier Series reconstruction
# ==========================================

x = DC * np.ones_like(t)

for component in components:
    x += component

# ==========================================
# Plot 1: DC Component
# ==========================================

plt.figure(figsize=(10, 4))

plt.plot(t, DC * np.ones_like(t), linewidth=2,
         label="DC Component")

plt.axhline(0, color='black', linewidth=0.8)
plt.title("DC Component")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# Plot 2: Fundamental Frequency
# ==========================================

plt.figure(figsize=(10, 4))

plt.plot(t, components[0], linewidth=2,
         label=f"Fundamental (f0 = {f0} Hz)")

plt.axhline(0, color='black', linewidth=0.8)
plt.title("Fundamental Frequency")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# Plot 3: Harmonics
# ==========================================

plt.figure(figsize=(10, 5))

for n in [1, 3, 5, 7, 9]:
    plt.plot(
        t,
        components[n-1],
        label=f"{n}th harmonic ({n*f0:.2f} Hz)"
    )

plt.title("Individual Harmonic Components")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# Plot 4: Fourier Series Reconstruction
# ==========================================

plt.figure(figsize=(12, 5))

plt.plot(t, x, linewidth=2,
         label=f"Fourier Series (N = {N})")

plt.title("Fourier Series Reconstruction")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ==========================================
# Plot 5: Effect of Adding Harmonics
# ==========================================

plt.figure(figsize=(12, 5))

for count in [1, 2, 3, 5, 9]:
    result = DC * np.ones_like(t)

    for component in components[:count]:
        result += component

    plt.plot(t, result, label=f"{count} components")

plt.title("Effect of Increasing Harmonics")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

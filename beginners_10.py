import math

def calculate_sine_wave(time, frequency, amplitude):
    """Calculate the value of a sine wave at a given time, frequency, and amplitude."""
    return amplitude * math.sin(2 * math.pi * frequency * time)

frequency = float(input("Please enter the frequency you want for the sine wave! "))
amplitude = float(input(" please enter the amplitude you want for the sine wave! "))

print(f"Sample values for a {frequency} Hz tone:")
for i in range(10):
    time = i * 0.0001
    value = calculate_sine_wave(time, frequency, amplitude)
    print(f"Time: {time:.5f}s -> Value: {value:.4f}")
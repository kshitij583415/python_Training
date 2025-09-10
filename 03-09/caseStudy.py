# 4]. CASE STUDY:
#      Optical Fiber Communication System Simulator
# Scenario:
# A telecom company wants to simulate the signal transmission in an optical fiber to study how signal strength changes with distance and losses. Your task is to build a Python program using functions that models a basic optical communication system.
# Requirements:
# Write a Python program with the following functionalities (each as a separate function):
# Input Parameters Function
# Take input:
# Initial Power (mW)
# Fiber Length (km)
# Attenuation (dB/km)
# Wavelength (nm)
# Convert Power Function
# Convert input power (mW) into dBm.
# Formula:P(dBm)=10×log⁡10(P(mW))P(dBm) = 10 \times \log_{10}(P(mW))P(dBm)=10×log10(P(mW))
# Calculate Loss Function
# Compute total attenuation:Loss(dB)=Attenuation×FiberLengthLoss(dB) = Attenuation \times FiberLengthLoss(dB)=Attenuation×FiberLength
# Output Power Function
# Calculate received power (dBm):Pout(dBm)=Pin(dBm)−Loss(dB)P_{out}(dBm) = P_{in}(dBm) - Loss(dB)Pout(dBm)=Pin(dBm)−Loss(dB)
# Bitrate vs Wavelength Function (simplified theoretical model)
# Assume the bitrate (Gbps) is inversely proportional to wavelength:Bitrate=1000Wavelength(nm)Bitrate = \frac{1000}{Wavelength (nm)}Bitrate=Wavelength(nm)1000
# Display Results Function
# Print:
# Input Power in dBm
# Fiber Loss (dB)
# Output Power (dBm)
# Estimated Bitrate (Gbps)
# Main Function
# Show a menu to perform:
# Calculate Signal Transmission
# Exit



import math

def convert_power_to_dbm(power_mw):
    return 10 * math.log10(power_mw)

def calculate_loss(length_km, attenuation_db_per_km):
    return length_km * attenuation_db_per_km

def calculate_output_power(power_in_dbm, loss_db):
    return power_in_dbm - loss_db

def calculate_bitrate(wavelength_nm):
    return 1000 / wavelength_nm

def display_results(power_dbm, loss_db, output_power_dbm, bitrate_gbps):
    print(f"Input Power: {power_dbm:.2f} dBm")
    print(f"Total Fiber Loss: {loss_db:.2f} dB")
    print(f"Output Power: {output_power_dbm:.2f} dBm")
    print(f"Estimated Bitrate: {bitrate_gbps:.2f} Gbps")

def main():
    power_mw = float(input("Enter Initial Power (mW): "))
    fiber_length_km = float(input("Enter Fiber Length (km): "))
    attenuation_db_per_km = float(input("Enter Attenuation (dB/km): "))
    wavelength_nm = float(input("Enter Wavelength (nm): "))

    power_dbm = convert_power_to_dbm(power_mw)
    loss_db = calculate_loss(fiber_length_km, attenuation_db_per_km)
    output_power_dbm = calculate_output_power(power_dbm, loss_db)
    bitrate_gbps = calculate_bitrate(wavelength_nm)

    display_results(power_dbm, loss_db, output_power_dbm, bitrate_gbps)

main()


# Sample Output:
# Enter Initial Power (mW): 3 
# Enter Fiber Length (km): 5
# Enter Attenuation (dB/km): 32
# Enter Wavelength (nm): 4

# Input Power: 4.77 dBm
# Total Fiber Loss: 160.00 dB
# Output Power: -155.23 dBm
# Estimated Bitrate: 250.00 Gbps
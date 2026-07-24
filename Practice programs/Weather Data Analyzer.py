temps = [float(input(f"Enter temperature for day {i+1}: ")) for i in range(7)]
print("Max:", max(temps), "Min:", min(temps), "Average:", sum(temps)/7)

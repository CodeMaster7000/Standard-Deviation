def calculate_mean(data):
    return sum(data) / len(data)

def calculate_population_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_sample_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def calculate_standard_deviation(variance):
    return variance ** 0.5
data = list(map(float, input("Enter data (separated by spaces): ").split()))
pop_variance = calculate_population_variance(data)
pop_std_dev = calculate_standard_deviation(pop_variance)

if len(data) > 1:
    samp_variance = calculate_sample_variance(data)
    samp_std_dev = calculate_standard_deviation(samp_variance)
else:
    samp_variance = None
    samp_std_dev = None

print("\nData:", data)
print("\nPopulation Statistics (2 d.p.)")
print("Variance:", round(pop_variance, 2))
print("Standard Deviation:", round(pop_std_dev, 2))
print("\nSample Statistics (2 d.p.)")
if samp_variance is not None:
    print("Variance:", round(samp_variance, 2))
    print("Standard Deviation:", round(samp_std_dev, 2))
else:
    print("Sample variance/standard deviation requires at least 2 data points.")

# Take number of observations
n = int(input("Enter number of observations: "))

data = []
total = 0

print("Enter data values:")
for i in range(n):
    val = int(input())
    data.append(val)
    total += val

# Mean
mean = total / n

# Median
data.sort()
mid = n // 2
if n % 2 == 0:
    median = (data[mid - 1] + data[mid]) / 2
else:
    median = data[mid]

# Mode (using frequency dictionary logic)
freq = {}
for num in data:
    freq[num] = freq.get(num, 0) + 1

maxFreq = max(freq.values())

modes = []
for key in freq:
    if freq[key] == maxFreq:
        modes.append(key)

if len(modes) == len(freq):
    mode = None   # No mode
else:
    mode = modes[0]

# Output
print("\nMean =", mean)
print("Median =", median)
print("Mode =", mode)

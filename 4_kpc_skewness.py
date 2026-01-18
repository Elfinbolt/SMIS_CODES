import math

def calcMean(num,n):
    return sum(num) / n

def calcMedian(num,n):
    num.sort()
    mid = n // 2
    if n % 2 == 0:
        return (num[mid - 1] + num[mid]) / 2
    else:
        return num[mid]

def calcMode(num):
    freq = {}
    for n in num:
        freq[n] = freq.get(n, 0) + 1

    maxFreq = max(freq.values())

    # Simplified mode calculation
    modes = []
    for key in freq:
        if freq[key] == maxFreq:
            modes.append(key)

    if len(modes) == len(freq):
        return None
    else:
        return modes[0]

def calcStdDev(num, mean):
    # Simplified variance calculation
    total = 0
    for x in num:
        total = total + (x - mean) ** 2

    var = total / len(num)
    return math.sqrt(var)

def calcSkewness(num):
    mean = calcMean(num,n)
    median = calcMedian(num,n)
    mode = calcMode(num)
    stdDev = calcStdDev(num, mean)

    if stdDev == 0:
        return 0
    if mode is not None:
        return (mean - mode) / stdDev
    else:
        return (3 * (mean - median)) / stdDev

# Main program
n = int(input("Enter the size of the series: "))
num = []

print("Enter the Elements:")
for i in range(n):
    value = float(input())
    num.append(value)

print("Mean:", calcMean(num, n))
print("Median:", calcMedian(num, n))
print("Mode:",calcMode(num))
print("Standard Deviation:", calcStdDev(num, calcMean(num, n)))
print("Karl Pearson's Coefficient of Skewness:", calcSkewness(num))

if calcSkewness(num) > 0:
    print("Positively Skewed")
elif calcSkewness(num) < 0:
    print("Negatively Skewed")
else:
    print("Symmetric Distribution")

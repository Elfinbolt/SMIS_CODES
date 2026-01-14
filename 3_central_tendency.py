class StatisticsCalculator:
    def __init__(self):
        print("Select the type of series:")
        print("1. Discrete Series")
        print("2. Continuous Series")
        print("3. Individual Series")

        choice = int(input("Enter choice: "))

        if choice == 1:
            self.discrete_series()
        elif choice == 2:
            self.continuous_series()
        elif choice == 3:
            self.individual_series()
        else:
            print("Invalid choice!")

    # 1️⃣ Discrete Series
    def discrete_series(self):
        n = int(input("Enter number of data points: "))

        x = []
        f = []
        sumFX = 0
        sumF = 0

        print("Enter value (x) and frequency (f):")
        for i in range(n):
            xi = int(input(f"x[{i+1}]: "))
            fi = int(input(f"f[{i+1}]: "))
            x.append(xi)
            f.append(fi)
            sumFX += xi * fi
            sumF += fi

        mean = sumFX / sumF

        # ✅ Simplified Cumulative Frequency
        cf = []
        total = 0
        for freq in f:
            total += freq
            cf.append(total)

        # Median
        mid = (sumF + 1) // 2
        for i in range(n):
            if cf[i] >= mid:
                median = x[i]
                break

        # Mode
        mode = x[0]
        maxFreq = f[0]
        for i in range(1, n):
            if f[i] > maxFreq:
                maxFreq = f[i]
                mode = x[i]

        print("\nMean =", mean)
        print("Median =", median)
        print("Mode =", mode)

    # 2️⃣ Continuous Series
    def continuous_series(self):
        n = int(input("Enter number of classes: "))

        lower = []
        upper = []
        f = []
        mid = []
        sumF = 0
        sumFMid = 0

        print("Enter lower limit, upper limit, frequency:")
        for i in range(n):
            li = int(input(f"Lower[{i+1}]: "))
            ui = int(input(f"Upper[{i+1}]: "))
            fi = int(input(f"Frequency[{i+1}]: "))
            lower.append(li)
            upper.append(ui)
            f.append(fi)
            mid_val = (li + ui) / 2
            mid.append(mid_val)
            sumFMid += mid_val * fi
            sumF += fi

        mean = sumFMid / sumF

        # ✅ Simplified Cumulative Frequency
        cf = []
        total = 0
        for freq in f:
            total += freq
            cf.append(total)

        # Median
        N = sumF
        for i in range(n):
            if cf[i] >= N / 2:
                L = lower[i]
                CFprev = 0 if i == 0 else cf[i - 1]
                fm = f[i]
                h = upper[i] - lower[i]
                median = L + ((N / 2 - CFprev) / fm) * h
                break

        # Mode
        modalIndex = 0
        for i in range(1, n - 1):
            if f[i] > f[modalIndex]:
                modalIndex = i

        L = lower[modalIndex]
        f1 = f[modalIndex]
        f0 = f[modalIndex - 1] if modalIndex > 0 else 0
        f2 = f[modalIndex + 1] if modalIndex < n - 1 else 0
        h = upper[modalIndex] - lower[modalIndex]

        mode = L + ((f1 - f0) / (2 * f1 - f0 - f2)) * h

        print("\nMean =", mean)
        print("Median =", median)
        print("Mode =", mode)

    # 3️⃣ Individual Series
    def individual_series(self):
        n = int(input("Enter number of observations: "))

        data = []
        total = 0

        print("Enter data values:")
        for i in range(n):
            val = int(input())
            data.append(val)
            total += val

        mean = total / n

        # Median
        data.sort()
        if n % 2 == 0:
            median = (data[n // 2 - 1] + data[n // 2]) / 2
        else:
            median = data[n // 2]

        # Mode
        mode = data[0]
        maxCount = 1
        currentCount = 1

        for i in range(1, n):
            if data[i] == data[i - 1]:
                currentCount += 1
                if currentCount > maxCount:
                    maxCount = currentCount
                    mode = data[i]
            else:
                currentCount = 1

        print("\nMean =", mean)
        print("Median =", median)
        print("Mode =", mode)


if __name__ == "__main__":
    StatisticsCalculator()

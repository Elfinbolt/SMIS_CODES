def rankData(data):
    sortedData = sorted(set(data))
    rankMap = {}

    # Assign ranks using simple for loop
    rank = 1
    for val in sortedData:
        rankMap[val] = rank
        rank += 1

    # Create ranked list
    ranks = []
    for x in data:
        ranks.append(rankMap[x])

    return ranks


def spearmanRankCorrelation(x, y):
    n = len(x)

    if n != len(y):
        return None

    rx = rankData(x)
    ry = rankData(y)

    # Calculate d² using simple loop
    d=0
    for i in range(n):
        d += ((rx[i] - ry[i])**2)

    return 1 - (6 * d) / (n * ((n ** 2) - 1))


# Main Program
n = int(input("Enter the number of pairs: "))

x = []
y = []

print("Enter the X values:")
for i in range(n):
    value = float(input())
    x.append(value)

print("Enter the Y values:")
for i in range(n):
    value = float(input())
    y.append(value)

rho = spearmanRankCorrelation(x, y)

print("Spearman's Rank Correlation Coefficient:", rho)

if rho > 0:
    print("Perfect Positive Correlation")
elif rho < 0:
    print("Perfect Negative Correlation")
else:
    print("No Correlation")

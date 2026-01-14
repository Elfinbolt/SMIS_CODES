def linear_regression(X, y):
    mean_x = sum(X) / len(X)
    mean_y = sum(y) / len(y)

    # Numerator using normal for loop
    numerator = 0
    for i in range(len(X)):
        numerator += X[i] * y[i]
    numerator = numerator - (sum(X) * sum(y)) / len(X)

    # Denominator using normal for loop
    denominator = 0
    for i in range(len(X)):
        denominator += X[i] ** 2
    denominator = denominator - (sum(X) ** 2) / len(X)

    b = numerator / denominator
    a = mean_y - b * mean_x

    return a, b


# Take number of data points
n = int(input("Enter number of data points: "))

X = []
y = []

# Take values from user
for i in range(n):
    x_val = float(input(f"Enter X[{i+1}]: "))
    y_val = float(input(f"Enter Y[{i+1}]: "))
    X.append(x_val)
    y.append(y_val)

# Calculate regression
a, b = linear_regression(X, y)

# Display equation
print("\nThe linear regression equation is:")
print("Y = {:.2f} + {:.2f}X".format(a, b))

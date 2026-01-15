def chi_square_test(matrix):
    # -------- Row totals --------
    rows = []
    for r in matrix:
        rows.append(sum(r))

    # -------- Column totals --------
    cols = []
    for j in range(len(matrix[0])):
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
        cols.append(col_sum)

    # -------- Grand total --------
    total_sum = sum(rows)

    # -------- Expected frequency matrix --------
    expected_matrix = []
    for i in range(len(matrix)):
        expected_row = []
        for j in range(len(matrix[0])):
            e_val = (rows[i] * cols[j]) / total_sum
            expected_row.append(e_val)
        expected_matrix.append(expected_row)

    # -------- Chi-square calculation --------
    chi_val = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            chi_val += ((matrix[i][j] - expected_matrix[i][j]) ** 2) / expected_matrix[i][j]

    # -------- Degrees of freedom --------
    df = (len(matrix) - 1) * (len(matrix[0]) - 1)

    # -------- Critical value (α = 0.05) --------
    crit_val = 5.99

    # -------- Approximate standard deviation --------
    sd_est = chi_val ** 0.5

    # -------- Output --------
    print("\nChi-Square Statistic:", chi_val)
    print("Degrees of Freedom:", df)
    print("Critical Value (α = 0.05):", crit_val)
    print("Approx Std Dev:", sd_est)

    if chi_val > crit_val:
        print("Decision: Reject Null Hypothesis (Significant)")
    else:
        print("Decision: Fail to Reject Null Hypothesis (Not Significant)")


# -------- USER INPUT PART --------
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

observed_matrix = []

print("Enter the observed frequencies:")
for i in range(r):
    row = []
    for j in range(c):
        val = int(input(f"Value at row {i+1}, column {j+1}: "))
        row.append(val)
    observed_matrix.append(row)

chi_square_test(observed_matrix)

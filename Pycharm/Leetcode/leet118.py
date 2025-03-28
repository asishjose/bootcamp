def generate(numRows):
    triangle = []  # Initialize an empty list to store rows of the triangle.

    # Loop through each row number (from 0 to numRows - 1).
    for row_num in range(numRows):
        row = [None] * (row_num + 1)  # Initialize an empty row with 'None' values.
        row[0], row[-1] = 1, 1  # Set the first and last elements to 1.

        # Fill the middle elements (if any) by summing the adjacent values from the previous row.
        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)  # Add the row to the triangle.

    return triangle  # Return the final triangle.


tri = generate(5)
print(tri)

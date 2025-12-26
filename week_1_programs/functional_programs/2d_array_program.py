"""
            a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
                       standard input and printing them out to standard output.
            b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
            c. Logic -> create 2-dimensional array in memory to read in M rows and N cols
            d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
                      OutputStreamWriter to print the output to the screen.
"""

def matrix_2d_approach_1():
    """
        USING 2 FOR LOOPS
        OUTER LOOP FOR ROWS
        FOR EACH ROW INNER COLUMN LOOP WILL APPEND ITS TEMP_LIST TO THE CORRESPONDING ROW NUMBER/ OUTER LIST INDEX
        note -> WORKS IF ONLY ONE INPUT IS GIVEN AT A TIME
        eg...>
         Enter the Number of Rows 
         3
         Enter the Number of cols
         2
         Enter the Values 
         1
         2
         3
         4
         5
         6
         o/p->  [[1, 2], [3, 4], [5, 6]]
    """
    rows = int(input("Enter the Number of Rows\n"))
    cols = int(input("Enter the number of cols\n"))

    print("Enter the Values")

    matrix_2d = []
    for r in range(rows):
        temp_row = []
        for c in range(cols):
            temp_row.append(int(input()))

        matrix_2d.append(temp_row)

    print(matrix_2d)

    # print(f"value at pos[1][1] -> {matrix_2d[1][1]}")  # ACESSING ELEMNT BY INDEX OF A 2D STRUCTURE
    # print(f"value at pos[2][1] -> {matrix_2d[2][1]}")

    print("Printing After extracting values using two for loops")
    for i in range(rows):
        for j in range(cols):
            print(f"{matrix_2d[i][j]} ", end="")
        print()

def main():
    matrix_2d_approach_1()

if __name__ == "__main__":
    main()



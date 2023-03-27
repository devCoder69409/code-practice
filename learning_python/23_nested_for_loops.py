
number_grid = [ #in this 2d list we have 4 elements. each of them are also lists. 
    [1, 2, 3], #4 rows, 3 columns. we can create grid like structures in python using 2d lists. 
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    print(row) #prints out all the rows.


for row in number_grid:
    for col in row: # we can reach each individual column or each individual element inside of these arrays. #so for example inside of the arrays that are the elements of number grid.
        print(col) #basically prints out all of the elements inside of all of the arrays inside of number grid. 
import csv


def read_csv_pages(n):
    """
    Function to read the first 100 lines of a csv dataset,
    this function will print the title, the author,
    the genre and the number of pages of all books
    with less than n pages.
    """

    with open('books_new.csv') as csv_file:   # Opening,reading file
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = next(csv_reader)         # Gets the first line

        if n <= 0:                            # Conditional for input <= 0
            print('Please, enter a valid length... ')

        i = 0
        
        for row in csv_reader:                # Iteration to get first 100 lines
            if i <= 100 and int(row[4]) < n:  # Books with less than n pages

                one = f'{row[0]} was written by '
                two = f'{row[1]}'
                three = f' and is {row[2]}'
                four = f'book with {row[4]} pages'
                print(one+two+three+four)    # Print
                i += 1                       # Counter up 1
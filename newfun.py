def book_pages(number_of_p):

    """
    Function to find the book with less pages that number_of_p parameter
    """

    books_length = {'Romeo and Juliet': 322,  # New dictionary
                    '1984': 340,
                    '2001: a Space Odyssey': 250,
                    'Pride and Prejudice': 450,
                    'The Great Gatsby': 200,
                    'The Lord of the Rings': 1100,
                    'The Old Man and the Sea': 100,
                    'The Picture of Dorian Gray': 300,
                    'A Christmas Carol': 125}

    max_pages = 0                               # Initialise variables
    book = None
    for k, v in books_length.items():            # Iteration
        # If found new book with more pages than the
        # previous best assign to update variable book
        if v < number_of_p and max_pages < v:
            max_pages = v
            book = k
    # Return
    a = f'The book with most pages less than {number_of_p}'
    b = f'is {book} with {max_pages}'
    return a+b
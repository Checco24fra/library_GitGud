list_of_books = {'Romeo and Juliet': 'William Shakespeare',
'1984': 'George Orwell',
'2001: a Space Odissey': 'Arthur C. Clarke',
'Pride and Prejudice' : 'Jane Austen',
'The Great Gatsby' : 'F.Scott Fitzgerald',
'The Lord of the Rings' : 'J. R. R. Tolkien',
'The Old Man and the Sea' : 'Ernest Hemingway',
'The Picture of Dorian Gray' : 'Oscar Wilde',
'A Christmas Carol' : 'Charles Dickens',
                 }
import csv
import re

def check_book(title):
    if title in list_of_books:
        print("The book {} is written by {}".format(title, list_of_books[title]))
    else:
        print("Sorry, we do not have {}".format(title))

def check_author(author_name):

    found = False
    for title, author in list_of_books.items():
        if author == author_name:
            print("{} wrote {}".format(author_name, title))
            found = True

    if not found:
        print("Sorry, {} is not present.".format(author_name))

def check_by_initial_author(first_letter):
	"""
	check_by_initial_author() returns all authors that starting with the letter given in input
	"""
    flag = 0				# a flag used to verify if there is no author with that letter
    if len(first_letter) == 1:	# if the user insert more than one letter, the script will return an print error
        for name in list_of_books.values():
            if name[0] == first_letter or title[0] == first_letter.upper():	# if a author start with the letter given in input
                print(name)													# it will be printed
                flag = 1													# deactivate the flag
        if flag == 0:
            print("no authors were found starting with the letter \"{}\"".format(first_letter))
    else:
        print("Error! enter only one letter")
        
def check_by_initial_title(first_letter):
	"""
	check_by_initial_title() returns all books that starting with the letter given in input
	"""
    flag = 0 							# a flag used to verify if there is no books with that letter
    if len(first_letter) == 1: 			# if the user insert more than one letter, the script will return an print error
        for title in list_of_books.keys(): # iterator
            if title[0] == first_letter or title[0] == first_letter.upper(): 	# if a book start with the letter given in input
                print(title)													# it will be printed
                flag = 1														# deactivate the flag
        if flag == 0:															
            print("no books were found starting with the letter \"{}\"".format(first_letter))
    else:
        print("Error! enter only one letter")

def read_csv_pages(author_name):
    """
    Function that receive in input a surname and return
    all the books that was written by that author
    """
    with open('books_new.csv') as csv_file:   # Opening file
        flag = 0
        csv_reader = csv.reader(csv_file, delimiter=',') #reading file
        header = next(csv_reader)         # reading the header

        print(f"{author_name.capitalize()} has written:")
        for row in csv_reader:                # Iteration for all lines
            if re.search(f"\W*({author_name.capitalize()})\W*", row[1]):  # Using Regular expression to find the name in the string
                print(f"- {row[0]} in {row[2]}")    # Print
                flag = 1
        if flag == 0:
            print("nothing found...")
import csv
import re

def check_book(title):
    """
    Print the author of a title
    """
    list_of_books = csv_to_title_author()
    if isinstance(title, str):
        if title in list_of_books:
            print("The book {} is written by {}".format(title, list_of_books[title]))
            return True
        else:
            print("Sorry, we do not have {}".format(title))
            return False
    else:
        print("Invalid type, the title should be a string")
        return None

def check_author(author_name):
    """
    Print all the titles written by an author
    """
    list_of_books = csv_to_title_author()
    if isinstance(author_name, str):
        found = False
        for title, author in list_of_books.items():
            if author == author_name:
                print("{} wrote {}".format(author_name, title))
                found = True
                return True

        if not found:
            print("Sorry, {} is not present.".format(author_name))
            return False
    else:
        print("Invalid type, the author's name should be a string")
        return None


def check_by_initial_author(first_letter):
    """
    check_by_initial_author() returns all authors that starting with the letter given in input
    """
    cbia_list= []
    flag = 0 # a flag used to verify if there is no author with that letter
    list_of_books = csv_to_title_author()
    if isinstance(first_letter, str):
        if len(first_letter) == 1:# if the user insert more than one letter, the script will return an print error
            for name in list_of_books.values():
                if name[0] == first_letter or name[0] == first_letter.upper():# if a author start with the letter given in input
                    cbia_list.append(name)
                    flag = 1# deactivate the flag
            if flag == 0:
                print("no authors were found starting with the letter \"{}\"".format(first_letter))
                return []
            else:
                print(*cbia_list, sep='\n')
                return cbia_list
        else:
            print("Error! enter only one letter")
            return False
    else:
        print("Invalid type, the input should be a character")
        return None

def check_by_initial_title(first_letter):
    """
    check_by_initial_title() returns all books that starting with the letter given in input
    """
    cbit_list= []
    flag = 0 							# a flag used to verify if there is no books with that letter
    list_of_books = csv_to_title_author()

    if isinstance(first_letter, str):
        if len(first_letter) == 1: 			# if the user insert more than one letter, the script will return an print error
            for title in list_of_books.keys(): # iterator
                if title[0] == first_letter or title[0] == first_letter.upper(): 	# if a book start with the letter given in input
                    cbit_list.append(title)													# it will be printed
                    flag = 1														# deactivate the flag
            if flag == 0:
                print("no books were found starting with the letter \"{}\"".format(first_letter))
                return []
            else:
                print(*cbit_list, sep='\n')
                return cbit_list
        else:
            print("Error! enter only one letter")
            return False
    else:
        print("Invalid type, the input should be a character")
        return None

def books_by_author(author_name):
    """
    Function that receive in input a surname and return
    all the books that was written by that author
    """
    rcp_list= []
    with open('books_new.csv') as csv_file:   # Opening file
        flag = 0
        csv_reader = csv.reader(csv_file, delimiter=',') #reading file
        header = next(csv_reader)         # reading the header
        if len(author_name)>0:
            print(f"{author_name.capitalize()} has written:")
            for row in csv_reader:                # Iteration for all lines
                if re.search(f"\W*({author_name.capitalize()})\W*", row[1]):  # Using Regular expression to find the name in the string
                    print(f"- {row[0]} in {row[2]}")    # Print
                    rcp_list.append(row[0])
                    flag = 1
            if flag == 0:
                print("nothing found...")
                return False
            else:
                return rcp_list
        else:
            print("The input is empty! Please insert a surname.")
            return None

def csv_to_title_author():
    """
    Function used to convert the .csv file into a dictionary
    containing the book name as index and the author as values
    """
    ctta_dict ={}
    with open('books_new.csv') as csv_file:   # Opening file
        csv_reader = csv.reader(csv_file, delimiter=',') #reading file
        header = next(csv_reader)         # reading the header
        for row in csv_reader:                # Iteration for all lines
            if row[1] != '':#There is some books without an author so I removed it
                ctta_dict[row[0]] = row[1]
    return ctta_dict

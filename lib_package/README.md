## Implementation of a Database of Books


This project simulates a small library with a list of books and associate authors.

In the repository you can find a file named ```library.py``` that implements 8 functions: 

1)```check_book_for_argp``` : uses argparse to see if the input(book title) is in the library
You must write after calling main.py the title of a book inside '' to see if it's present and it's author, use optional arguments -v, --verbose for a different output

2)```check_author_for_argp``` : uses argparse to see if the input(author) is in the library
You must write after calling main.py the author of a book inside '' to see if it's present and the book he wrote, use optional arguments -q, --quiet for a different output


3)```check_book``` : checks if the parameter(title) is in the new library from the csv a returns a string with the author and the book
You must change in the main.py the parameter to have the wanted output

4)```check_author``` : checks if the parameter(author) is in the new library from the csv a returns a string with the author and the book
You must change in the main.py the parameter to have the wanted output

5)```check_by_initial_author``` : checks if the parameter(string of one letter) is in the new library from the csv a returns a string with the author otherwise return another string 
You must change in the main.py the parameter to have the wanted output

6)```check_initial_title``` : checks if the parameter(string of one letter) is in the new library from the csv a returns a string with the title otherwise return another string 
You must change in the main.py the parameter to have the wanted output

7)```books_by_author``` : checks if the parameter(author) is in the new library from the csv a returns a string with all the books that wrote an author otherwise return another string 
You must change in the main.py the parameter to have the wanted output

8) ```csv_to_title``` : creates a new dictionary with all author and title's books of the csv file in lib_package
It's not called and doesn't return nothing

9) ```read_csv_pages( ``` : prints all books in the csv file with less than parameter(n) pages
You must change in the main.py the parameter to have the wanted output

An example is shown in ```main.py``` file to test all the functions in the library plus test.

If you run the program, executing the main file with: ```python main.py``` it will  give you the following results:

```
$ python3 main.py '1984' 'Willian Shakespeare' -q -v
1 Function ) 1984 is written by George Orwell who has the authorship
2) The Willian Shakespeare is not in the library
3) Sorry, we do not have 1984
4) Sorry, Willian Shakespeare is not present.
5) All author with that initial
6) All books with that initial 
7) All books by that author
8) No output because creates a new dictionary
9) From the csv file print all book with less than n pages

```
For tests run:
python -m unittest -v -b tests/test_books_by_author.py
python -m unittest -v -b tests/test_library_basic.py
python -m unittest -v -b tests/test_library_advanced.py

If the tests are correct the output will return ok on all tests/test_library_advanced.py
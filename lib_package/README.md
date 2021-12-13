## Implementation of a Database of Books


This project simulates a small library with a list of books and associate authors.

In the repository you can find a file named ```library.py``` that implements two functions: ```check_book``` and ```check_author```.
Such functions check if the given input is a valid book title in the library collection, or if an author is present.
An example is shown in ```main.py``` file to test if some book or author are in the library.

If you run the program, executing the main file with: ```python main.py``` it will  give you the following results:

```
$ python main.py
The book The Old Man and the Sea is written by Ernest Hemingway
The book Romeo and Juliet is written by William Shakespeare
Sorry, we do not have A Farewell to Arms
Jane Austen wrote Pride and Prejudice
Sorry, Gabriele D'Annunzio is not present.

```

**Optional**: you can consider to extend the given example adding other information about the books (e.g. year, editor, brief description, ...).
You can also consider implementing an utility that reads from a csv file the data, or a database with library users.
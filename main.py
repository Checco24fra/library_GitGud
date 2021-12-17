from library import check_book
from library import check_author
from library import check_book_for_argp
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Find what book wrote an author')
    parser.add_argument('book', help='Write a book')
    parser.add_argument('-v', "--verbose", help="Write if you want more specification", action = 'store_true')
    args = parser.parse_args()

    book_exists, author = check_book_for_argp(args.book)
    if book_exists:
        if args.verbose:
            print(f'The book {args.book} is written by {author} who has the authorship')
        else:
            print(f'{author} wrote {args.book}')
    else:
        print(f'The book {args.book} is not in the library')

    check_book("The Old Man and the Sea")
    check_book("Romeo and Juliet")
    check_book("A Farewell to Arms")
    check_author("Jane Austen")
    check_author("Gabriele D'Annunzio")


from library import check_book_for_argp,check_author_for_argp
from library import check_book, check_author, check_by_initial_author, check_by_initial_title
from lib_package import csvmodule

import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Find what book wrote an author and which author wrote a book')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('book', help='Write a book')
    parser.add_argument('author', help='write an author')
    parser.add_argument('-v', "--verbose", help="Write if you want more specification", action = 'store_true')
    group.add_argument('-q', '--quiet', help='Write an author', action = 'store_true')
    args = parser.parse_args()

    book_exists, author = check_book_for_argp(args.book)
    if book_exists:
        if args.verbose:
            print(f'The book {args.book} is written by {author} who has the authorship')
        else:
            print(f'{author} wrote {args.book}')
    else:
        print(f'The book {args.book} is not in the library')

    
    author_exits, title = check_author_for_argp(args.author)
    if author_exits:
        if args.quiet:
            print(f'{author_exits} has written {title}')
        else:
            print(f'{title} is written by {author_exits}')
    else:
        print(f'The {args.author} is not in the library')


    check_book(args.book)
    check_author(args.author)
    check_by_initial_author("j")
    check_by_initial_title("c")
    
    csvmodule.read_csv_pages(200)
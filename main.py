from library import check_book_for_argp, check_author_for_argp
from library import check_book, check_author
from library import check_by_initial_author, check_by_initial_title
from lib_package import csvmodule


import argparse


if __name__ == '__main__':

    '''
    Argparser makes a person input author and book from terminal
    and outputs a string with the output depending on the 
    optional argument
    ''' 
 
    A = 'Find what book wrote an author and which author wrote a book'
    B = 'Write if you want more specification'
    C = 'Write an author'  # Value to shorten lines

    parser = argparse.ArgumentParser(description='A')
    group = parser.add_mutually_exclusive_group()  # Group for + arg
    parser.add_argument('book', help='Write a book')  # Two positional
    parser.add_argument('author', help='write an author')  # Two opz.
    parser.add_argument('-v', "--verbose", help=B, action='store_true')
    group.add_argument('-q', '--quiet', help=C, action='store_true')
    args = parser.parse_args()

    '''
    First conditional for the first pos. argument
    '''

    book_exists, author = check_book_for_argp(args.book)  # New outputs of fun
    if book_exists:
        if args.verbose:
            print(f'{args.book} is written by {author} who has the authorship')
        else:
            print(f'{author} wrote {args.book}')
    else:
        print(f'The book {args.book} is not in the library')

    '''
    Second conditional for the second pos. argument
    '''

    author_exits, title = check_author_for_argp(args.author)  # New outputs of fun
    if author_exits:
        if args.quiet:
            print(f'{author_exits} has written {title}')
        else:
            print(f'{title} is written by {author_exits}')
    else:
        print(f'The {args.author} is not in the library')


    '''
    Other functions
    '''

    check_book(args.book)
    check_author(args.author)
    check_by_initial_author("j")
    check_by_initial_title("c")
    csvmodule.read_csv_pages(200)

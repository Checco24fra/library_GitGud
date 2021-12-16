from library import check_book
import argparse


parser = argparse.ArgumentParser(description='Find what book wrote an author')
parser.add_argument('book', help='Write an author')
parser.add_argument('-v', "--verbose", help="Write a something", action="store_true")
args = parser.parse_args()

if args.verbose:
    print(check_book(args.book))
    print('This is the only book in the library')
else:
    print(check_book(args.author))

#!/usr/bin/env python3
import sys
import math
books = [("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
         ("1984", "George Orwell", "Dystopian"),
         ("To Kill a Mockingbird", "Harper Lee", "Classic"),
         ("Pride and Prejudice", "Jane Austen", "Romance"),
         ("The Catcher in the Rye", "J.D. Salinger", "Classic"),
         ("Brave New World", "Aldous Huxley", "Dystopian"),
         ("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
         ("The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy"),
         ("Moby-Dick", "Herman Melville", "Adventure"),
         ("Crime and Punishment", "Fyodor Dostoevsky", "Classic")]
authors = {author for _, author, _ in books}
genres = {genre for _, _, genre in books}
borrowed_books = []
def view():
	books.sort(key=lambda b: b[0])
	author = list(authors)
	author.sort()
	genre = list(genres)
	genre.sort()
	borrowed = list(borrowed_books)
	borrowed.sort()
	print("********************************")
	print("""View:
                  1.Books
                  2.Authors
                  3.Genres
                  4.Borrowed books""")
	choice = input("Choose: ").strip()
	match choice:
		case "1":
			print("\nList of books: ")
			for num, book in enumerate(books, start=1):
				if book in borrowed_books:
					print(f"{num}. {book[0]} - {book[1]} ({book[2]}) [BORROWED]")
				else:
					print(f"{num}. {book[0]} - {book[1]} ({book[2]})")
		case "2":
			print("\nList of authors: ")
			for num, author in enumerate(author, start=1):
				print(f"{num}. {author}")
		case "3":
			print("\nList of genres: ")
			for num, genre in enumerate(genre, start=1):
				print(f"{num}. {genre}")
		case "4":
			print("\nList of borrowed books: ")
			if len(borrowed_books) == 0:
				print("none")
			else:
				for num, book in enumerate(borrowed, start=1):
					print(f"{num}. {book[0]} - {book[1]} ({book[2]})")
		case _:
			print("Ivalid input")
def exit():
	print("Exiting...")
	sys.exit()

def add_book():
	global books
	global authors
	global genres
	book = input("Name of book: ").title()
	author = input("Name of author: ").title()
	genre = input("Genre of book: ").title()
	for i in books:
		if book == i[0]:
			print(f"\nbook already exists: {book}")
			break
	else:
		books.append((book, author, genre))
		print(f"\nBook added to library: {book}")
		if author not in authors:
			authors.add(author)
		if genre not in genres:
			genres.add(genre)
def remove_book():
	global books
	global authors
	global genres
	rm_book = input("Enter title to remove: ").lower()
	for book in books:
		if rm_book == book[0].lower():
			books.remove(book)
			print(f"removed: {rm_book}")
			break
	else:
		print(f"{rm_book}: does not exist.")

#def update_lists():     -/Not needed
	#global authors
	#global genres
	#global borrowed_books
	#authors = {author for _, author, _ in books}
	#genres = {genre for _, _, genre in books}

def borrow_book():
	global books
	global borrowed_books
	borrow = input("Enter book to borrow: ").lower()
	for book in borrowed_books:
		if borrow == book[0].lower():
			print("Book already borrowed")
			break
	else:
		for book in books:
			if borrow == book[0].lower():
				borrowed_books.append(tuple(book))
				print(f"Borrowed book: ({borrow})")
				break
		else:
			print(f"Book not found: ({borrow})")

def return_book():
	global books
	global borrowed_books
	rbook = input("Enter book to return: ").lower()
	for book in borrowed_books:
		if book[0].lower() == rbook:
			borrowed_books.remove(book)
			print(f"Book returned: {rbook}")
			break
	else:
		print("Invalid title")

def search():
	print("\n********************************")
	print("""Search by:
		1. Title
		2. Author
		3. Genre """)
	choice = input("Choose: ").strip()
	match choice:
		case "1":
			search_title()
		case "2":
			search_author()
		case "3":
			search_genre()
		case _:
			print("Ivalid input")

def search_title():
	title = input("\nEnter title: ").lower()
	print("\nResult: \n")
	result = []
	for book in books:
		if title == book[0].lower():
			result.append(book)
	result.sort(key=lambda t: t[0])
	if len(result) == 0:
		print("Nothing found")
	else:
		for num, book in enumerate(result, start=1):
			print(f"{num}. {book[0]} - {book[1]} ({book[2]})")

def search_author():
	author = input("\nName of author: ").lower()
	print("\nResult: \n")
	result = []
	for book in books:
		if author == book[1].lower():
			result.append(book)
	result.sort(key=lambda t: t[0])
	if len(result) == 0:
		print("Nothing found")
	else:
		for num, book in enumerate(result, start=1):
			print(f"{num}. {book[0]} - {book[1]} ({book[2]})")

def search_genre():
	genre = input("\nEnter genre: ").lower()
	print("\nResult: \n")
	result = []
	for book in books:
		if genre == book[2].lower():
			result.append(book)
	result.sort(key=lambda t: t[0])
	if len(result) == 0:
		print("Nothing found")
	else:
		for num, book in enumerate(result, start=1):
			print(f"{num}. {book[0]} - {book[1]} ({book[2]})")





while True:
	print("\n********************************")
	print("""Library Menu:
	1. View
	2. Search
	3. Add book
	4. Remove book
	5. Borrow book
	6. Return book
	7. Exit""")
	choice = input("Choose: ").strip()
	match choice:
		case "1":
			view()
		case "2":
			search()
		case "3":
			add_book()
		case "4":
			remove_book()
		case "5":
			borrow_book()
		case "6":
			return_book()
		case "7":
			exit()
		case _:
			print("Invalid input")


class InputProvider:

    def __init__(self):
        pass

    def ask_for_author_name(self):
        self.author_name = input('Enter the the name of the author of the book: ')

    def ask_for_author_surname(self):
        self.author_surname = input('Enter the the surname of the author of the book: ')

    def ask_for_user_name(self):
        self.user_name = input('Enter your name: ')

    def ask_for_user_surname(self):
        self.user_surname = input('Enter your surname: ')

    def ask_for_user_age(self):
        self.user_age = input('Enter your age: ')

    def ask_for_user_mail(self):
        self.user_mail = input('Enter your email address: ')

    def ask_for_user_phone(self):
        self.user_phone = input('Enter your phone number: ')

    def ask_for_books_target(self):
        self.book_type = input('Enter number of books you want to read: ')

    def ask_for_book_type(self):
        self.book_type = input('Enter book type: ')

    def ask_for_book_title(self):
        self.book_title = input('Enter the book title: ')

    def ask_for_book_description(self):
        self.book_description = input('Enter the book description or link to it: ')

    def ask_for_book_year(self):
        self.book_year = input('Enter the publication year: ')

    def ask_for_book_pages(self):
        self.book_year = input('Enter the number of pages of chosen book: ')

    def ask_for_people_book_rating(self):
        self.book_rating = input('Enter the rating people gave to the book (on a scale of 1 to 10): ')

    def ask_for_book_pages_already_read(self):
        self.book_rating = input('How many pages of the book you have already read: ')

    def ask_for_your_book_rating(self):
        self.book_rating = input('Enter the rating you give to the book (on a scale of 1 to 10): ')

    def ask_for_reading_status(self):
        self.reading_status = input('Enter the status of reading the book (Do przeczytania, W trakcie, Przeczytana): ')

    def ask_for_publishing_house(self):
        self.publishing_house = input('Enter the publishing house of the book: ')
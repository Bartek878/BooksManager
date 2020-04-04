from Configurator import Config
config = Config()
from SQL_connection import EstablishingConnection
establishingConnection = EstablishingConnection()

class Inserting_SQL_DATA:

    def dbo_Autorzy(self):
        conn = establishingConnection.Connect_to_SQL()
        author_name = config.author_name
        author_surname = config.author_surname
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Autorzy (imie_autor, nazwisko_autor)
                                        VALUES
                                        (?, ?)
                                        ''', (author_name, author_surname))
            conn.commit()
        except Exception:
            print('Ten autor już istnieje w bazie danych, więc nie zostanie on wprowadzony ponownie.')

    def dbo_Czytelnicy(self):
        conn = establishingConnection.Connect_to_SQL()
        reader_name = config.user_name
        reader_surname = config.user_surname
        reader_age = config.user_age
        reader_email = config.user_mail
        reader_phone = config.user_phone
        reader_target = config.book_target
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Czytelnicy (imie, nazwisko, wiek, email, 
                                        telefon, cel_przeczytanych_ksiazek)
                                        VALUES
                                        (?, ?, ?, ?, ?, ?)
                                        ''', (reader_name, reader_surname, reader_age, reader_email, reader_phone, reader_target))
            conn.commit()
        except Exception:
            print('Ten czytelnik już istnieje w bazie danych, więc nie zostanie on wprowadzony ponownie.')

    def dbo_Gatunki(self):
        conn = establishingConnection.Connect_to_SQL()
        book_type = config.book_type
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Gatunki (gatunek)
                                        VALUES
                                        (?)
                                        ''', (book_type))
            conn.commit()
        except Exception:
            print('Ten gatunek już istnieje w bazie danych, więc nie zostanie on wprowadzony ponownie.')

    def dbo_Ksiazki(self):
        conn = establishingConnection.Connect_to_SQL()
        book_title = config.book_title
        book_description = config.book_description
        book_year = config.book_year
        book_pages = config.book_pages
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Ksiazki (tytul, opis, rok_wydania, liczba stron)
                                        VALUES
                                        (?, ?, ?, ?)
                                        ''', (book_title, book_description, book_year, book_pages))
            conn.commit()
        except Exception:
            print('Ta ksiazka już istnieje w bazie danych, więc nie zostanie ona wprowadzona ponownie.')

    def dbo_Oceny(self):
        conn = establishingConnection.Connect_to_SQL()
        book_rating_people = config.book_rating_people
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Oceny (ocena_innych)
                                        VALUES
                                        (?)
                                        ''', (book_rating_people))
            conn.commit()
        except Exception:
            print('Ta ocena już istnieje w bazie danych, więc nie zostanie ona wprowadzona ponownie.')

    def dbo_Przeczytania(self):
        conn = establishingConnection.Connect_to_SQL()
        book_pages_already_read = config.book_pages_already_read
        book_rating_user = config.book_rating_user
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Przeczytania (liczba_stron_przeczytanych, twoja_ocena)
                                        VALUES
                                        (?, ?)
                                        ''', (book_pages_already_read, book_rating_user))
            conn.commit()
        except Exception:
            print('Takie dane juz istnieja w bazie danych, więc nie zostana one wprowadzona ponownie.')

    def dbo_Statusy(self):
        conn = establishingConnection.Connect_to_SQL()
        reading_status = config.reading_status
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Statusy (obecny_status)
                                        VALUES
                                        (?)
                                        ''', (reading_status))
            conn.commit()
        except Exception:
            print('Taki status juz istnieje w bazie danych, więc nie zostanie on wprowadzony ponownie.')

    def dbo_Wydawnictwa(self):
        conn = establishingConnection.Connect_to_SQL()
        publishing_house = config.publishing_house
        try:
            conn.execute('''
                                        INSERT INTO BooksManager.dbo.Wydawnictwa (onazwa_wydawnictwa)
                                        VALUES
                                        (?)
                                        ''', (publishing_house))
            conn.commit()
        except Exception:
            print('Takie wydawnictwo juz istnieje w bazie danych, więc nie zostanie ono wprowadzony ponownie.')

class UpdatingBookStatus:

    def __init__(self):
        pass

    def change_status(self):
        status_info = input('Czy chcesz zmienić status dla którejs z ksiazek? (TAK lub NIE):')
        if status_info == 'TAK':
            for_title = input('Podaj tytuł książki dla której chcesz zmienić status: ')
            status_to_be = input('Na jaki status chcesz zmienić (Do przeczytania, W trakcie, Przeczytane)?')
            print()
            conn = establishingConnection.Connect_to_SQL()
            conn.execute("UPDATE FinalResults SET obecny_status = ? WHERE tytul = ?", (status_to_be, for_title))
            conn.commit()
        elif status_info != 'TAK':
            print('Nie to nie, w takim razie bierz sie za czytanie :)')

class BooksCounter:

    def __init__(self):
        pass

    def count_books(self):

        conn = establishingConnection.Connect_to_SQL()
        conn.execute("SELECT COUNT(imie) FROM FinalResults WHERE imie = ?", (config.user_name))
        wynik = conn.fetchall()
        ilosc = len(wynik)
        print('Obecnie ilość przeczytanych przez Ciebie książek to: ' + ilosc)

        conn.execute("SELECT cel_przeczytanych_ksiazek FROM Czytelnicy WHERE imie = ?", (config.user_name))
        cel = conn.fetchall()
        ilosc_cel = len(cel)
        pozostalo = ilosc_cel - ilosc
        print('Natomiast Twoj cel to ' + cel + 'ksiazek, wiec pozostalo Ci do przeczytania ' + pozostalo)

class BooksProposer:

    def __init__(self):
        pass

    def proposed_choice(self):

        conn = establishingConnection.Connect_to_SQL()
        conn.execute("SELECT TOP 1 tytul FROM Ksiazki WHERE id_gatunek = 2 ORDER BY NEWID()")
        wynik = conn.fetchall()
        print('Patrzac na wybrany przez Ciebie gatunek, proponuje przeczytac rowniez ten tytul: ' + wynik)
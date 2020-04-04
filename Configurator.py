import pathlib
from selenium import webdriver
from UserInputs import InputProvider
inputProvider = InputProvider()

class Config(object):
    author_name = inputProvider.ask_for_author_name()
    author_surname = inputProvider.ask_for_author_surname()
    user_name = inputProvider.ask_for_user_name()
    user_surname = inputProvider.ask_for_user_surname()
    user_age = inputProvider.ask_for_user_age()
    user_mail = inputProvider.ask_for_user_mail()
    user_phone = inputProvider.ask_for_user_phone()
    book_target = inputProvider.ask_for_books_target()
    book_type = inputProvider.ask_for_book_type()
    book_title = inputProvider.ask_for_book_title()
    book_description = inputProvider.ask_for_book_description()
    book_year = inputProvider.ask_for_book_year()
    book_pages = inputProvider.ask_for_book_pages()
    book_rating_people = inputProvider.ask_for_people_book_rating()
    book_pages_already_read = inputProvider.ask_for_book_pages_already_read()
    book_rating_user = inputProvider.ask_for_your_book_rating()
    reading_status = inputProvider.ask_for_reading_status()
    publishing_house = inputProvider.ask_for_publishing_house()
    driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    server_name = 'ARLAPPDK419\PYTHONAPPS'
    database_name = 'BooksManager'
    file_ok = str(pathlib.Path().absolute()) + '\weather_ok.csv'
    mail_subject = 'SQL data set'
    sql_query_main = '''
SELECT 
	Czytelnicy.imie,nazwisko,wiek,email,telefon,ilosc_przeczytanych_ksiazek, cel_przeczytanych_ksiazek,
	Ksiazki.tytul,opis,rok_wydania,
	Przeczytania.liczba_stron_przeczytanych,
	Ksiazki.liczba_stron, 
	Statusy.obecny_status, 
	Gatunki.gatunek,
	Autorzy.imie_autor,nazwisko_autor,
	Wydawnictwa.nazwa_wydawnictwa,
	Przeczytania.twoja_ocena,
	Oceny.ocena_innych
FROM Przeczytania
	INNER JOIN Czytelnicy
		ON Przeczytania.id_czytelnik = Czytelnicy.id_czytelnik
	INNER JOIN Ksiazki 
		ON Przeczytania.id_ksiazka = Ksiazki.id_ksiazka
		INNER JOIN Gatunki
			ON Ksiazki.id_gatunek = Gatunki.id_gatunek
		INNER JOIN Autorzy
			ON Ksiazki.id_autor = Autorzy.id_autor
		INNER JOIN Wydawnictwa
			ON Ksiazki.id_wydawnictwo = Wydawnictwa.id_wydawnictwo
	INNER JOIN Statusy
		ON Przeczytania.id_status = Statusy.id_status
	INNER JOIN Oceny
		ON Przeczytania.id_ocena = Oceny.id_ocena'''
# Python app using SQL and Selenium.

from Configurator import Config
config = Config()
from SQL_connection import EstablishingConnection
establishingConnection = EstablishingConnection()
from SQL_InsertData import Inserting_SQL_DATA, UpdatingBookStatus, BooksCounter, BooksProposer
inserting_SQL_DATA = Inserting_SQL_DATA()
updatingBookStatus = UpdatingBookStatus()
booksCounter = BooksCounter()
booksProposer = BooksProposer

def main():

    establishingConnection.Connect_to_SQL()
    establishingConnection.run_query()
    inserting_SQL_DATA.dbo_Autorzy()
    inserting_SQL_DATA.dbo_Czytelnicy()
    inserting_SQL_DATA.dbo_Gatunki()
    inserting_SQL_DATA.dbo_Ksiazki()
    inserting_SQL_DATA.dbo_Oceny()
    inserting_SQL_DATA.dbo_Przeczytania()
    inserting_SQL_DATA.dbo_Statusy()
    inserting_SQL_DATA.dbo_Wydawnictwa()
    updatingBookStatus.change_status()
    booksCounter.count_books()
    booksProposer.proposed_choice()


if __name__ == '__main__':
    main()
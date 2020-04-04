from Configurator import Config
config = Config()
import pyodbc

class EstablishingConnection:

    def __init__(self):
        pass

    def Connect_to_SQL(self):

        conn = pyodbc.connect("DRIVER={{SQL Server}};"
                              "SERVER={0};"
                              "database={1};"
                              "trusted_connection=yes"
                              .format(Config.server_name,Config.database_name))

        return conn

    def run_query(self):
        conn = self.Connect_to_SQL()
        cursor = conn.cursor()
        conn.execute(Config.sql_query_main)

        for row in cursor:
             print(row)
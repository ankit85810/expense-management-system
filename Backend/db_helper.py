import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "root",
        database = "expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit :
         connection.commit()
    cursor.close()
    connection.close()

def fetch_expense_for_date(expense_date):
    logger.info(f"fetch_expense_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT  * FROM expenses WHERE expense_date = %s" , (expense_date,))
        data = cursor.fetchall()
        return data

def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s" , (expense_date,))

def insert_expense(expense_date,amount,category ,notes):
    logger.info(f"insert_expense called with date : {expense_date} , amount : {amount} , category : {category} and notes : {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date , amount , category , notes) VALUES (%s,%s,%s,%s)", (expense_date,amount,category ,notes))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start date: {start_date} and end date: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT category , SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s and %s  GROUP BY category", (start_date,end_date))
        data = cursor.fetchall()
        return data
    
def fetch_expense_summary_all_months():
    logger.info("fetch_expense_summary_all_months called")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT DATE_FORMAT(expense_date, '%M %Y') AS month_name,SUM(amount) AS total_spent FROM expenses GROUP BY month_name ORDER BY MIN(expense_date)")
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    expenses = fetch_expense_for_date("2024-08-01")
    print(expenses)
    # summary = fetch_expense_summary("2024-08-03" , "2024-09-05")
    # for records in summary:
    #     print(records)
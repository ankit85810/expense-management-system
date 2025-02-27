from Backend import db_helper

def test_fetch_expense_for_date_15th_aug():
    expenses = db_helper.fetch_expense_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"

def test_fetch_expanse_for_date_invalid():
    expenses = db_helper.fetch_expense_for_date("9999-09-01")
    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2994-09-01" , "2099-09-02")

    assert len(summary) == 0

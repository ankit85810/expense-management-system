from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from pydantic import BaseModel
from typing import List

class Expense(BaseModel):
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date

app = FastAPI()

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date: date):
    dataa = db_helper.fetch_expense_for_date(expense_date)
    if dataa is None:
        raise HTTPException(status_code= 500 , detail="Failed to retrieve expenses from the database.")
    return dataa

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date : date , expenses:List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)

    return {"message" : "Expenses updated successfully"}

@app.post("/analytics")
def get_analytics_by_category(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    
    if data is None:
        raise HTTPException(status_code=500 , detail="Failed to retrieve expense summary from the database.")
    
    total = sum([row['total'] for row in data])

    breakdown = {}

    for row in data:
        
        percentage = (row['total']/total) * 100 if total != 0 else 0
        breakdown[row['category']] = {
            "total" : row['total'],
            "percentage" : percentage
        }
    return breakdown

@app.get("/analytics_month")
def get_analytics_by_month():
    data = db_helper.fetch_expense_summary_all_months()

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    return data

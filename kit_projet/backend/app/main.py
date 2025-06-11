from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "employeesdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

class Employee(BaseModel):
    id: int
    name: str
    role: str

@app.get("/employees", response_model=List[Employee])
def get_employees():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, role FROM employees;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "name": r[1], "role": r[2]} for r in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/employees", response_model=Employee)
def add_employee(emp: Employee):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO employees (id, name, role) VALUES (%s, %s, %s);",
                    (emp.id, emp.name, emp.role))
        conn.commit()
        cur.close()
        conn.close()
        return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

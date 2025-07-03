from fastapi import FastAPI
from pydantic import BaseModel
import os


class SalaryInput(BaseModel):
    salary: int
    bonus: int
    taxes: int


# Set port to the env variable PORT to make it easy to choose the port on the server
# If the Port env variable is not set, use port 8000
PORT = os.environ.get("PORT", 8000)
app = FastAPI(port=PORT)


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/multiply")
async def multiply_number(number: float):
    return {"result": number*2}

@app.post("/salary")
async def calculate_salary(salary_input: SalaryInput):
    return {"result": salary_input.salary + salary_input.bonus - salary_input.taxes}
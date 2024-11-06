from fastapi import FastAPI

app = FastAPI()

@app.get("/sum1n/{n}")
def sum1n(n: int):
    result = sum(range(1, n + 1))
    return {"result": result}

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

###############################

@app.get("/fibo")
def fibo(n: int):
    result = fibonacci(n)
    return {"result": result}

from fastapi import Header

###############################

@app.post("/reverse")
def reverse(string: str = Header()):
    reversed_string = string[::-1]
    return {"result": reversed_string}

###############################

from fastapi import Body

items = []

@app.put("/list")
def add_to_list(element: dict = Body()):
    items.append(element["element"])
    return {"result": items}

@app.get("/list")
def get_list():
    return {"result": items}

###############################

from fastapi import HTTPException

@app.post("/calculator")
def calculator(expr: dict = Body()):
    try:
        num1, operator, num2 = expr["expr"].split(',')
        num1, num2 = float(num1), float(num2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise HTTPException(status_code=403, detail="zerodiv")
            result = num1 / num2
        else:
            raise ValueError
    except (ValueError, KeyError):
        raise HTTPException(status_code=400, detail="invalid")
    return {"result": result}

########################################


from fastapi import FastAPI, Request, Header, Body, HTTPException
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from starlette.responses import Response
import time

app = FastAPI()

# Метрики
http_requests_total = Counter(
    'http_requests_total', 'Number of HTTP requests received', ['method', 'endpoint']
)
http_requests_milliseconds = Histogram(
    'http_requests_milliseconds', 'Duration of HTTP requests in milliseconds', ['method', 'endpoint']
)
last_sum1n = Gauge('last_sum1n', 'Value stores last result of sum1n')
last_fibo = Gauge('last_fibo', 'Value stores last result of fibo')
list_size = Gauge('list_size', 'Value stores current list size')
last_calculator = Gauge('last_calculator', 'Value stores last result of calculator')
errors_calculator_total = Counter('errors_calculator_total', 'Number of errors in calculator')

# Middleware для сбора метрик по HTTP-запросам
@app.middleware("http")
async def track_metrics(request: Request, call_next):
    method = request.method
    endpoint = request.url.path

    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000  # в миллисекундах

    # Обновление
    http_requests_total.labels(method=method, endpoint=endpoint).inc()
    http_requests_milliseconds.labels(method=method, endpoint=endpoint).observe(duration)

    return response

# Эндпоинт для метрик Prometheus
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")

# Маршруты
@app.get("/sum1n/{n}")
def sum1n(n: int):
    result = sum(range(1, n + 1))
    last_sum1n.set(result) 
    return {"result": result}

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.get("/fibo")
def fibo(n: int):
    result = fibonacci(n)
    last_fibo.set(result) 
    return {"result": result}

items = []

@app.post("/reverse")
def reverse(string: str = Header()):
    reversed_string = string[::-1]
    return {"result": reversed_string}

@app.put("/list")
def add_to_list(element: dict = Body()):
    items.append(element["element"])
    list_size.set(len(items)) 
    return {"result": items}

@app.get("/list")
def get_list():
    return {"result": items}

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
                errors_calculator_total.inc()  
                raise HTTPException(status_code=403, detail="zerodiv")
            result = num1 / num2
        else:
            raise ValueError
        last_calculator.set(result)  
    except (ValueError, KeyError):
        errors_calculator_total.inc()  
        raise HTTPException(status_code=400, detail="invalid")
    return {"result": result}
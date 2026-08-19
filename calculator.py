def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



def lambda_handler(event, context):
    # 'event' is the input AWS sends in, e.g. {"operation": "add", "a": 2, "b": 3}
    operation = event.get("operation")
    a = event.get("a")
    b = event.get("b")

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        return {"statusCode": 400, "body": "Unknown operation"}

    return {"statusCode": 200, "body": str(result)}
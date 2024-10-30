from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template("calculator.html", title="Fun Calculator")

@app.route("/calculate", methods=["POST"])
def calculate():
    if request.method=='POST':
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        # Perform the selected operation
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            # Handle division by zero
            result = "Undefined (division by zero)" if num2 == 0 else num1 / num2
        else:
            result = "Invalid operation"
            
    return render_template("result.html", title="Calculation Result", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

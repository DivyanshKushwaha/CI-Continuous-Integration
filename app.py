from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def power_calculator():
    result = {}
    if request.method == "POST":
        try:
            n = int(request.form.get("number", 1))
            result["number"] = n
            result["square"] = n ** 2
            result["cube"] = n ** 3
            result["fifth_power"] = n ** 5
        except ValueError:
            result["error"] = "Please enter a valid integer"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

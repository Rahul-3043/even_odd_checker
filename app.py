from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def check_even_odd():
    result = ""
    if request.method == "POST":
        num = request.form.get("number", type=int)
        if num is not None:
            result = f"{num} is {'Even' if num % 2 == 0 else 'Odd'}"
    return render_template_string("""
        <h2>Even or Odd Checker</h2>
        <form method="post">
            Enter number: <input name="number" type="number" required />
            <input type="submit" value="Check" />
        </form>
        <p>{{ result }}</p>
    """, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


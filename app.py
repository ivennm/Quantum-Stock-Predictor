from flask import Flask, render_template, request
import return_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    stock_data = None
    financials = None
    actions = None
    stock_name = None

    if request.method == "POST":
        stock_name = request.form["stock_name"].upper()
        stock_data, financials, actions = return_data.get_data(stock_name)

    
    return render_template("index.html", stock_data=stock_data, financials=financials, actions=actions, stock_name=stock_name)

if __name__ == "__main__":
    app.run(debug=True)
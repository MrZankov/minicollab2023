from flask import Flask, render_template, request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/graph", methods=["POST"])
def graph():
  file = request.files["file"]
  df = pd.read_csv(file)
  sns.lineplot(x="Date", y="Temperature", data=df)
  plt.savefig("static/graph.png")
  return render_template("graph.html")

if __name__ == "__main__":
  app.run(debug=True)
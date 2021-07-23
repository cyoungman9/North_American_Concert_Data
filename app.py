from flask import Flask, render_template, redirect
import pandas as pd
import json
import plotly
import plotly.express as px
from sqlalchemy import create_engine


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/city')
def city():
    return render_template('city.html')

@app.route('/gross')
def gross():
    return render_template('gross.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

@app.route('/revenue')
def revenue():
    return render_template('revenue.html')

@app.route('/concert')
def concert():
    rds_connection_string = "postgres:postgres@localhost:5432/Concerts"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    year_df = pd.read_sql_query('select * from concert_count_year', con=engine).head()
    fig = px.bar(year_df, x="year", y="count", title="Number of Concerts by Year")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    description = """
    This bar chart was constructed using 58 months, or approximately 6 years, of North American concert data. As one would expect, the number of concerts on average increases in the spring, reaches its apex in the summer, and decreases in the fall. Outdoor amphitheaters add a significant amount of concert crowd capacity during the summer months.
    """
    return render_template('concert.html', graphJSON=graphJSON, description=description)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
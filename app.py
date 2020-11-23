from flask import Flask, render_template
from map import plot_3d_map
import pandas as pd

app = Flask(__name__)

def read_data(path='data/national-charge-point-registry.csv'):
    df = pd.read_csv(path)
    return df


@app.route('/')
def map():
    df = read_data()
    return render_template('map.html', map=plot_3d_map(df).to_html(as_string=True,
                                                                            iframe_width=800,
                                                                            iframe_height=800,
                                                                            notebook_display=False
                                                                            ))


if __name__ == "__main__":
    app.run(debug=True)
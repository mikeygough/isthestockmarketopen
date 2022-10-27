from flask import Flask, render_template, request
import datetime

# turn this file into a flask app
app = Flask(__name__)

@app.route("/")
def index():
    # current date
    now = datetime.datetime.now()
    
    # list of NYSE holidays
    # source: https://www.nyse.com/markets/hours-calendars
    holidays = [datetime.datetime(2022, 1, 17),
                datetime.datetime(2022, 2, 21),
                datetime.datetime(2022, 4, 15),
                datetime.datetime(2022, 5, 30),
                datetime.datetime(2022, 6, 20),
                datetime.datetime(2022, 7, 4),
                datetime.datetime(2022, 9, 5),
                datetime.datetime(2022, 11, 24),
                datetime.datetime(2022, 12, 26),
                datetime.datetime(2023, 1, 2),
                datetime.datetime(2023, 1, 16),
                datetime.datetime(2023, 2, 20),
                datetime.datetime(2023, 4, 7),
                datetime.datetime(2023, 5, 29),
                datetime.datetime(2023, 6, 19),
                datetime.datetime(2023, 7, 4),
                datetime.datetime(2023, 9, 4),
                datetime.datetime(2023, 11, 23),
                datetime.datetime(2023, 12, 25),
                datetime.datetime(2024, 1, 1),
                datetime.datetime(2024, 1, 15),
                datetime.datetime(2024, 2, 19),
                datetime.datetime(2024, 3, 29),
                datetime.datetime(2024, 5, 27),
                datetime.datetime(2024, 6, 19),
                datetime.datetime(2024, 7, 4),
                datetime.datetime(2024, 9, 2),
                datetime.datetime(2023, 11, 28),
                datetime.datetime(2023, 12, 25)]

    # check if holiday
    holiday = now in holidays

    return render_template("index.html", holiday=holiday)


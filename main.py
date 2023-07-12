import billboard
import requests
import os
import datetime
from flask import Flask, request, render_template


app = Flask(__name__)
global chosen_date


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/boxes', methods=["POST"])
def boxes():
    date = request.form['date']
    chosen_date = date
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    print(edit_date)
    return render_template("boxes.html", date=date)


@app.route('/music')
def music():
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    final_date = edit_date.strftime('%Y-%m-%d')
    chart = billboard.ChartData('hot-100', date=final_date)
    return render_template("music.html", date=chosen_date, song_list=chart)


@app.route('/featured')
def feat():
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    written_date = edit_date.strftime('%B-%d')
    final_date = edit_date.strftime('%Y/%m/%d')

    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/featured/' + final_date

    headers = {
        'Authorization': os.environ['AccessToken'],
        'User-Agent': 'Time Machine'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return render_template("featured.html", date=written_date, feat_list=data['onthisday'])


@app.route('/deaths')
def deaths():
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    written_date = edit_date.strftime('%B-%d')
    final_date = edit_date.strftime('%m/%d')
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/deaths/' + final_date

    headers = {
        'Authorization': os.environ['AccessToken'],
        'User-Agent': 'Time Machine'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return render_template("deaths.html", date=written_date, death_list=data['deaths'])


@app.route('/world events')
def events():
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    written_date = edit_date.strftime('%B-%d')
    final_date = edit_date.strftime('%m/%d')
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/events/' + final_date

    headers = {
        'Authorization': os.environ['AccessToken'],
        'User-Agent': 'Time Machine'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    return render_template("events.html", date=written_date, event_list=data['events'])


@app.route('/birthdays')
def birthdays():
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    written_date = edit_date.strftime('%B-%d')
    final_date = edit_date.strftime('%m/%d')
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/births/' + final_date

    headers = {
        'Authorization': os.environ['AccessToken'],
        'User-Agent': 'Time Machine'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    return render_template("birthdays.html", date=written_date, birthday_list=data['births'])


@app.route('/holidays')
def holidays():
    try:
        edit_date = datetime.datetime.strptime(chosen_date, '%d-%m-%Y')
    except ValueError:
        return render_template("formatdate.html")
    written_date = edit_date.strftime('%B-%d')
    final_date = edit_date.strftime('%m/%d')
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/holidays/' + final_date

    headers = {
        'Authorization': os.environ['AccessToken'],
        'User-Agent': 'Time Machine'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return render_template("holidays.html", date=written_date, holiday_list=data['holidays'])


@app.route('/formatdate')
def formatdate():
    return render_template("formatdate.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, send_file, request, url_for
import random
from datetime import datetime
from clndr import generate_calendar, createLines, create_calendar_image

app = Flask(__name__)


@app.route("/")
def home():
    calendar_link = url_for('calendar_endpoint', _external=True)
    return f"""
    <h1>🗓 Useless Calendar API</h1>
    <p>Get your calendar as PNG:</p>
    <a href="{calendar_link}">{calendar_link}</a>
    """

@app.route("/calendar")
def calendar_endpoint():
    year = int(request.args.get("year", datetime.now().year + 1))
    hide = random.random()
    clndr = generate_calendar(year, hide_probability=hide)
    lines = createLines(clndr, year, hide)
    print(lines)
    img_buf = create_calendar_image(lines, 3840, 2160)
    return send_file(img_buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
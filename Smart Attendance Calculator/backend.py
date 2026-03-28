from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/progress", methods=["GET", "POST"])
def home():

    attendance = ""   # ✅ changed from None
    message = ""
    status = ""

    if request.method == "POST":

        total = int(request.form["total"])
        attended = int(request.form["attended"])
        na = int(request.form["na"])

        effective_total = total - na

        if effective_total > 0:

            attendance = round((attended / effective_total) * 100, 2)

            if attendance >= 75:
                skip = math.floor((attended / 0.75) - effective_total)
                message = f"✔ You are ELIGIBLE for semester. You can skip {skip} classes."
                status = "success"

            else:
                needed = math.ceil((0.75 * effective_total) - attended)
                message = f"⚠ You are DETAINED. Attend {needed} more classes to reach 75%."
                status = "warning"

        else:
            message = "Invalid input. Check values."
            status = "warning"

    return render_template(
        "frontend.html",
        attendance=attendance,
        message=message,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)
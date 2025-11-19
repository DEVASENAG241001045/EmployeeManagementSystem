app.route("/att", methods=["GET", "POST"])
def att():
    return render_template("att.html")
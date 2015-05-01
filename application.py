from flask import Flask, request

app = Flask(__name__)

@app.route("/application-form")
def application_form():
    # Return this as a string

    return render_template("application-form.html")
    
    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application-form", methods="GET")
def application_info():
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("openjobs")

    return render_template("application-answers.html",
                            first_name=first_name,
                            salary = salary,
                            job = job
                            )

if __name__ == "__main__":
    app.run(debug=True)
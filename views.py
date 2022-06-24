from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)
task_list = []

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/todos", methods= ["GET", "POST"])
def todos():
    if request.method == "POST":
        task = request.form.get("task-input")
        task_list.append(task)
        print(task_list)
        return render_template("todos.html", task_list=task_list)
    return render_template("todos.html")

@views.route("/basket")
def basket():
    return render_template("basket.html")

@views.route("/seriesone")
def seriesone():
    return render_template("seriesone.html")

@views.route("/seriestwo")
def seriestwo():
    return render_template("seriestwo.html")

@views.route("/seriesthree")
def seriesthree():
    return render_template("seriesthree.html")

@views.route("/customercare")
def customercare():
    return render_template("customercare.html")   

@views.route("/checkout")
def checkout():
    return render_template("checkout.html")

@views.route("/product")
def item():
    return render_template("product.html")
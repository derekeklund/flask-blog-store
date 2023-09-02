
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask muthafucka!'

from flask import Flask, render_template, session, request, redirect, g
# from flask_session import Session
# from flask_session.__init__ import Session
# import sqlite3
from email.message import EmailMessage
import ssl
import smtplib
# from flask_sqlalchemy import SQLAlchemy


# Configure app
app = Flask(__name__)


# Send email when someone reviews a product
def send_review_email(product):
    name = request.form.get('name')
    email = request.form.get('email')
    stars = request.form.get('stars')
    title = request.form.get('title')
    body = request.form.get('body')
    product = product

    print("Name: ", name)
    print("Email: ", email)
    print("Stars: ", stars)
    print("Title: ", title)
    print("Body: ", body)

    email_sender = 'derekeklund32@gmail.com'
    email_password = 'vkouogdhapwzzmoh'
    email_receiver = 'derekeklund32@gmail.com'

    subject = 'New Product Review - FinRizz'

    body = f"""
    Product: {product} \n
    Reviewer: {name} \n
    Email: {email} \n
    Rating: {stars} \n
    Title: {title} \n
    Body: {body}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# @login_required is a function from helpers.py file that ensures the user is redirected to login first to access page
@app.route("/", methods=["GET", "POST"])
#@login_required
def index():
    return render_template("index.html")

# Blog navigation
@app.route("/blog/the_hound_of_hounslow", methods=["GET", "POST"])
def hound():
    return render_template("blog/the_hound_of_hounslow.html")

@app.route("/blog/meme_traders", methods=["GET", "POST"])
def meme_traders():
    return render_template("blog/meme_traders.html")

@app.route("/blog/tanker_gang", methods=["GET", "POST"])
def tanker_gang():
    return render_template("blog/tanker_gang.html")

@app.route("/blog/martin_shkreli", methods=["GET", "POST"])
def martin():
    return render_template("blog/martin_shkreli.html")


# Product navigation
@app.route("/products/subprime-mug", methods=["GET", "POST"])
def product_1():

    # If user writes review
    if request.method == "POST":
        send_review_email("Subprime Mug")
        return redirect("/products/subprime-mug")

    # GET (no form submission)
    else:
        return render_template("products/subprime-mug.html")


@app.route("/products/ftx-mug", methods=["GET", "POST"])
def product_2():

    if request.method == "POST":
        send_review_email("FTX Mug")
        return redirect("/products/ftx-mug")

    else:
        return render_template("products/ftx-mug.html")


@app.route("/products/lehman-mug", methods=["GET", "POST"])
def product_3():

    if request.method == "POST":
        send_review_email("Lehman Mug")
        return redirect("/products/lehman-mug")

    else:
        return render_template("products/lehman-mug.html")


@app.route("/products/svb-mug", methods=["GET", "POST"])
def product_4():

    if request.method == "POST":
        send_review_email("SVB Mug")
        return redirect("/products/svb-mug")

    else:
        return render_template("products/svb-mug.html")


@app.route("/products/stratton-mug", methods=["GET", "POST"])
def product_5():

    if request.method == "POST":
        send_review_email("Stratton Mug")
        return redirect("/products/stratton-mug")

    else:
        return render_template("products/stratton-mug.html")


@app.route("/products/guh-mug", methods=["GET", "POST"])
def product_6():

    if request.method == "POST":
        send_review_email("Guh Mug")
        return redirect("/products/guh-mug")

    else:
        return render_template("products/guh-mug.html")


@app.route("/products/theta-gang-oe-mug", methods=["GET", "POST"])
def product_7():

    if request.method == "POST":
        send_review_email("Theta Gang OE Mug")
        return redirect("/products/theta-gang-oe-mug")

    else:
        return render_template("products/theta-gang-oe-mug.html")


@app.route("/products/theta-gang-retro-mug", methods=["GET", "POST"])
def product_8():

    if request.method == "POST":
        send_review_email("Theta Gang Retro Mug")
        return redirect("/products/theta-gang-retro-mug")

    else:
        return render_template("products/theta-gang-retro-mug.html")


@app.route("/products/subprime-shirt", methods=["GET", "POST"])
def product_9():

    if request.method == "POST":
        send_review_email("Subprime Shirt")
        return redirect("/products/subprime-shirt")

    else:
        return render_template("products/subprime-shirt.html")


@app.route("/products/ftx-shirt", methods=["GET", "POST"])
def product_10():

    if request.method == "POST":
        send_review_email("FTX Shirt")
        return redirect("/products/ftx-shirt")

    else:
        return render_template("products/ftx-shirt.html")


@app.route("/products/lehman-shirt", methods=["GET", "POST"])
def product_11():

    if request.method == "POST":
        send_review_email("Lehman Shirt")
        return redirect("/products/lehman-shirt")

    else:
        return render_template("products/lehman-shirt.html")


@app.route("/products/bear-stearns-intern-shirt", methods=["GET", "POST"])
def product_12():

    if request.method == "POST":
        send_review_email("Bear Stearns Intern Shirt")
        return redirect("/products/bear-stearns-intern-shirt")

    else:
        return render_template("products/bear-stearns-intern-shirt.html")


@app.route("/products/bear-stearns-is-fine-shirt", methods=["GET", "POST"])
def product_13():

    if request.method == "POST":
        send_review_email("Bear Stearns Is Fine Shirt")
        return redirect("/products/bear-stearns-is-fine-shirt")

    else:
        return render_template("products/bear-stearns-is-fine-shirt.html")


@app.route("/products/svb-bonds-shirt", methods=["GET", "POST"])
def product_14():

    if request.method == "POST":
        send_review_email("SVB Bonds Shirt")
        return redirect("/products/svb-bonds-shirt")

    else:
        return render_template("products/svb-bonds-shirt.html")


@app.route("/products/theta-gang-shirt", methods=["GET", "POST"])
def product_15():

    if request.method == "POST":
        send_review_email("Theta Gang Shirt")
        return redirect("/products/theta-gang-shirt")

    else:
        return render_template("products/theta-gang-shirt.html")


@app.route("/products/svb-bank-run-shirt", methods=["GET", "POST"])
def product_16():

    if request.method == "POST":
        send_review_email("SVB Bank Run Shirt")
        return redirect("/products/svb-bank-run-shirt")

    else:
        return render_template("products/svb-bank-run-shirt.html")


# Shop navigation
@app.route("/shop_new", methods=["GET", "POST"])
def shop_new():
    return render_template("shop_new.html")

@app.route("/shop_best_sellers", methods=["GET", "POST"])
def best_sellers():
    return render_template("shop_best_sellers.html")

@app.route("/shop_shirts", methods=["GET", "POST"])
def shop_shirts():
    return render_template("shop_shirts.html")

@app.route("/shop_sweatshirts", methods=["GET", "POST"])
def shop_sweatshirts():
    return render_template("shop_sweatshirts.html")

@app.route("/shop_hats", methods=["GET", "POST"])
def shop_hats():
    return render_template("shop_hats.html")

@app.route("/shop_mugs", methods=["GET", "POST"])
def shop_mugs():
    return render_template("shop_mugs.html")

@app.route("/shop_all", methods=["GET", "POST"])
def shop_all():
    return render_template("shop_all.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blog.html")


# Footer navigation
@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@app.route("/shipping", methods=["GET", "POST"])
def shipping():
    return render_template("shipping.html")

@app.route("/refunds", methods=["GET", "POST"])
def refunds():
    return render_template("refunds.html")

@app.route("/privacy", methods=["GET", "POST"])
def privacy():
    return render_template("privacy.html")

@app.route("/terms_of_service", methods=["GET", "POST"])
def terms():
    return render_template("terms_of_service.html")

@app.route("/meet_the_team", methods=["GET", "POST"])
def meet():
    return render_template("meet_the_team.html")

if __name__ == "__main__":
    app.run(debug=False) # This should be set to false in a production environment
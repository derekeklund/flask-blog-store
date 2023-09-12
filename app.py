from flask import Flask, render_template, session, request, g, redirect
# from flask_session import Session
# from flask_session.__init__ import Session
import sqlite3
import os
from email.message import EmailMessage
import ssl
import smtplib

# Configure app
app = Flask(__name__)

# Get database connection
def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get current reviews for product
def get_reviews(product):
    # print("Product: ", product)
    conn = get_db_connection()

    rating = conn.execute(f"SELECT avgReview FROM averageReviews WHERE productName = '{product}'").fetchall()

    reviews = conn.execute(f"SELECT reviewerName, reviewTitle, reviewBody, rating FROM userReviews WHERE productName = '{product}'").fetchall()

    print("Rating: ", rating)
    print("Reviews: ", reviews)


    if not reviews:
        returnStatement = "No reviews yet for this product."
        print(returnStatement)

        conn.close()
        return returnStatement
    
    else:
        avgRating = rating[0]
        reviews = reviews[0]
        # print("Rating: ", rating)
        print("Reviews: ", reviews)
        avgRating = avgRating['avgReview']
        reviewerName = reviews['reviewerName']
        reviewTitle = reviews['reviewTitle']
        reviewBody = reviews['reviewBody']
        reviewRating = reviews['rating']
        print("ReviewerName: ", reviewerName)
        print("ReviewTitle: ", reviewTitle)
        print("ReviewBody: ", reviewBody)
        print("Review Rating: ", reviewRating)
        print(f"The current rating for {product} is: ", avgRating)

        conn.close()
        return avgRating, reviewerName, reviewTitle, reviewBody, reviewRating

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
    reviews = get_reviews("Subprime_Mug") 

    print("Reviews: ", reviews)

    avgRating = reviews[0]
    reviewerName = reviews[1]

    print("Average Rating: ", avgRating)
    print("Reviews : ", reviews)
    reviewTitle = reviews[2]
    reviewBody = reviews[3]
    reviewRating = reviews[4]

    print("Average Rating: ", avgRating)
    print("Reviewer Name: ", reviewerName)
    print("Review Title: ", reviewTitle)
    print("Review Body: ", reviewBody)
    print("Review Rating: ", reviewRating)

    if request.method == "POST":
        send_review_email("Subprime Mug")
        return redirect("/products/subprime-mug")

    # GET (no form submission)
    else:
        return render_template("products/subprime-mug.html", reviews=reviews)
    

@app.route("/products/ftx-mug", methods=["GET", "POST"])
def product_2():
    reviews = get_reviews("FTX_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("FTX Mug")
        return redirect("/products/ftx-mug")

    else:
        return render_template("products/ftx-mug.html", reviews=reviews)
    

@app.route("/products/lehman-mug", methods=["GET", "POST"])
def product_3():
    reviews = get_reviews("Lehman_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Lehman Mug")
        return redirect("/products/lehman-mug")

    else:
        return render_template("products/lehman-mug.html", reviews=reviews)


@app.route("/products/svb-mug", methods=["GET", "POST"])
def product_4():
    reviews = get_reviews("SVB_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("SVB Mug")
        return redirect("/products/svb-mug")

    else:
        return render_template("products/svb-mug.html", reviews=reviews)


@app.route("/products/stratton-mug", methods=["GET", "POST"])
def product_5():
    reviews = get_reviews("Stratton_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Stratton Mug")
        return redirect("/products/stratton-mug")

    else:
        return render_template("products/stratton-mug.html", reviews=reviews)


@app.route("/products/guh-mug", methods=["GET", "POST"])
def product_6():
    reviews = get_reviews("Guh_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Guh Mug")
        return redirect("/products/guh-mug")

    else:
        return render_template("products/guh-mug.html", reviews=reviews)


@app.route("/products/theta-gang-oe-mug", methods=["GET", "POST"])
def product_7():
    reviews = get_reviews("Theta_OE_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Theta Gang OE Mug")
        return redirect("/products/theta-gang-oe-mug")

    else:
        return render_template("products/theta-gang-oe-mug.html", reviews=reviews)


@app.route("/products/theta-gang-retro-mug", methods=["GET", "POST"])
def product_8():
    reviews = get_reviews("Theta_Retro_Mug")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Theta Gang Retro Mug")
        return redirect("/products/theta-gang-retro-mug")

    else:
        return render_template("products/theta-gang-retro-mug.html", reviews=reviews)


@app.route("/products/subprime-shirt", methods=["GET", "POST"])
def product_9():
    reviews = get_reviews("Subprime_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Subprime Shirt")
        return redirect("/products/subprime-shirt")

    else:
        return render_template("products/subprime-shirt.html", reviews=reviews)


@app.route("/products/ftx-shirt", methods=["GET", "POST"])
def product_10():
    reviews = get_reviews("FTX_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("FTX Shirt")
        return redirect("/products/ftx-shirt")

    else:
        return render_template("products/ftx-shirt.html", reviews=reviews)


@app.route("/products/lehman-shirt", methods=["GET", "POST"])
def product_11():
    reviews = get_reviews("Lehman_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Lehman Shirt")
        return redirect("/products/lehman-shirt")

    else:
        return render_template("products/lehman-shirt.html", reviews=reviews)


@app.route("/products/bear-stearns-intern-shirt", methods=["GET", "POST"])
def product_12():
    reviews = get_reviews("Bear_Stearns_Intern_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Bear Stearns Intern Shirt")
        return redirect("/products/bear-stearns-intern-shirt")

    else:
        return render_template("products/bear-stearns-intern-shirt.html", reviews=reviews)


@app.route("/products/bear-stearns-is-fine-shirt", methods=["GET", "POST"])
def product_13():
    reviews = get_reviews("Bear_Stearns_Is_Fine_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Bear Stearns Is Fine Shirt")
        return redirect("/products/bear-stearns-is-fine-shirt")

    else:
        return render_template("products/bear-stearns-is-fine-shirt.html", reviews=reviews)


@app.route("/products/svb-bonds-shirt", methods=["GET", "POST"])
def product_14():
    reviews = get_reviews("SVB_Bonds_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("SVB Bonds Shirt")
        return redirect("/products/svb-bonds-shirt")

    else:
        return render_template("products/svb-bonds-shirt.html", reviews=reviews)


@app.route("/products/theta-gang-shirt", methods=["GET", "POST"])
def product_15():
    reviews = get_reviews("Theta_Gang_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("Theta Gang Shirt")
        return redirect("/products/theta-gang-shirt")

    else:
        return render_template("products/theta-gang-shirt.html", reviews=reviews)


@app.route("/products/svb-bank-run-shirt", methods=["GET", "POST"])
def product_16():
    reviews = get_reviews("SVB_Bank_Run_Shirt")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("SVB Bank Run Shirt")
        return redirect("/products/svb-bank-run-shirt")

    else:
        return render_template("products/svb-bank-run-shirt.html", reviews=reviews)
    
@app.route("/products/ftx-hat", methods=["GET", "POST"])
def product_17():
    reviews = get_reviews("FTX_Hat")

    if reviews == "No reviews yet for this product.":
        print("YARRRRRGGGG")

    # print("Reviews: ", reviews)

    if request.method == "POST":
        send_review_email("FTX Bahamas Hat")
        return redirect("/products/ftx-hat")

    else:
        return render_template("products/ftx-hat.html", reviews=reviews)


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

@app.route("/shop_collections", methods=["GET", "POST"])
def shop_collections():
    return render_template("shop_collections.html")

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
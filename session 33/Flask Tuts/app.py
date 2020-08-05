from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


friends = {"Ritvik" : 18, 
			"Bhargav" : 12, "Naivedh" : 24}

age = 29


dog_images = ["https://cdn.pixabay.com/photo/2016/12/13/05/15/puppy-1903313__340.jpg",
"https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg",
 "https://www.cesarsway.com/wp-content/uploads/2019/10/AdobeStock_190562703.jpeg"]




# routes
@app.route("/")
def kuch_bhi():
	choose_dog = np.random.choice(dog_images)
	return render_template("home.html", my_friends = friends, my_age = age, dog_url = choose_dog)

@app.route("/order")
def orders_page():
	return "This page will show all your orders.!!!"


@app.route("/submit", methods = ['GET', 'POST'])
def get_name():
	if request.method == 'POST':
		n = request.form['my_name']

	return "<h1>Welcome  {} </h1>".format(n)









if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image


app = Flask(__name__)

dic = {0 : 'cat', 1 : 'dog', 2 :"horse", 3:'human'}


model = load_model('model.h5')
model._make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(100,100))
	i = image.img_to_array(i)
	i = i.reshape(1, 100,100,3)
	p = model.predict_classes(i)
	return dic[p[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def kuch_bhi():
	return render_template("home.html")

@app.route("/about")
def about_page():
	return "About You..!!!"






@app.route("/submit", methods = ['GET', 'POST'])
def get_hours():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)



	return render_template("home.html", prediction = p, img_path = img_path)





if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
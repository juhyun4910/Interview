from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_model_filename(height, weight):
    if 150 <= height < 160:
        height = 155
    elif 160 <= height < 170:
        height = 165
    elif 170 <= height <= 180:
        height = 175
    else:
        return None

    if 40 <= weight < 50:
        weight = 45
    elif 50 <= weight < 60:
        weight = 55
    elif 60 <= weight < 70:
        weight = 65
    elif 70 <= weight <= 80:
        weight = 75
    else:
        return None

    return f"{height}_{weight}_S.glb"

@app.route('/')
def avatar_selection():
    return render_template('avatar_selection.html')

@app.route('/customize_avatar', methods=['POST'])
def customize_avatar():
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    model_filename = get_model_filename(height, weight)
    if model_filename:
        return render_template('avatar_customize.html', model_filename=model_filename)
    else:
        return "Invalid height or weight", 400

@app.route('/fitting_avatar', methods=['POST'])
def fitting_avatar():
    model_filename = request.form['model_filename']
    return render_template('avatar_fitting.html', model_filename=model_filename)

if __name__ == '__main__':
    app.run(debug=True)

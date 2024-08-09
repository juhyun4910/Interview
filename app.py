from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def avatar_selection():
    return render_template('avatar_selection.html')

@app.route('/customize_avatar', methods=['POST'])
def customize_avatar():
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    model_filename = get_model_filename(height, weight)  # 모델 파일 이름 결정하는 함수

    return render_template('avatar_customize.html', model_filename=model_filename)

@app.route('/fitting_avatar', methods=['POST', 'GET'])
def fitting_avatar():
    model_filename = request.args.get('model_filename') if request.method == 'GET' else request.form['model_filename']
    return render_template('avatar_fitting.html', model_filename=model_filename)

@app.route('/avatar_fitting2', methods=['GET','POST'])
def avatar_fitting2():
    model_filename = request.args.get('model_filename') if request.method == 'GET' else request.form['model_filename']
    return render_template('avatar_fitting2.html', model_filename=model_filename)

def get_height_category(height):
    if 150 <= height < 160:
        return '155'
    elif 160 <= height < 170:
        return '165'
    else:
        return '175'

def get_weight_category(weight):
    if 40 <= weight < 50:
        return '45'
    elif 50 <= weight < 60:
        return '55'
    elif 60 <= weight < 70:
        return '65'
    else:
        return '75'
    
def get_model_filename(height, weight):
    # 키와 몸무게를 바탕으로 모델 파일 이름을 결정하는 로직
    height_category = get_height_category(height)
    weight_category = get_weight_category(weight)
    return f"{height_category}_{weight_category}_S.glb"

if __name__ == '__main__':
    app.run(debug=True)

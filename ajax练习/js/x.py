from flask import Flask,request
import json





app = Flask(__name__)


@app.route('/index')
def x():
    data={
	'name':'coco',
	'age':'23'
	}
    return data



@app.route('/test_10',methods=['post'])
def y():
    return_dict = {
        'return_doce':'200',
        'message':'处理成功',
        'result':'False'
            }
    if request.args is None:
        return_dict['return_code'] = '204'
        return_dict['message'] = '请求参数为空'
        return return_dict
    else:
        get_data=request.get_json()
        return_dict['result']='%s今年%s岁' % (get_data['name'],get_data['age'])
        return return_dict

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }




if __name__ == '__main__':
    app.run('127.0.0.1','8082',debug=True )

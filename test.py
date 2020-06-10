# x = 5
# if x<3:
#     print('小')
# elif x>5:
#     print('中')
# else:
#     print('大')


# def test(x,y=3):
#     print(x)
#     print(y)
# test(2)
from flask import Flask
app=Flask(__name__)
#定义路由
@app.route('/index')
def index():
    html="<div> hello world </div>"
    return html
if __name__=='__main__':
    #开启调试服务器
    app.run(debug=True)
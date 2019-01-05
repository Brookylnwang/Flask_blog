from flask import Flask, request, render_template, jsonify, abort
import time, dns.resolver, bs4

# from flask_restful import reqparse,abort,Api,Resource


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# 用户名密码登录
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return render_template('home.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

# 跳转到个人练习页面
@app.route('/traing', methods=['GET'])
def demo_traing():
    return render_template('traing.html')


# 尝试写Flask的api接口
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': u'Centos',
        'description': u'Need to learn for a long time',
        'done':True
    }
]


@app.route('/resolve_dns', methods=['GET'])
def resolve_dns():
    domain = request.values.get("domain_name")
    if not domain:
        return "Domain_name is null"
    A = dns.resolver.query(domain, 'A')
    for i in A.response.answer:
        for j in i.items:
            j = str(j) + "\n"
            j += j

    return render_template('traing.html',results=j,domain=domain)
    # return j
# 简易的API实例演示，通过URL传递参数。
@app.route('/todo/api/v1.0/tasks/<int:task_id>/', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))  # 转化为list,filter对象没有len属性
    if len(task) == 0:
        return "Not found this page!!!"
    return jsonify({'tasks': task[0]})




if __name__ == '__main__':
    app.run(debug=True)

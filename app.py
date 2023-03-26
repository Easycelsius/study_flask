from flask import Flask, jsonify, redirect, render_template, url_for, request

# import logging
# # 파일로 남기기 위해  filename='test.log' parameter로 추가한다.
# logging.basicConfig(filename='test.log', level=logging.DEBUG)

# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

app = Flask(__name__)

@app.route("/")
def hello():                           
    return "<h1>Hello World!</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id

@app.route("/first/<int:messageid>")
def get_first(messageid):
    return "<h1>%d</h1>" % (messageid + 5)

@app.route('/json_test')
def hello_json():
    data = {'name' : 'Aaron', 'family' : 'Byun'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = { 'server_name' : '0.0.0.0', 'server_port' : '8080' }
    return jsonify(data)

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['myName']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('myName')
      return redirect(url_for('success', name=user))
   
@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('simple.html')

@app.route('/hello_loop')
def hello_name():
    value_list = ['list1', 'list2', 'list3']
    return render_template('loop.html', values=value_list)

@app.route('/hello_if')
def if_html():
    value = 20
    return render_template('condition.html', data=value)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>", 404

@app.route('/get')
def get_cookie():
    username = request.cookies.get('username')
    return render_template('loop.html', name=username)

host_addr = "0.0.0.0"
port_num = "9000"

if __name__ == "__main__":              
    app.run(host=host_addr, port=port_num)

'''
anotation

before_first_request : 웹 application 기동 이후 가장 처음에 들어오는 HTTP 요청에서만 실행
before_request : HTTP 요청이 들어올때마다 실행
before_first_request, before_request는 인자를 전달할 수는 없음
after_request : HTTP 요청이 끝나고 브라우저에 응답하기 전에 실행
teardown_request : HTTP 요청 결과가 브라우저에 응답한 다음 실행
teardown_appcontext : HTTP 요청이 완전히 완료되면 실행
'''

'''

'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return get_page('default_username')  # 여기서 'default_username'을 원하는 기본 사용자 이름으로 변경하세요.

@app.route('/<username>')
def get_page(username):
    length = len(username)
    return render_template("index.html", name=username, length=length)

if __name__ == "__main__":
    app.run()
    print('11111111')
from bottle import get, post, request, run, route, template, static_file
import json



@route('/')
def index():
    return template('views/index.tpl')

@route('/generator')
def generator():
    return template('static/templete/generator.html')

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")


@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")


@get('/login')
def login():
    return template('static/templete/test_it.html')


@post('/login')
def do_login():
    data_frame = {}
    answer = []

    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    otdel = request.forms.get("otdel")

    data_frame["user_name"] = first_name
    data_frame["Last_name"] = last_name
    data_frame["otdel"] = otdel

    with open(first_name + last_name + ".json", "w", encoding="UTF-8") as f:
        for i in range(1, 20, 1):
            param = request.forms.get("answer{}".format(i))
            answer.append(param)
        data_frame["answers"] = answer
        json.dump(data_frame, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run(host="127.0.0.1", port=8080, debug=True, reloader=True)
import requests

login_url = 'http://exercise.kingname.info/exercise_login'
login_success_url = 'http://exercise.kingname.info/exercise_login_success'

data ={
    'username': 'kingname',
    'password': 'genius'
}

session = requests.Session()
before_login = session.get(login_success_url).text
print('登录前的页面：', before_login)
print('登录中...')
response = session.post(login_url, data=data)
print('登录后的页面：', response.text)
after_login = session.get(login_success_url).text
print('登录后的页面：', after_login)

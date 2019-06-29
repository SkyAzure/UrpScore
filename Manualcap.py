from PIL import Image
import requests
from io import BytesIO
import sys


def get_html():
    # hosturl用于获取cookies, posturl是登陆请求的URL
    # login_url = 'http://jwxt.tust.edu.cn/'
    number = '16012115'
    password = '094414'

    login_url = 'http://jwxtxs.tust.edu.cn/j_spring_security_check'
    html_url = "http://jwxtxs.tust.edu.cn/wx/login/user"

    # User-Agent信息
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    # Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    postData = {'j_username': number, 'j_password': password, 'j_captcha': '', 'j_captcha1': "error"}
    # 登陆Form_Data信息

    session = requests.Session()

    image = session.get(cap_url, headers=head).content
    BytesIOObj = BytesIO()
    BytesIOObj.write(image)
    img = Image.open(BytesIOObj)
    img.show()
    capcha = input("请手动输入验证码:")

    html = session.post("http://jwxtxs.tust.edu.cn:46110/j_spring_security_check", data=postData, headers=head).text

    # html = session.get(gpa_url).text

    return html


print(get_html())
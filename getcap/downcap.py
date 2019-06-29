import requests
import time


def downimage(i):
    # 构建session
    session = requests.Session()
    # 建立请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Connection": "keep-alive"}
    # 验证码链接
    url = "http://jwxtxs.tust.edu.cn:46110/img/captcha.jpg"
    # 获取响应图片内容
    image = session.get(url, headers=headers).content
    # 保存本地
    with open("C://Users/sky/Desktop/urpcap/" + str(i) + ".jpg", "wb") as f:
        f.write(image)


if __name__ == "__main__":
    # 获取i张照片
    for i in range(100, 3000):
        downimage(i)
        print(i)
        print("成功\n")
        time.sleep(0.5)
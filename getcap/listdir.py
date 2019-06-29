import os

def img_num():
    x=0
    imgpath= os.path.abspath(os.path.join(os.getcwd(),"../.."))+"/capimg/"
    print(imgpath)

    img_names = os.listdir(imgpath)
    for img_name in img_names:
        x+=1
        print(img_name)
    return x
if __name__ == '__main__':
    print(img_num())

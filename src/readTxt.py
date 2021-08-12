# encoding:utf-8
def thunder_to_normal(url):
    print(url)
    f = open(url, 'r', encoding="utf-8", newline='')  # 返回一个文件对象
    dc = open("C:\\Users\\Administrator\\Desktop\\dc.txt", "a", encoding="utf-8", newline='')
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        flag = 'validation.ValidateException' in line
        if flag:
            print(line)
            dc.write(line)
        line = f.readline()

    f.close()


if __name__ == '__main__':
    thunder_to_normal("C:\\Users\\Administrator\\Desktop\\error.2021-08-10.0.log")

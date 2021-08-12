import base64


class changeWorker:
    @staticmethod
    def thunder_to_normal(thunder_url):
        if thunder_url.startswith('thunder://') or url.startswith('Thunder://'):
            real_url = thunder_url[10:]
        else:
            real_url = thunder_url
        real_url = bytes(real_url, encoding="utf8")
        missing_padding = 4 - len(url) % 4
        if missing_padding:
            real_url += b'=' * missing_padding
        print(real_url)
        mystr2 = base64.decodebytes(real_url)
        # result = str(mystr2,'utf-8')
        result = mystr2.decode()
        return result[2:-2]


if __name__ == '__main__':
    url = input('input thunder URL \n')
    print(changeWorker.thunder_to_normal(url))

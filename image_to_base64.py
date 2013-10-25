import base64


def main(image):
    f = open(image)
    data = f.read()
    f.close()

    string = base64.b64encode(data)

    out = open("test.txt", "w")
    out.write(string)
    out.close()

    convert = base64.b64decode(string)

    t = open("img/out.jpg", "w+")
    t.write(convert)
    t.close()


main("img/2.jpg")

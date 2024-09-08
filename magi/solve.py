a = "¢§¨©ª¯°±²·¸¹º¿ÀÁÂÇÈÉÊÏÐÑÒ×bghijopqrwxyzABGHIJOPQR\"'()*/012789:?@WXYZ_`a ¡ØÙÚß"
b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
o = "¨È¢Ð¨É¯ØÉqj ÇÊ¿jJ bÇj PqH ¸HÒ P É±H pAÁ±HÇJ ºbRBhÚ"


def solve(s):
  return ''.join(b[a.index(c)] for c in s)


print(solve(o))

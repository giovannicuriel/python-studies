a = 10
b = [1, 2, 3]
c = "last string"

def format1(a, b, c):
  ret = 'this is a: {}, b: {}, c: {}'.format(a, b, c)
  return ret
def format2(a, b, c):
  ret = 'this is a: %d, b: %s, c: %s' % (a, b, c)
  return ret
def format3(a, b, c):
  ret = ','.join(map(str, [a, b, c]))
  return ret
def format4(a, b, c):
  ret = f'this is a: {a}, b: {b}, c: {c}'
  return ret

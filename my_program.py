from get_age import get_age
from first import addition

try:
    a = get_age()
    b = get_age()
    c = get_age()
    result = addition(addition(a, b), c)
    print(result)
except BaseException as e:
    print(e.args)


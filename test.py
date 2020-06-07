# x = 5
# if x<3:
#     print('小')
# elif x>5:
#     print('中')
# else:
#     print('大')


# def test(x,y=3):
#     print(x)
#     print(y)
# test(2)


def test(x):
        if x==1:
                return 1
        return x*test(x-1)
print(test(3))
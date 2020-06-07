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


import pickle
d = dict(name='Bob', age=20, score=88)
x=pickle.dumps(d)
y=pickle.loads(x)
print(y)
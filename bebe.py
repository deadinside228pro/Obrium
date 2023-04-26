import requests


sub = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
print(sub)
if sub == 1337:
    print(sub, type(sub))
else:
    for i,b in sub.get('works').items():
        # print(i,b, len(b))
        for f in range(len(b)):
            if i+b[f] == 'rus7_1_rus':
                print(i+b[f], type(i),type(b[f]))


# sub = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
# x = [*sub]
# print(x)

# r = {'f':2132, 'w': 'wfwe'}
#
# for i in sub.keys():
#     print(i)

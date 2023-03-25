import requests

sub = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e05'}).json()
if sub == 1337:
    print(sub)
else:
    print('все норм')

# r = {'f':2132, 'w': 'wfwe'}
#
# for i in sub.keys():
#     print(i)

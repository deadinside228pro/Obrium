import requests

sub = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
if sub == 1337:
    print(sub)
else:
    print(sub.get('CompletedWorks'))
sub = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
x = [*sub]
print(x)

# r = {'f':2132, 'w': 'wfwe'}
#
# for i in sub.keys():
#     print(i)

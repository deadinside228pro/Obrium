import requests


subjects = requests.post("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
print(subjects)

l = list(map(lambda x: (x[0], x[1]), subjects.items()))

print(l)
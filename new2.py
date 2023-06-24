import requests
import os
data = requests.post("http://stepan4ek.pythonanywhere.com/post_info")
print(data.content)
with open("test2.py","w") as file:
    file.write(data.content.decode("utf-8"))
    file.close()
# os.system('test2.py')
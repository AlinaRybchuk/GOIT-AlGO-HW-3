file = open("cats_info_file.txt", "r")
with open("cats_info_file.txt", "r") as file:
    for text in file.readlines():
     file = (text.strip().split(","))
     
cats_list = [
    {"id":"60b90c1c13067a15887e1ae1", "name": "Tayson", "age":"3"},
    {"id":"60b90c2413067a15887e1ae2", "name": "Vika", "age":"1"}, 
    {"id":"60b90c2e13067a15887e1ae3", "name": "Barsik", "age":"2"}, 
    {"id":"60b90c3b13067a15887e1ae4", "name": "Simon", "age":"12"}, 
    {"id":"60b90c4613067a15887e1ae5", "name": "Tessi", "age":"5"}
]
print(cats_list)







  
  






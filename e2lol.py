import json, requests
url = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
resp = requests.get(url)
dict = json.loads(resp.text)

input_file = input("Where is you txt file ?") #write file directory
read_file_name = open(input_file, "r")
read_lines = read_file_name.readlines()
final_file = []
new_file = []
words3 = []


for row in read_lines: #Translation
    words = row.split(" ")
    words3 = words3 + words
    
for word in words3:
        #dict[word]
    if word in list(dict.keys()):
        new_file.append(dict[word])
    else:
        new_file.append(word)
   
sentence = str(" ".join(new_file))#translated content


file = open(str(input_file).replace(".txt", "_LOLcat.txt"), 'w') #Saving the new file
file.write(sentence)
file.close()
print("The file was saved on your directory.")
#1
from functools import reduce
nums = [5, 9, 4, 8]
result = reduce(lambda x, y: x * y, nums)
print(result)

#2
s = "Bikini Botom"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Upper case letters:", upper)
print("Lower case letters:", lower)

#3
string = "madam"
is_palindrome = string == string[::-1]
print(is_palindrome)

#4
import time, math
num = 25100
ms = 2123
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} miliseconds is {math.sqrt(num)}")

#5
t = (True, True, True)
print(all(t))

#6
import os
path = "."
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])
print("All:", os.listdir(path))

#7
import os
path = "."
print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#8
import os
path = "example.txt"
if os.path.exists(path):
    dirname = os.path.dirname(path)
    filename = os.path.basename(path)
    print("Directory:", dirname)
    print("Filename:", filename)
else:
    print("Path does not exist")

#9
with open("file.txt", "r") as f:
    print("Number of lines:", sum(1 for _ in f))

#10
lst = ["патрик", "спанчбоб", "cвидвард"]
with open("list.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")

#11
import string
for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()

#12
with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
    dst.write(src.read())

#13
import os
path = "file_to_delete.txt"
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted")
else:
    print("Cant delete file or file dont exist")

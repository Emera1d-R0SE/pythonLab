print("mode1")
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
print("\n ___file closed__")


print("mode2(line by line)")
with open("file.txt", "r") as f:
    print("Line1: ", f.readline(), end="\n")
    print("Line2: ", f.readlines(), end="\n")
print(" ")

print("mode3 (all line as a list)")
with open("file.txt","r") as f:
    print(f.readlines())
print("")


print("mode4 (splits the words)")
with open("file.txt","r") as f:
    #print(f.readlines())
    for line in f:
        print(line.split(" "))
print("")










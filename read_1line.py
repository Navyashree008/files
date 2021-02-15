# to get space between one line
f = open("people1")
print(f.readline())
print(f.readline())
f.close()

# to not get space between lines
f = open("people1")
print(f.readline(),end="")
print(f.readline(),end="")
f.close()
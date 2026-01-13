text = "Hello World"

print(text[::-1])
print("end")

print("wow".join([text,"!!"]))

text2 = "Python Programming"

print(text2[0])
print(text2[-1])
print(len(text2))
print(text2.lower())

print(text2[0:6])
print(text2.replace("Python","Java"))

print(text2)

s = 'hello world. this sentance will print in the next line. this is another sentance.'
print(s)

print(len(s.split(".")))
print(len(s.split(" ")))
words = s.split(" ")
print(words)

sentences = s.split(".")
sentences = sentences[:-1]
print(f"sentances: {sentences}")
print(60*"=")

numbers = [0,1,2,3,4,5]

print(numbers[2])
numbers[5] = 10
print(numbers)
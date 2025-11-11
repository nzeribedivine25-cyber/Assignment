#ESCAPE CHARACTERS
txt = "We are the so-called \"Vikings\" from the north"
print(txt)

txt = 'it\'s alright'
print(txt)

txt = "This will insert one \\ (backslash)"
print(txt)

txt = "This will insert one, \n come here now"
print(txt)

txt = "i am a techrise \r participant"
print(txt)

txt = "i am who \t i am"
print(txt)

txt = "i am you and \b you are me"
print(txt)

txt = "you fed \f us when"
print(txt)

txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)  

#string methods
text = "hello world"
print(text.capitalize())

text = "Grüße"
print(text.casefold())

text = "data" 
print(text.center(10, "*"))

text = "HELLO" 
print(text.lower())

text = "HeLlO" 
print(text.swapcase())

text = "data science" 
print(text.title())

text = "data" 
print(text.upper())

text = "42"
print(text.zfill(5))

text = "banana" 
print(text.count("a"))

text = "file.txt" 
print(text.endswith(".txt"))

text = "apple" 
print(text.find("p"))

text = "apple" 
print(text.index("l"))

text = "banana" 
print(text.rfind("a"))

text = "banana" 
print(text.rindex("n"))

text = "Python" 
print(text.startswith("Py"))

words = ["Hello", "World"] 
print("-".join(words))

text = "hi" 
print(text.ljust(5, "."))

text = " data" 
print(text.lstrip())

text = "name:bob" 
print(text.partition(":"))

text = "hi" 
print(text.rjust(5, "."))

text = "a,b,c" 
print(text.rpartition(","))

text = "one,two,three" 
print(text.rsplit(",", 1))

text = "data   " 
print(text.rstrip())

text = "red,blue" 
print(text.split(","))

text = "Line 1\nLine 2"
print(text.splitlines())

text = "  data  " 
print(text.strip())

text = "Data123" 
print(text.isalnum())

text = "Python" 
print(text.isalpha())

text = "abc" 
print(text.isascii())

text = "123"
print(text.isdecimal())

text = "123" 
print(text.isdigit())

text = "my_var" 
print(text.isidentifier())

text = "hello" 
print(text.islower())

text = "123" 
print(text.isnumeric())

text = "data" 
print(text.isprintable())

text = " \t\n" 
print(text.isspace())

text = "Hello World" 
print(text.istitle())

text = "DATA" 
print(text.isupper())

text = "data" 
print(text.encode("utf-8"))

name = "Alex" 
print("Hello, {}!".format(name))

data = {'x': 10} 
print("The value is {x}".format_map(data))

text = "cat dog" 
print(text.replace("cat", "fish"))

table = str.maketrans("a", "o") 
print(table)

text = "data" 
print(text.translate(table))
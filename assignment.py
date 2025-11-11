#SECTION A~ STRING BASICS
#Q1
word1 = 'Python'
word2 = "Programming"
word3 = """Language."""
print(word1, word2, word3)

#Q2
sentence = ("Python is fun to learn")
print(sentence)


#Q3
multiline_str ="""Python is powerful. 
It is easy to learn. 
It is loved by developers"""
print(multiline_str)


#SECTION B~ STRINGS AS ARRAYS
#Q4
X = "PYTHON"
print(X[0])
print(X[3])
print(X[5])


#Q5
for varlan in "Python":
  print(varlan)


#SECTION C~ STRING LENGHT AND CHECKING
#Q6
fruit = "Banana"
print (len("fruit"))

#Q7
word = ('learning Python is cool')
# print('Python' in word )
print("Yes,'Python' is found!")

#Q8
# print('Java' in word)
print("No,'Java' is not found")

#BONUS TASK
#Q9
message = "Coding is fun"
count = 0
for char in message:
    if char == 'n':
        count += 1
print("total count of 'n':", count)


#Q10
Poem = """PYTHON IS NOT JUST A SNAKE,
IT'S ALSO A PROGRAMMING LANG..
I LOVE PYTHON."""
print(Poem)






#VARIABLES AND STRINGS

#SECTION A~ VARIABLES
#Q1
name = 'Ada'
age = '18'
school = ' Bright Future Academy'
print(f"My name is {name}, i am {age} years old, and i attend {school}.")


#Q2
country = "Nigeria"
capital = "Abuja"
print(f'The capital of {country} is {capital}.')


#Q3
First_name = 'John'
Middle_name = 'Paul'
Last_name = 'Okoro'
print(f'Full_name: {First_name} {Middle_name} {Last_name}')


#Q4
food = 'Rice'
drink = 'Juice'
print(f"I love eating {food} and {drink}")
z = ["1", "3", "2", "4", 'Alice', 'Bob'] 
z.sort() 
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.") 

multi_line = """Hello there! 
How are you? 
I'm fine.""" 
print(multi_line) 

spam = 'Hello World' 

s= spam.lstrip('Hel')
print(s) 
s= spam.rstrip('rld') 
print(s)
s= spam.strip() 
print(s)

string=', '.join(['cats', 'rats', 'bats']) 
print(string)
string=' '.join(['My', 'name', 'is', 'Simon']) 
print(string)
string='ABC'.join(['My', 'name', 'is', 'Simon']) 
print(string)
string='My name is Simon'.split() 
print(string)
string='MyABCnameABCisABCSimon'.split('ABC') 
print(string)
string='My name is Simon'.split('m')
print(string)

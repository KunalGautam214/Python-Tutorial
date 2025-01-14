
message = 'Hello World!'
print(message)

message = """Hello World!
Welcome to my world"""
print(message)

message = "Hello World!"
print(len(message))

message = "Hello World!"
print(message[0:5])

message = "Hello World!"
print(message[6:])

message = "Hello World!"
print(message.lower())

message = "Hello World!"
print(message.upper())

message = "Hello World!"
print(message.count('l'))

message = "Hello World!"
print(message.find('l'))

message = "Hello World!"
print(message.find('z'))

message = "Hello World!"
new_message = message.replace('World', 'Universe')
print(new_message)

greeting = "Hello"
name = 'Code with KG'
message = greeting + ' ' + name
print(message)

greeting = "Hello"
name = 'Code with KG'
message = '{} {}'.format(greeting, name)
print(message)

greeting = "Hello"
name = 'Code with KG'
message = f'{greeting} {name}'
print(message)

print(dir(str))

print(help(str.lower))
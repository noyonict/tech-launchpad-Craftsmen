# 0 1 2 3 4 5 6 7 8 9 10
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
message = 'Hello Word!'
message[0] = 'M'
print(message)
print(len(message))

print(message[1])
print(message[0])
print(message[10])
print(message[-5])
print(message[-2])
# print(message[string_index: end_index: step])
print(message[::3])
print(message[::-2])
print(message[::-0])  # ValueError slice step cannot be zero
# mem message -> 'Hello Word!'
# mem message -> 'Mello Word! MMM'

message = 'Hello Word! HHH'
print(id(message))
new_message = message.replace('H', 'M')
print(message)
print(new_message)
print(id(message))
print(list(message).pop(6))
print(message)

print(message.replace('Hello', 'Hlekl asdkfjlskfj '))
message = ' Hello Word!e HHH     '
for i in message:
    print(i)
print(dir(message))
print(message.upper())
print(message.lower())
print(message.title())
user_input = input('Enter something: ').strip()
print(message)
print(message.strip('H e'))
print(message.rstrip('H e'))
print(message.lstrip('H e'))

message = 'Hello Word!'
new_message = message[:6] + message[7:]
print(new_message)


def remove_specific_index(original_message, index_point):
    initial_message = original_message[:index_point]
    end_message = original_message[index_point+1:]
    new_message = initial_message + end_message
    return new_message


print(remove_specific_index(message, 6))

message = 'Hello Word!'
message = list('Hello Word!')

greeting = 'Hello'
name = 'Sakib'
message_1 = greeting + ' ' + name + ', Welcome Back!' + str(5)
message_2 = '{0} {1}, Welcome Back! {0}'.format(greeting, name)
message_3 = f'{greeting} {name}, Welcome Back! {str(5)} {greeting}'
print(message_1)
print(message_2)
print(message_3)

print(help(str))


message = 'Hello World!'
message_split = message.split('World')
print(message_split)

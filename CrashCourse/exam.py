# 1.
print(7 ** 4)

# 2.
s = 'Hi there Sam!'
list1 = s.split(' ')
print(list1)

# 3.

planet = 'Earth'
diameter = '12742'

print('The diameter of {0} is {1} kilometers'.format(planet, diameter))

# 4.
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2][0])


# 5.
def domain_get(domain):
    index = domain.index('@')
    result_domain = domain[index + 1:]
    return result_domain


print(domain_get('dkasarov@unwe.bg'))


# 6.
def fing_dog(dog):
    if dog.lower().find('dog') != -1:
        return True
    else:
        return False


print(fing_dog('Is there a dog here?'))
print(fing_dog('Is there a cat here?'))


# 7.
def count_dog(dog):
    count = 0
    list = dog.lower().split(' ')
    for d in list:
        if d == 'dog':
            count += 1
    return count


print(count_dog('This dog is faster than the other dog dude!'))

# 8.
seq = ['soup', 'dog', 'salad', 'cat', 'great']
result = list(filter(lambda x: x[0] == 's', seq))
print(result)


# 9.
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    tickets = ('No ticket', 'Small ticket', 'Big ticket')
    if speed <= 60:
        return tickets[0]
    elif speed in range(61, 81):
        return tickets[1]
    elif speed >= 81:
        return tickets[2]


print(caught_speeding(66, True))

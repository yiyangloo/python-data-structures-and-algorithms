hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
print(len(hero))

# 2. Add 'black panther' at the end of this list
hero.append('black panther')
print(hero)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
hero.remove('black panther')
hero.insert(3, 'black panther')
print(hero)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
hero[1:3] = ['doctor strange']
print(hero)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
hero.sort()
print(hero)

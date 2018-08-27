#!/usr/bin/python3
import array

symbols = '#!/usr/bin/python3'
my_tuple = tuple(ord(symbol) for symbol in symbols)
print(my_tuple)

# what does first parameter mean?
my_array = array.array('I', (ord(symbol) for symbol in symbols))

print(my_array)

colors = ['yellow', 'black', 'brown', 'pink', 'white']
sizes = ['S', 'L', 'XL', 'M', 'XXL']
# using a generator expression would save the expense of building a list with
generated_shirts = ('%s %s' % (c, s) for c in colors for s in sizes)

for tshirt in generated_shirts:
    print(tshirt)

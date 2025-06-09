# Example-1
print("tharun")

#Formatting with placeholders
print("I'm going to inject %s here." %'tharun')
print("I'm going to inject %s text here, and %s text here.%s" %('some','more','tharu'))

x, y , z= 'some', 'more' , 'tharun'
print("I'm going to inject %s text here, and %s text here. %s"%(x,y , z))


#Format conversion methods.
print('He said his name was %s.' %'Fred') #He said his name was Fred
print('He said his name was %r.' %'<Fred') # He said his name was '<Fred'


print('I once caught a fish %s.' %'this \tbig') # I once caught a fish this  big
print('I once caught a fish %r.' %'this \tbig') # I once caught a fish 'this \tbig'

print('I wrote %s programs today.' %3.75) #3.75
print('I wrote %d programs today.' %3.75) # 3

#Padding and Precision of Floating Point Numbers
print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))
print('Floating point numbers: %25.2f' %(13.144))


#Multiple Formatting
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))


# Formatting with the .format() method
print('This is a string with an {}'.format('insert'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))

#Alignment, padding and precision with .format()
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

#You can pass an optional <,^, or > to set a left, center or right
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))


print('This is my ten-character, two-decimal number:%10.2f' %13.579) # Field width
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

#Formatted String Literals (f-strings)
name = 'Tharun'
print(f"He said his name is {name}.")
print(f"He said his name is {name!r}")


# Example-1
print("gautham")

#Formatting with placeholders
print("I'm going to inject %s here." %'gautham')
print("I'm going to inject %s text here, and %s text here.%s" %('some','more','gautham'))

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

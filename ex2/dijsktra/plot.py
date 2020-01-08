import matplotlib.pyplot as plt

# Hardcoded memory accesses
x = [92943465,
    93150336,
    141722318]
# Hardcoded memory footprints
y = [707.7 ,
    941.8,
    360.7]

plt.plot(x,y,'bo')

for x,y in zip(x,y):

    if (x==92943465) & (y==707.7):
        label = 'sll'
    if (x==93150336) & (y==941.8):
        label = 'dll'
    if (x==141722318) & (y==360.7):
        label = 'dyn_arr'


    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# naming axis
plt.xlabel('Memory accesses')
plt.ylabel('Memory footprint (KB)')

# giving a title to my graph
plt.title('DDTR - data types comparison')

plt.show()

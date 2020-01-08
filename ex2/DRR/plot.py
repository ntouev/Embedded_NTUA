import matplotlib.pyplot as plt

# Hardcoded memory accesses
x = [67058967,
    67696447,
    469222244,
    67069137,
    67706225,
    469238457,
    67587245,
    68245731,
    469946613]
# Hardcoded memory footprints
y = [798.8,
    980.3,
    1111,
    823,
    983.3,
    1128,
    760.2,
    928.5,
    1075]

plt.plot(x,y,'bo')

for x,y in zip(x,y):

    if (x==67058967) & (y==798.8):
        label = 'sll-sll'
    if (x==67696447) & (y==980.3):
        label = 'sll-dll'
    if (x==469222244) & (y==1111):
        label = 'sll-dyn_arr'
    if (x==67069137) & (y==823):
        label = 'dll-sll'
    if (x==67706225) & (y==983.3):
        label = 'dll-dll'
    if (x==469222244) & (y==1128):
        label = 'dll-dyn_arr'
    if (x==67587245) & (y==760.2):
        label = 'dyn_arr-sll'
    if (x==68245731) & (y==928.5):
        label = 'dyn_arr-dll'
    if (x==	469946613) & (y==1075):
        label = 'dyn_arr-dyn_arr'

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

import numpy as np
import matplotlib.pyplot as plt
import csv


# 1. Generate a Sine and a Cosine wave
x = np.arange(0, 4*np.pi-1, 0.1)
y = np.sin(x)
z = np.cos(x)

# 2. Plot (time vs sine) and (time vs cosine)
plt.plot(x,y)
plt.plot(x,z)
plt.savefig('output.png', bbox_inches='tight')
plt.show()

# 3. Store the sine data in a variable name “amplitude1” and cosine data in a variable name “amplitude2”.
amplitude1 = np.sin(x)
amplitude2 = np.cos(x)

# 4. Make an array with name “amplitude” using numpy and store the “time”, “amplitude1” and “amplitude2” data in the variable “amplitude”.
amplitude = np.asarray([x,amplitude1, amplitude2])

# 5. Store the data of “amplitude” in .csv file.
np.savetxt("amplitude.csv",amplitude,'%s',delimiter=",")


# 6. Make a function to open the saved file (file saved with .csv extension) and read the data from this file. 
with open('amplitude.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
    data = np.genfromtxt("amplitude.csv", delimiter=",",names=["x","y"])

# 7. After reading the data, plot the data using matplotlib library. 
plt.plot(data['x'],data['y'])

# 8. Save the figure(s) (with .png extension) using python code in a folder.
plt.savefig('output1.png', bbox_inches='tight')
plt.show()
plt.plot3(x,y,z)



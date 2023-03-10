# Example of simple data colection. Random daily temperature of a moanth.
measurements_v=[15.136, 16.279, 17.324, 18.709, 19.288, 20.121, 21.938, 22.306,
                23.578, 24.446, 25.321, 26.059, 27.178, 28.152, 29.046, 15.494, 
                16.721, 17.911, 18.776, 19.501, 20.731, 21.179, 22.724, 23.077, 
                24.654, 25.065, 26.401, 27.872, 28.106, 29.525, 15.278]

# Define the minimum and maximum values from user.
min_v =float(input("Please insert minimum value to be filtered on data results: "))
max_v=float(input("Please insert maximum value to be filtered on data results: "))

# Chekking for proper input values.
if max_v < min_v:
    print("Try again, MAX value can't be less than MIN value!")

# Function that keeps values in the range of a given min and max.
def minmax(x):
    if x >= min_v and x <= max_v:
        return x
    
# Using filter method with a given values.
filtered_measurements = list(filter(minmax, measurements_v))

# Print the filtered measurements to standart.
print("Listed values in the range: ",filtered_measurements)

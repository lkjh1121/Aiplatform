from sklearn import datasets

# Load the digits dataset
digits = datasets.load_digits()
print(digits.data.shape)

import matplotlib.pyplot as plt

# Display the last digit
plt.gray()
plt.matshow(digits.images[0])
plt.show()

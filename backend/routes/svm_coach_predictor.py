import numpy as np
import pickle
from sklearn import svm

# Sample training data: (Train Number, Coach ID) -> Position at platform
# Assume we have past data of how coaches were placed at stations.
train_data = np.array([
    [12345, 1, 10], [12345, 2, 15], [12345, 3, 20],  # Train 12345
    [67890, 1, 12], [67890, 2, 18], [67890, 3, 25],  # Train 67890
    [11111, 1, 5], [11111, 2, 10], [11111, 3, 15]   # Train 11111
])

# Features: Train Number & Coach ID
X = train_data[:, :2]

# Labels: Position at Platform
y = train_data[:, 2]

# Train the model
model = svm.SVC(kernel='linear')
model.fit(X, y)

print("✅ Model trained & saved!")

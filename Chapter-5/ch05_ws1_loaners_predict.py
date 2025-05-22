import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset from CSV
data = pd.read_csv('loaners-repayment-data.csv')

# Drop unnecessary columns: 'LastName', 'FirstName', 'PhoneNumber'
data = data.drop(columns=['LastName', 'FirstName', 'PhoneNumber'])

# Separate features (X) and target (y)
X = data[['Age', 'Income', 'DebtAmount', 'CreditScore', 'LoanDuration', 'MissedPayments']]
y = data['Repay']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the neural network model
model = Sequential([
    Input(shape=(X_train.shape[1],)),  # Input layer specifying the input shape
    Dense(32, activation='relu'),      # First hidden layer with 32 neurons
    Dense(64, activation='relu'),      # Second hidden layer with 64 neurons
    Dense(1, activation='sigmoid')     # Output layer with 1 neuron (for binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)

print(f'Test Accuracy: {test_acc}')

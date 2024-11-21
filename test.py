import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd

# Assume you already have the scaled data: X_scaled (features) and y_train_scaled (target)
# Also, x_test_scaled (test features) and y_test_scaled (test target)

# Define the model
def build_budget_model(input_shape):
    input_layer = Input(shape=(input_shape,))
    # First dense layer with Batch Normalization and Dropout
    dense = Dense(128, activation='relu', kernel_initializer='he_normal')(input_layer)
    dense = BatchNormalization()(dense)
    dense = Dropout(0.2)(dense)
    
    # Second dense layer
    dense = Dense(64, activation='relu', kernel_initializer='he_normal')(dense)
    dense = BatchNormalization()(dense)
    dense = Dropout(0.2)(dense)
    
    # Third dense layer
    dense = Dense(32, activation='relu', kernel_initializer='he_normal')(dense)
    
    # Output layer (1 neuron for regression)
    output_layer = Dense(1, activation='linear', kernel_initializer='he_normal')(dense)
    
    return Model(inputs=input_layer, outputs=output_layer)

# Build the model
model = build_budget_model(X_scaled.shape[1])

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=1e-4),  # Adjust learning rate for stability
    loss='mse',  # Mean Squared Error for regression
    metrics=['mae']  # Mean Absolute Error for easier interpretability
)

# Print model summary
model.summary()

# Train the model
history = model.fit(
    X_scaled,
    y_train_scaled,
    validation_split=0.2,  # Use 20% of the training data for validation
    epochs=50,  # You can increase epochs if needed
    batch_size=32,
    verbose=1
)

# Evaluate the model on test data
test_loss, test_mae = model.evaluate(x_test_scaled, y_test_scaled, verbose=1)
print(f"Test Loss (MSE): {test_loss}")
print(f"Test MAE: {test_mae}")

# Make predictions
y_pred_scaled = model.predict(x_test_scaled)

# If the target is scaled, reverse scaling (optional)
# Assuming 'scaler_y' is the scaler used for y_train_scaled
# y_pred_original = scaler_y.inverse_transform(y_pred_scaled)
# y_test_original = scaler_y.inverse_transform(y_test_scaled.reshape(-1, 1))

# Calculate additional metrics
mse = mean_squared_error(y_test_scaled, y_pred_scaled)
mae = mean_absolute_error(y_test_scaled, y_pred_scaled)
r2 = r2_score(y_test_scaled, y_pred_scaled)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"R² Score: {r2}")

# Create a comparison DataFrame
comparison = pd.DataFrame({
    "Actual": y_test_scaled.flatten(),
    "Predicted": y_pred_scaled.flatten()
})
print(comparison.head())

# Optional: Plot training history
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Validation Loss')
plt.show()

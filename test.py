import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Define input shape based on the number of features
input_shape = X_scaled.shape[1]

# Build the model
def build_regression_model(input_shape):
    # Input layer
    input_layer = Input(shape=(input_shape,), name="numerical_input")
    
    # Dense layers with dropout
    dense_layer = Dense(64, activation='relu', kernel_initializer='he_normal')(input_layer)
    dense_layer = Dropout(0.2)(dense_layer)
    dense_layer = Dense(64, activation='relu', kernel_initializer='he_normal')(dense_layer)
    dense_layer = Dropout(0.2)(dense_layer)
    dense_layer = Dense(32, activation='relu', kernel_initializer='he_normal')(dense_layer)
    
    # Output layer (single value for regression)
    output_layer = Dense(1, activation='linear', kernel_initializer='he_normal', name="output")(dense_layer)
    
    # Model definition
    model = Model(inputs=input_layer, outputs=output_layer)
    return model

# Instantiate the model
model = build_regression_model(input_shape)

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=1e-3),
    loss='mse',  # Mean Squared Error
    metrics=['mae']  # Mean Absolute Error
)

# Print model summary
model.summary()

# Train the model
history = model.fit(
    X_scaled,
    y_train_scaled,
    validation_split=0.2,  # Use 20% of the data for validation
    epochs=50,
    batch_size=32,
    verbose=1
)

# Evaluate the model
results = model.evaluate(X_scaled, y_train_scaled, verbose=0)
print(f"Loss: {results[0]}, MAE: {results[1]}")

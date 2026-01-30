import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        
        # Parameters (like sklearn)
        self.coef_ = None        # theta_1
        self.intercept_ = None   # theta_0
        
        self.losses_ = []        # store SSE

    def fit(self, X, y):
        # Ensure numpy arrays
        X = np.array(X)
        y = np.array(y)

        # Reshape if X is 1D
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        n_samples, n_features = X.shape

        # Initialize parameters
        self.coef_ = np.zeros(n_features)
        self.intercept_ = 0

        # Gradient Descent
        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.coef_) + self.intercept_

            # Gradients
            dw = (2 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (2 / n_samples) * np.sum(y_pred - y)

            # Update parameters
            self.coef_ -= self.learning_rate * dw
            self.intercept_ -= self.learning_rate * db

            # SSE loss
            loss = np.sum((y - y_pred) ** 2)
            self.losses_.append(loss)

    def predict(self, X):
        X = np.array(X)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        return np.dot(X, self.coef_) + self.intercept_

    def mse(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def plot_training(self, X, y):
        X = np.array(X)
        y = np.array(y)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        # Plot SSE
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(self.losses_)
        plt.title("SSE Over Iterations")
        plt.xlabel("Iterations")
        plt.ylabel("SSE")

        # Plot regression line
        plt.subplot(1, 2, 2)
        plt.scatter(X, y, color="blue", label="Data")
        plt.plot(X, self.predict(X), color="red", label="Regression Line")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()

        plt.tight_layout()
        plt.show()

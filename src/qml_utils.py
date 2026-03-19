# src/qml_utils.py
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

def load_mnist_binary(n_samples=200,
                      n_features=2,
                      random_state=42):
    from sklearn.datasets import load_digits
    digits = load_digits()
    X = digits.data
    y = digits.target

    # binary: digit 0 vs digit 1
    mask = y < 2
    X = X[mask]
    y = y[mask]

    # subsample
    np.random.seed(random_state)
    idx = np.random.choice(
        len(X), n_samples, replace=False
    )
    X = X[idx]
    y = y[idx]

    # PCA to reduce to n_features
    pca = PCA(n_components=n_features)
    X = pca.fit_transform(X)

    # normalize to [0, 1]
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    return X, y

if __name__ == "__main__":
    X, y = load_mnist_binary()
    print(f"X shape : {X.shape}")
    print(f"y shape : {y.shape}")
    print(f"classes : {np.unique(y)}")
    print(f"feature range : [{X.min():.2f}, {X.max():.2f}]")
    print("qml_utils ready!")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Wczytanie danych
iris = load_iris()
X = iris.data
y = iris.target

# 2. Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Utworzenie modelu
model = KNeighborsClassifier(n_neighbors=1)

# 4. Trenowanie
model.fit(X_train, y_train)

# 5. Predykcja
y_pred = model.predict(X_test)

# 6. Wynik
print("Dokładność modelu:", accuracy_score(y_test, y_pred))

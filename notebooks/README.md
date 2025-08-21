## Zadania w repozytorium
1. Task 1 – Hello ML (KNN na Iris)
2. Task 2 – Podstawowe EDA na Iris
3. Task 2b – Rozszerzone EDA na Iris (histogramy, korelacje, PCA, skalowanie)
3. Task 3 - Make_moons, brudne dane, granice dezycyjne.
4. Task 4 - Granice decyzyjne różnych modeli (make_moons)
   Cel: porównanie, jak różne algorytmy klasyfikacyjne dzielą dane w 2D.
   Modele i obserwacje:

   KNN (k=5) – granice gładkie, dopasowują się do kształtu księżyców. Radzi sobie dobrze, choć czasem łapie szum.

   Logistic Regression – granica liniowa, nie radzi sobie z rozdzieleniem półksiężyców → niedouczenie (underfitting).

   Decision Tree (max_depth=5) – granice prostokątne, poszarpane. Głębsze drzewa byłyby bardzo przeuczone → tendencja do overfittingu.

   SVM (RBF kernel) – granice gładkie i nieliniowe, najlepiej oddzielają klasy. Najwyższa dokładność w tym eksperymencie.

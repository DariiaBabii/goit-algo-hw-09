## Висновки

Проведено дослідження з метою порівняння ефективності жадібного алгоритму та алгоритму динамічного програмування, базуючись на часі їх виконання.

Час виконання було виміряно з використанням модуля `timeit` у Python.

**Результати:**
Для проведення тестування було взято значення 102134 монет. Отримано такі результати:
```
|Algoritms           | Time                
------------------------------------------------------------
|Greedy algorithm    | 0.00001             
|Dynamic programming | 1.07722 
```

З результатів бачимо, що жадібний алгоритм значно швидший за алгоритм динамічного програмування, особливо для великих сум. Втім, потрібно пам'ятати про точність. Жадібний алгоритм може бути неефективним у певних умовах і не завжди гарантує оптимальне рішення, на відміну від алгоритму динамічного програмування, який завжди забезпечує точний результат, хоч і вимагає більше часу для виконання.
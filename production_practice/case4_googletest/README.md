# Кейс-задача № 4 — контрактные тесты GoogleTest

В проекте описаны интерфейсы трёх контейнеров и тесты их ожидаемого поведения:

- очередь `IQueue<T>`: `push`, `pop`, `empty`, порядок FIFO;
- максимальная куча `IMaxHeap<T>`: `push`, `pop`, `empty`, извлечение от большего к меньшему;
- бинарное дерево поиска `IBinaryTree`: `push`, `pop`, `search`.

По условию практики реализации контейнеров не входят в работу. Фабричные функции объявлены в `include/containers.hpp`, а конкретная реализация подключается к тестовой сборке отдельным исходным файлом.

## Структура

```text
case4_googletest/
├── CMakeLists.txt
├── include/
│   └── containers.hpp
└── tests/
    └── containers_test.cpp
```

## Проверка интерфейсной части

По умолчанию CMake проверяет конфигурацию проекта без реализации контейнеров:

```bash
cmake -S . -B build
cmake --build build
```

## Запуск контрактных тестов с реализацией

Укажите путь к файлу, который определяет функции `make_queue`, `make_max_heap` и `make_binary_tree`:

```bash
cmake -S . -B build-tests \
  -DBUILD_CONTRACT_TESTS=ON \
  -DCONTAINER_IMPLEMENTATION=/absolute/path/to/containers_implementation.cpp
cmake --build build-tests
ctest --test-dir build-tests --output-on-failure
```

Для сборки тестов требуется установленный GoogleTest, доступный через `find_package(GTest)`.

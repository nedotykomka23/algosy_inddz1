def test_traversal():
    dll = DoublyLinkedList()

    # 1. Тест обхода пустого списка
    assert dll.forward_traverse() == []
    assert dll.backward_traverse() == []
    assert list(dll) == []
    assert list(reversed(dll)) == []

    # Наполнение списка: [10, 20, 30, 40]
    for val in [10, 20, 30, 40]:
        dll.append(val)

    # 2. Прямой и обратный обход
    assert dll.forward_traverse() == [10, 20, 30, 40]
    assert dll.backward_traverse() == [40, 30, 20, 10]

    # 3. Прямой и обратный обход через встроенные протоколы (__iter__ и __reversed__)
    assert [x for x in dll] == [10, 20, 30, 40]
    assert [x for x in reversed(dll)] == [40, 30, 20, 10]

    # 4. Обход в обоих направлениях после модификации списка
    dll.insert_at(2, 25)  # [10, 20, 25, 30, 40]
    dll.delete_at(0)  # [20, 25, 30, 40]

    assert dll.forward_traverse() == [20, 25, 30, 40]
    assert dll.backward_traverse() == [40, 30, 25, 20]
    assert list(dll) == [20, 25, 30, 40]
    assert list(reversed(dll)) == [40, 30, 25, 20]

    print("Тесты успешно пройдены!")


if __name__ == "__main__":
    test_traversal()

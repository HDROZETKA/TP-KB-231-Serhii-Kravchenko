import pytest
from lab_02 import students, addNewElement, deleteElement, updateElement


def test_add_new_element():
    initial_len = len(students)
    addNewElement()
    assert len(students) == initial_len + 1
    assert any(student["name"] == "Serhii" for student in students)


def test_update_element():
    updateElement()
    updated_student = next(student for student in students if student["name"] == "Serhii")
    assert updated_student["age"] == 21


def test_delete_element():
    initial_len = len(students)
    deleteElement()
    assert len(students) == initial_len - 1
    assert not any(student["name"] == "Serhii" for student in students)

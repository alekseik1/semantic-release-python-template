import pytest
from hypothesis import given
from semantic_release_python import min_, min_multi
from hypothesis import strategies as st


@given(st.floats(allow_nan=False), st.floats(allow_nan=False))
def test_min_two(a, b):
    assert min(a, b) == min_(a, b)


@given(st.lists(st.floats(allow_nan=False), min_size=1))
def test_min_many(l):
    assert min(l) == min_multi(*l)


def test_min_error():
    with pytest.raises(ValueError):
        min_multi()
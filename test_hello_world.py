# test_hello_world.py
import pytest
from hello_world import hello_world 

def test_hello_world():
    assert hello_world() == "Hello, World!"
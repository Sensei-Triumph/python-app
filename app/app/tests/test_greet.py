from app.greet import greet

def test_greet():
    assert greet("Jenkins") == "Hello, Jenkins!"
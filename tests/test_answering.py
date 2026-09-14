from copilot.answering import answer


def test_answer_returns_the_question():
    result = answer("What is compliance?")
    assert "compliance" in result.lower()
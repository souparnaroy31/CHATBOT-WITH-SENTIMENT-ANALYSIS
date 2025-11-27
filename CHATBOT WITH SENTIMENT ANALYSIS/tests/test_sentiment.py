from sentiment import analyze_sentiment

def test_positive_sentiment():
    sentiment, score = analyze_sentiment("I love this!")
    assert sentiment == "Positive"

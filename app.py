import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text):
        """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

        dict: A dictionary containing polarity, subjectivity, and assessment
    """
        blob = TextBlob(text)
        sentiment = blob.sentiment

        return {
                "polaity": round(sentiment.polarity, 2), # -1 (negative) to 1 (positive)
                "subjectivity": round(sentiment.subjectivity, 2), # 0 (objective) to 1 (subjective)
                "assessment": "Positive" if sentiment.polarity > 0 else "Negative" if sentiment.polarity < 0 else "Neutral"
        }

# Create the Gradio interface
demo = gr.Interface(
        fn=sentiment_analysis,
        inputs=gr.Textbox(placeholder="Enter text to analyze..."),
        outputs=gr.JSON(),
        title="Text Sentiment Analysis",
        description="Analyze the sentiment of text using TextBlob"
)

# Launch the interface and mcp server
if __name__ == "__main__":
        demo.launch(mcp_server=True)
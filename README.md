# Text Sentiment Analysis

**Source:** Based on code from the [Hugging Face MCP course Unit 2: Gradio client](https://huggingface.co/learn/mcp-course/unit2/gradio-client).

A simple Gradio web application to analyze the sentiment of text using TextBlob.

## Features

* **Polarity**: Score from -1 (negative) to 1 (positive).
* **Subjectivity**: Score from 0 (objective) to 1 (subjective).
* **Assessment**: Classification as `Positive`, `Neutral`, or `Negative` based on polarity.
* Minimal dependencies and easy to set up.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/seanpoyner/mcp-sentiment.git
   cd mcp-sentiment
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Launch the Gradio interface:

```bash
python app.py
```

By default, Gradio will host the interface locally at `http://localhost:7860`.

To launch with `mcp_server` enabled:

```bash
python app.py --mcp_server=True
```

## API Reference

The core function is defined in `app.py`:

```python
def sentiment_analysis(text: str) -> dict:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing:
            - polarity (float): -1 (negative) to 1 (positive).
            - subjectivity (float): 0 (objective) to 1 (subjective).
            - assessment (str): "Positive", "Neutral", or "Negative".
    """
```

## Contributing

Contributions and improvements are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
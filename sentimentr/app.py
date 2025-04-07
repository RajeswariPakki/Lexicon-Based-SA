# app.py code

from flask import Flask, render_template, request
from sentimentr import Sentiment  # Assuming your Sentiment class is in sentimentr.py

app = Flask(__name__)
    
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    single_text_results = None
    multiple_text_results = None
    input_type = None

    if request.method == "POST":
        input_type = request.form.get("input_type")  # 'single' or 'multiple'
        input_text = request.form.get("input_text")

        # Create an instance of Sentiment
        s = Sentiment

        if input_type == "single":
            # Single text input: Process and get detailed output
            polarity_score = s.get_polarity_score(input_text.strip())
            single_text_results = {
                "text": input_text.strip(),
                "polarity": polarity_score,
            }
        elif input_type == "multiple":
            # Multiple text input: Process each line
            text_docs = input_text.strip().split("\n")
            multiple_text_results = []
            for doc in text_docs:
                polarity_score = s.get_polarity_score(doc.strip())
                multiple_text_results.append({
                    "text": doc.strip(),
                    "polarity": polarity_score,
                })

    return render_template(
        "index.html",
        single_text_results=single_text_results,
        multiple_text_results=multiple_text_results,
        input_type=input_type,
    )

if __name__ == "__main__":
    app.run(debug=True)

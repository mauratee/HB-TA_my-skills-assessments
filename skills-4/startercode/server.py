"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all to finish
the assessment!
"""
# Add "request" import for MCQ 7
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def show_index():
    """Show the assessment page"""

    return render_template("index.html")


# ## MCQ Question 7 ###

# @app.route('/items')
# def get_item_by_index():
#     items = ['apple', 'berry', 'cherry']
#     idx = int(request.args.get('index', 0))

#     return items[idx]


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )

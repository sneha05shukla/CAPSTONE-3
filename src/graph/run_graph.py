import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

from src.graph.workflow import graph

print("Starting Graph Test...")

result = graph.invoke(
    {
        "query": "I am angry because my refund is delayed"
    }
)

print(result)
#Count tokens and the cost of API call
from llm.llm import generate_evaluate_chain
from streamlitapp import RESPONSE_JSON, subject, text, tone


import json


response=generate_evaluate_chain(
        {
        "text": text,
        "number": mcq_count,
        "subject":subject,
        "tone": tone,
        "response_json": json.dumps(RESPONSE_JSON)
            }
    )
#st.write(response)
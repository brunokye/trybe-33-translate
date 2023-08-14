import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    list = HistoryModel.list_as_json()
    data = json.loads(list)

    data[0].pop("_id")
    data[1].pop("_id")

    assert data[0] == {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    }

    assert data[1] == {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    }

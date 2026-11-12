# Final project

An emotion detection web application for the IBM Python and Flask course.
It calls the live Skills Network Watson NLP API and returns anger, disgust,
fear, joy, sadness, and the dominant emotion. The original IBM HTML and
JavaScript interface is retained.

## Run in the Skills Network Cloud IDE

The Watson endpoint is available from the course lab environment.

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection.py
python3 -m pylint server.py
python3 server.py
```

Open port 5000 with the lab's Launch Application tool. The `/emotionDetector`
route reads the `textToAnalyze` query parameter. An HTTP 400 response from
Watson produces None values and the UI displays `Invalid text! Please try again!`.
Service transport failures return HTTP 503 instead of invented emotion scores.

## Verified results, 12 November 2026

- Both integration tests passed: five required emotion examples and empty input.
- Pylint score for `server.py`: **10.00/10**.
- The browser displayed dominant emotion **joy** for `I think I am having fun`.
- Empty input displayed the required error message.
- Actual terminal records are retained in `evidence/`.

This implementation was prepared with AI assistance and verified against the
live Watson service in the course Cloud IDE. Starter interface and license:
IBM Developer Skills Network, original revision
`3e04588b7b73640f1afb806d3e6bf3e2a41e8fd2`.

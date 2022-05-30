# ef23-ai-carrace

This is part of a school project - please ignore.

## Setup

```sh
git clone https://github.com/rafaelurben/ef23-ai-carrace.git
cd ef23-ai-carrace
python -m pip install -r requirements.txt
```

### Folder structure

- (parent)
  - ef23-ai-carrace
    - networks
    - scripts
      - pyworld
  - NeuralRacingV1
    - data (default `TRACES_PATH`)

An alternative traces path can be set via the `TRACES_PATH` environment variable.

## Run

Run the `evaluation.py` script to generate traces in the `TRACES_PATH` folder.

## Source

Python module for the neural network features: (created by me)
https://github.com/rafaelurben/python-neural-network

Source code for the `pyworld` folder: (created by @gymburgdorf-ef23)
https://github.com/gymburgdorf-ef23/NeuralRacingV1/tree/main/pyworld

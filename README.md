# Celestial Client
This is the accompanying Python client to [www.celestial-automl.com](www.celestial-automl.com).

## Installation

```
git clone https://github.com/LarsHH/celestial-client.git
cd celestial-client
pip install -e .
```

## Usage

```
import celestial
# ...

number_of_trials = 100
for _ in range(number_of_trials):
    trial = celestial.Trial(study_id=<your study id>)

    # ...train with trial.parameters...
    # ...assign resulting loss to loss...

    trial.submit_result(loss=<your loss value>)
```

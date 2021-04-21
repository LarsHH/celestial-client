# Celestial Client
This is the accompanying Python client to [www.celestial-automl.com](www.celestial-automl.com), a free hyperparameter optimization service. Read our [Medium article](https://medium.com/@lars.h.hertel/hyperparameter-optimization-as-a-service-with-celestial-automl-b12a1c98638a) on how to get started.

## Installation

```
pip install celestial-client
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

## Examples

A full example can be run as:
```
cd celestial-client
python examples/mlp.py --study-id <your-study-id>
```

Note that this requires scikit-learn, e.g.
```
pip install sklearn
```

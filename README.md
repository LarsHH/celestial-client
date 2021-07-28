# Celestial Client
This is the accompanying Python client to [www.celestial-automl.com](www.celestial-automl.com), a free hyperparameter optimization service. Read our [Medium article](https://medium.com/@lars.h.hertel/hyperparameter-optimization-as-a-service-with-celestial-automl-b12a1c98638a) on how to get started.

Check out the Colab [Keras Example Notebook](https://colab.research.google.com/drive/1FF36LO64x5wDMlvsyF11OfewVEP82Ob0?usp=sharing).

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

#### Keras
Find a Google Colab Notebook tuning a Keras Convnet [here](https://colab.research.google.com/drive/1FF36LO64x5wDMlvsyF11OfewVEP82Ob0?usp=sharing).

#### Scikit Learn

A full example can be run as:
```
cd celestial-client
python examples/mlp.py --study-id <your-study-id>
```

Note that this requires scikit-learn, e.g.
```
pip install sklearn
```

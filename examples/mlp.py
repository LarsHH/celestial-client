
import argparse
import celestial
from sklearn.datasets import load_breast_cancer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
parser = argparse.ArgumentParser()
parser.add_argument('--study-id', type=int,
                    help='The ID of the study in the Celestial web app.')
args = parser.parse_args()

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                     random_state=1)

for i in range(20):
    trial = celestial.Trial(study_id=args.study_id)
    print(trial.parameters)

    clf = MLPClassifier(max_iter=300,
                        solver=trial.parameters['solver'],
                        learning_rate_init=trial.parameters['learning_rate_init'],
                        learning_rate=trial.parameters['learning_rate'],
                        batch_size=trial.parameters['batch_size'])
    clf.fit(X_train, y_train)
    acc = clf.score(X_test, y_test)
    print(f"Accuracy={acc}, loss={1.-acc}")
    trial.submit_result(loss=1.-acc)

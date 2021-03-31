import celestial
import logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s %(levelname)s %(message)s')

for _ in range(10):
    trial = celestial.Trial(study_id=3)
    print(trial.parameters)
    print(trial.submit_result(loss=1-trial.parameters['param1'], accuracy=0.9+trial.parameters['param2']/200).json())
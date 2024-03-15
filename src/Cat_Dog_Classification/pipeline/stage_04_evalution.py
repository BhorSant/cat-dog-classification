from src.Cat_Dog_Classification.config import ConfigurationManager
from src.Cat_Dog_Classification.components import Evaluation
from src.Cat_Dog_Classification import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
            

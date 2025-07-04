from bullprediction.config.configuration import ConfigurationManager
from bullprediction.conponents.model_trainer import ModelTrainer
from bullprediction.conponents.data_transformation import DataTransformation


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation()
        data_transformer = DataTransformation(config=data_transformation_config)
        model_trainer_config = config.get_model_trainer()
        model_trainer = ModelTrainer(config=model_trainer_config, data_transformer=data_transformer)
        model_trainer.train()


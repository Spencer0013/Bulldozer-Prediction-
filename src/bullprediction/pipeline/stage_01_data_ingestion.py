from bullprediction.config.configuration import ConfigurationManager
from bullprediction.conponents.data_ingestion import DataIngestion
from bullprediction.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.read_data()
        data_ingestion.process_and_save()


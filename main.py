from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import STAGE_NAME, DataIngestionTrainingPipeline

try:
    logger.info('{STAGE_NAME}<<<')
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    

except Exception as e:
    logger.exception(e)
    raise e


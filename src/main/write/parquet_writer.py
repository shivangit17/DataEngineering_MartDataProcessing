import traceback
from src.main.utility.logging_config import *
class ParquetWriter:
    def __init__(self,mode,data_format):
        self.mode = mode
        self.data_format = data_format

    def dataframe_writer(self,df, file_path):
        try:
            logger.info("**************** 4444444444444 **************")
            df.write.format(self.data_format) \
                .option("header", "true") \
                .mode(self.mode) \
                .option("path", file_path) \
                .save()
            logger.info("**************** 555555555555555 **************")

        except Exception as e:
            logger.error(f"Error writing the data : {str(e)}")
            traceback_message = traceback.format_exc()
            print(traceback_message)
            raise e
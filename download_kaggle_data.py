import kagglehub
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class DownloadKaggleData:

    def __init__():
        # Download latest version
        logging.info("Download air quality sample data.")
        kagglehub.dataset_download("razanihababdellatif/smart-city-digital-twin-ecosystem-dataset", path="air_quality.csv", output_dir="./data")
        logging.info("Download traffic sample data.")
        kagglehub.dataset_download("razanihababdellatif/smart-city-digital-twin-ecosystem-dataset", path="traffic.csv",output_dir="./data")
        logging.info("Download weather sample data.")
        kagglehub.dataset_download("razanihababdellatif/smart-city-digital-twin-ecosystem-dataset", path="weather.csv", output_dir="./data")

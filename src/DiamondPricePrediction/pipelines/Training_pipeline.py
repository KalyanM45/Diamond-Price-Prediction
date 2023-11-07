from src.DiamondPricePrediction.components.Data_ingestion import DataIngestion
import os
import sys
import pandas as pd
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception

obj = DataIngestion()
obj.initiate_data_ingestion()
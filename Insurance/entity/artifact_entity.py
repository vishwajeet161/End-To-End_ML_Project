# artifact_entity file generates outputs and save it here

from dataclasses import dataclass


class DataIngestionArtifact:
    feature_store_file_path:str 
    train_file_path:str
    test_file_path:str
    
"""
To be written
"""

from pathlib import Path

import pandas as pd


class LoadTrain:
    def __init__(self):
        self.data = None
        self.filePath = None
        self.mode = None

    def load_data(self, path, mode="embd"):
        """
        Modes: embeddings, text
        """
        self.filePath = Path(path)
        self.mode = mode

        if not self.filePath.exists():
            raise FileNotFoundError(f"Dataset not found: {self.filePath}")

        # check for file extention
        extension = self.filePath.name.split(".")[1]

        # read text descriptors
        if self.mode == "text":
            if extension == "csv":
                self.data = pd.read_csv(self.filePath)
                print("Dataset loaded")

            elif extension in ["xls", "xlsx"]:
                self.data = pd.read_excel(self.filePath)
                print("Dataset loaded")
            else:
                raise ValueError(
                    f"Invalid file type: {self.filePath.suffix}. "
                    "Expected an Excel file (csv or xlsx or xls)."
                )
        elif self.mode == "embd":
            pass

        else:
            raise ValueError(f"Invalid read mode: {self.mode}.")

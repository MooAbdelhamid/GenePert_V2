"""
TBD
"""


class BuildTrain:
    def __init_(self, mode):
        if mode not in ["load", "generate"]:
            raise ValueError("Mode must be 'load' or 'generate'")

        self.mode = mode
        self.embeddings = None
        self.gene_descriptions = None
        self.model = None

    def load_precomputed    (self):
        pass

    def load_gene_descriptions(self):
        pass

    def load_model(self):
        pass

    def generate_embeddings(self):
        pass

    def validate_embeddings(self):
        pass

    def build(self):
        pass

from classes.data_processor import DataProcessor


class MockProcessor(DataProcessor):
    def _process_list(self, data: list):
        return ["processed_list"]

    def _process_dict(self, data: dict):
        return {"processed_dict": "processed"}

    def _process_default(self, data):
        return "default_processed"

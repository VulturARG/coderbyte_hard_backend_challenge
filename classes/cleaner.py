from classes.data_processor import DataProcessor


class Cleaner(DataProcessor):
    def _process_list(self, data):
        cleaned_list = [self.process(item) for item in data if item not in ([], {}, '', None)]
        cleaned_list = [item for item in cleaned_list if item not in ([], {})]
        return cleaned_list if cleaned_list else []

    def _process_dict(self, data):
        cleaned_dict = {}
        for k, v in data.items():
            cleaned_value = self.process(v)
            if cleaned_value not in ([], '', None):
                cleaned_dict[k] = cleaned_value
        return cleaned_dict if cleaned_dict else {}


from classes.data_processor import DataProcessor


class KeySorter(DataProcessor):
    def _process_list(self, data):
        return [self.process(item) for item in data]

    def _process_dict(self, data):
        return {
            k: self.process(v)
            for k, v in sorted(data.items(), key=lambda item: item[0].lower())
        }

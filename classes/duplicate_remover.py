from classes.data_processor import DataProcessor


class DuplicateRemover(DataProcessor):
    def _process_list(self, data):
        seen = []
        for item in data:
            if not isinstance(item, dict):
                seen.append(item)
                continue
            if item in seen:
                continue
            seen.append(self.process(item))
        return seen

    def _process_dict(self, data):
        return {k: self.process(v) for k, v in data.items()}

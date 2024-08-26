# solution_with_patterns/classes/key_sorter.py

class KeySorter:
    def sort_keys(self, data):
        if isinstance(data, dict):
            return {k: self.sort_keys(v) for k, v in sorted(data.items(), key=lambda item: item[0].lower())}
        elif isinstance(data, list):
            return [self.sort_keys(item) for item in data]
        else:
            return data

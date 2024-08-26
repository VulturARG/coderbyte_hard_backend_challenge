class DuplicateRemover:
    def remove_duplicates(self, data):
        if isinstance(data, list):
            seen = []
            for item in data:
                if isinstance(item, dict):
                    if item not in seen:
                        seen.append(self.remove_duplicates(item))
                else:
                    seen.append(item)
            return seen
        elif isinstance(data, dict):
            return {k: self.remove_duplicates(v) for k, v in data.items()}
        else:
            return data

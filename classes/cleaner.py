class Cleaner:
    def clean(self, data):
        if isinstance(data, list):
            cleaned_list = [
                self.clean(item) for item in data if item not in ([], {}, "", None)
            ]
            cleaned_list = [item for item in cleaned_list if item not in ([], {})]
            return cleaned_list if cleaned_list else []
        elif isinstance(data, dict):
            cleaned_dict = {}
            for k, v in data.items():
                cleaned_value = self.clean(v)
                if cleaned_value not in ([], "", None):
                    cleaned_dict[k] = cleaned_value
            return cleaned_dict if cleaned_dict else {}
        else:
            return data

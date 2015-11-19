class SearchValidation:

    @staticmethod
    def is_zero_results(json):
        return json["status"] == "ZERO_RESULTS"


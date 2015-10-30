from simpatize.models import Place


class QueryHelper:

    @staticmethod
    def identify_query(query):
        query = dict(query)
        print(query)
        if "place_name" in query:
            print(QueryHelper.select_place_by_name(query["place_name"]))

    @staticmethod
    def select_place_by_name(place_name):
        return Place.objects.get(name=place_name)


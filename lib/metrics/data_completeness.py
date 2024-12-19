import json
import os
import unittest

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)

data_path = os.path.join(script_path, "..", "..", "data")


class DistrictsTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(DistrictsTestCase, self).__init__(*args, **kwargs)

        # Load geojson file
        with open(
            file=os.path.join(
                data_path, "berlin-lor-districts", "bezirksgrenzen.geojson"
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson = json.load(geojson_file, strict=False)

    def test_feature_count(self):
        self.assertEqual(12, len(self.geojson["features"]))


class ForecastAreasTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ForecastAreasTestCase, self).__init__(*args, **kwargs)

        # Load geojson file
        with open(
            file=os.path.join(
                data_path,
                "berlin-lor-forecast-areas-until-2020",
                "lor_prognoseraeume.geojson",
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson_until_2020 = json.load(geojson_file, strict=False)
        with open(
            file=os.path.join(
                data_path,
                "berlin-lor-forecast-areas-from-2021",
                "lor_prognoseraeume_2021.geojson",
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson_from_2021 = json.load(geojson_file, strict=False)

    def test_feature_count_until_2020(self):
        self.assertEqual(60, len(self.geojson_until_2020["features"]))

    def test_feature_count_from_2021(self):
        self.assertEqual(58, len(self.geojson_from_2021["features"]))


class DistrictRegionsTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(DistrictRegionsTestCase, self).__init__(*args, **kwargs)

        # Load geojson file
        with open(
            file=os.path.join(
                data_path,
                "berlin-lor-district-regions-until-2020",
                "lor_bezirksregionen.geojson",
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson_until_2020 = json.load(geojson_file, strict=False)
        with open(
            file=os.path.join(
                data_path,
                "berlin-lor-district-regions-from-2021",
                "lor_bezirksregionen_2021.geojson",
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson_from_2021 = json.load(geojson_file, strict=False)

    def test_feature_count_until_2020(self):
        self.assertEqual(138, len(self.geojson_until_2020["features"]))

    def test_feature_count_from_2021(self):
        self.assertEqual(143, len(self.geojson_from_2021["features"]))


class PlanningAreasTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PlanningAreasTestCase, self).__init__(*args, **kwargs)

        # Load geojson file
        with open(
            file=os.path.join(
                data_path,
                "berlin-lor-planning-areas-until-2020",
                "lor_planungsraeume.geojson",
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson_until_2020 = json.load(geojson_file, strict=False)
        with open(
            file=os.path.join(
                data_path,
                "berlin-lor-planning-areas-from-2021",
                "lor_planungsraeume_2021.geojson",
            ),
            mode="r",
            encoding="utf-8",
        ) as geojson_file:
            self.geojson_from_2021 = json.load(geojson_file, strict=False)

    def test_feature_count_until_2020(self):
        self.assertEqual(448, len(self.geojson_until_2020["features"]))

    def test_feature_count_from_2021(self):
        self.assertEqual(542, len(self.geojson_from_2021["features"]))


if __name__ == "__main__":
    unittest.main()

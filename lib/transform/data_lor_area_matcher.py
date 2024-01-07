import json
import os

import geopandas as gpd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def identify_lor_area_matches(source_path, results_path, intersection_ratio_threshold=0.9, area_tolerance=0.01, clean=False,
                              quiet=False):
    matches = []

    for lor_area_type in ["forecast-areas", "district-regions", "planning-areas"]:
        lor_area_type_matches = []

        # Read geojson files
        gdf_until_2020 = gpd.read_file(os.path.join(source_path, f"berlin-lor-{lor_area_type}-until-2020",
                                                    f"berlin-lor-{lor_area_type}-until-2020.geojson"))
        gdf_from_2021 = gpd.read_file(os.path.join(source_path, f"berlin-lor-{lor_area_type}-from-2021",
                                                   f"berlin-lor-{lor_area_type}-from-2021.geojson"))

        gdf_until_2020_feature_count = gdf_until_2020.index.size
        gdf_from_2021_feature_count = gdf_from_2021.index.size

        # Set coordinate reference system
        gdf_until_2020.set_crs("EPSG:4326", inplace=True)
        gdf_from_2021.set_crs("EPSG:4326", inplace=True)

        # Iterate over both geojson files
        for _, feature_until_2020 in gdf_until_2020.iterrows():
            for _, feature_from_2021 in gdf_from_2021.iterrows():
                # Calculate intersection area
                intersection_area = feature_until_2020.geometry.intersection(feature_from_2021.geometry).area
                intersection_ratio_until_2020 = intersection_area / feature_until_2020.geometry.area
                intersection_ratio_from_2021 = intersection_area / feature_from_2021.geometry.area

                # Calculate the area of each polygon
                area_a = feature_until_2020.geometry.area
                area_b = feature_from_2021.geometry.area

                # Calculate the relative difference in areas
                area_difference = abs(area_a - area_b) / max(area_a, area_b)

                if intersection_ratio_until_2020 > intersection_ratio_threshold and intersection_ratio_from_2021 > intersection_ratio_threshold and area_difference < area_tolerance:
                    lor_area_type_matches.append(
                        {"until-2020": feature_until_2020['id'], 'from-2021': feature_from_2021['id']})

        print(
            f"✓ Found {len(lor_area_type_matches)} matches in {lor_area_type} (until 2020: {gdf_until_2020_feature_count}, from 2021: {gdf_from_2021_feature_count})")
        matches += lor_area_type_matches

    write_json_file(os.path.join(results_path, "berlin-lor-matches", "berlin-lor-matches.json"), matches, clean, quiet)


def write_json_file(file_path, json_content, clean, quiet):
    if not os.path.exists(file_path) or clean:

        # Make results path
        path_name = os.path.dirname(file_path)
        os.makedirs(os.path.join(path_name), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(json_content, json_file, ensure_ascii=False)

            if not quiet:
                print(f"✓ Writes LOR area matches into {os.path.basename(file_path)}")
    else:
        print(f"✓ Already exists {os.path.basename(file_path)}")

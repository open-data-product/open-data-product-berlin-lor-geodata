import json
import os

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def extend_data_properties(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in os.walk(source_path):
        for file_name in [file_name for file_name in sorted(files) if file_name.endswith(".geojson")]:
            subdir = subdir.replace(f"{source_path}/", "")

            # Make results path
            os.makedirs(os.path.join(results_path), exist_ok=True)

            source_file_path = os.path.join(source_path, subdir, file_name)
            results_file_path = os.path.join(results_path, subdir, file_name)

            with open(source_file_path, "r", encoding="utf-8") as geojson_file:
                geojson = json.load(geojson_file, strict=False)

            geojson, changed = extend_properties(geojson)

            if changed:
                with open(results_file_path, "w", encoding="utf-8") as geojson_file:
                    json.dump(geojson, geojson_file, ensure_ascii=False)

                    if not quiet:
                        print(f"✓ Extend {file_name}")
            else:
                if not quiet:
                    print(f"✓ Already extended {file_name}")


def extend_properties(geojson):
    changed = False

    for feature in geojson["features"]:
        properties = feature["properties"]

        id = properties["id"]

        if id == "01":
            properties["area"] = 39_340_000
            changed = True
        elif id == "02":
            properties["area"] = 20_360_000
            changed = True
        elif id == "03":
            properties["area"] = 103_100_000
            changed = True
        elif id == "04":
            properties["area"] = 59_760_000
            changed = True
        elif id == "05":
            properties["area"] = 91_740_000
            changed = True
        elif id == "06":
            properties["area"] = 102_400_000
            changed = True
        elif id == "07":
            properties["area"] = 52_930_000
            changed = True
        elif id == "08":
            properties["area"] = 44_890_000
            changed = True
        elif id == "09":
            properties["area"] = 167_410_000
            changed = True
        elif id == "10":
            properties["area"] = 61_770_000
            changed = True
        elif id == "11":
            properties["area"] = 52_020_000
            changed = True
        elif id == "12":
            properties["area"] = 89_190_000
            changed = True

    return geojson, changed

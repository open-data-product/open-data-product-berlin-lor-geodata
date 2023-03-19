import os
import shutil

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def copy_data(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in os.walk(source_path):
        for source_file_name in files:
            subdir = subdir.replace(f"{source_path}/", "")
            results_file_name = get_results_file_name(source_file_name)

            # Make results path
            os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

            source_file_path = os.path.join(source_path, subdir, source_file_name)
            results_file_path = os.path.join(results_path, subdir, results_file_name)

            # Check if file needs to be copied
            if clean or not os.path.exists(results_file_path):
                shutil.copyfile(source_file_path, results_file_path)

                if not quiet:
                    print(f"✓ Copy {results_file_name}")
            else:
                print(f"✓ Already exists {results_file_name}")


def get_results_file_name(source_file_name):
    if source_file_name == "bezirksgrenzen.geojson":
        return "berlin-lor-districts.geojson"
    elif source_file_name == "lor_prognoseraeume.geojson":
        return "berlin-lor-forecast-areas-until-2020.geojson"
    elif source_file_name == "lor_prognoseraeume_2021.geojson":
        return "berlin-lor-forecast-areas-from-2021.geojson"
    elif source_file_name == "lor_bezirksregionen.geojson":
        return "berlin-lor-district-regions-until-2020.geojson"
    elif source_file_name == "lor_bezirksregionen_2021.geojson":
        return "berlin-lor-district-regions-from-2021.geojson"
    elif source_file_name == "lor_planungsraeume.geojson":
        return "berlin-lor-planning-areas-until-2020.geojson"
    elif source_file_name == "lor_planungsraeume_2021.geojson":
        return "berlin-lor-planning-areas-from-2021.geojson"
    else:
        return source_file_name

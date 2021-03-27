"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(list(fieldnames))
        for approach in results:
            datetime_utc = datetime_to_str(approach.time)
            distance_au = approach.distance
            velocity_km_s = approach.velocity 
            designation = approach.neo.designation
            name = approach.neo.name if approach.neo.name else "" 
            diameter = approach.neo.diameter
            potentially_hazardous = approach.neo.hazardous 
            writer.writerow([datetime_utc, distance_au, velocity_km_s, designation, name, diameter, potentially_hazardous])

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    '''
    {
    "datetime_utc": "2025-11-30 02:18",
    "distance_au": 0.397647483265833,
    "velocity_km_s": 3.72885069167641,
    "neo": {
      "designation": "433",
      "name": "Eros",
      "diameter_km": 16.84,
      "potentially_hazardous": false
    }
    '''
    data = []
    for approach in results:
        datetime_utc = datetime_to_str(approach.time)
        distance_au = approach.distance
        velocity_km_s = approach.velocity 
        designation = approach.neo.designation
        name = approach.neo.name if approach.neo.name else "" 
        diameter = approach.neo.diameter
        potentially_hazardous = approach.neo.hazardous 
        obj = {
            'datetime_utc': datetime_utc,
            'distance_au': distance_au,
            'velocity_km_s': velocity_km_s,
            'neo': {
                'designation': designation,
                'name': name,
                'diameter_km': diameter,
                'potentially_hazardous': potentially_hazardous
            }
        }
        data.append(obj)
        

    with open(filename, 'w') as f:
        json.dump(data, f)

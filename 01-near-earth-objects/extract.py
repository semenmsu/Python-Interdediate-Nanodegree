"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import pandas as pd

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    df = pd.read_csv(neo_csv_path, low_memory=False)
    df = df[['pdes', 'name','pha', 'diameter']]
    df.pdes = df.pdes.astype('str')
    neos = [NearEarthObject(**value) for  value in df.T.to_dict().values()]
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    
    json_data = None
    with open(cad_json_path, "r") as f:
        json_data = json.load(f)
    if json_data:
        df = pd.DataFrame.from_records(json_data['data'])
        df.columns = json_data['fields']
        df = df[['des', 'cd','dist', 'v_rel']]
        df.des = df.des.astype('str')
        approaches = [CloseApproach(**value) for  value in df.T.to_dict().values()]
        return approaches
    return []

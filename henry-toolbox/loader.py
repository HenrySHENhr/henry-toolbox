import csv
import io
import json
import os
import yaml


def load_yaml_file(yaml_file):
    """
    Load yaml file
    :param yaml_file: yaml file path
    :return: file content
    """
    with io.open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_content = yaml.load(f)
        return yaml_content


def load_json_file(json_file):
    """
    Load json file
    :param json_file: json file path
    :return: file content
    """
    with io.open(json_file, encoding='utf-8') as f:
        json_content = json.load(f)
        return json_content


def load_csv_file(csv_file):
    """
    Load csv file
    :param csv_file: csv file path
    :return: list of parameters, each parameter is in dict format
    """
    if not os.path.isabs(csv_file):
        project_working_directory = os.getcwd()
        csv_file = os.path.join(project_working_directory, *csv_file.split("/"))

    csv_content_list = []
    with io.open(csv_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_content_list.append(row)
    return csv_content_list

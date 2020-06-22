import sys

from .loader import load_csv_file


def match_sub(source, sub):
    index_list = []
    source_data = [item['url'] for item in load_csv_file(source)]
    sub_data = [item['url'] for item in load_csv_file(sub)]
    for source_item in source_data:
        for sub_item in sub_data:
            if sub_item in source_item:
                index_list.append([source_data.index(source_item), sub_data.index(sub_item)])
    return index_list


def run_cli(arguments=None):
    """
    Run client
    :param arguments: input arguments
    :return:
    """
    if arguments is None:
        arguments = sys.argv[1:]
    print('main', arguments)

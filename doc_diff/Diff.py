import csv
import os.path as path
import datetime


def gen_comp_report(diff1, diff2):
    evaluation_results = _compare_two_files(diff1.data_dict, diff2.data_dict)

    now = datetime.datetime.now()

    # write the results for corresponding files
    _write_out_results(evaluation_results[0], '../results/matching_list_' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[1], '../results/un_matching_list_' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[2], '../results/unknown_list_' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[3], '../results/additional_list_' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[0], '../results/common_in_doc1-and-doc2' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[1], '../results/common_key_with_diff_values' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[2], '../results/exclusive_in_doc1' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results[3], '../results/exclusive_in_doc2' + now.strftime("%Y-%m-%d") + '.csv')


def _write_out_results(data, filename):
    """
    Allow to write the dict data to CSV format
    :param data: dictionary list
    :param filename: filename including the path
    """
    writer = csv.writer(open(filename, 'wb'))
    for key, value in data.items():
        writer.writerow([key + '\t' + value])


def _compare_two_files(dict1, dict2):
    """
    This will compare to dictionary values and generate
    matching, un-matching, unknown (dict1) and additional
    lists.
    :param dict1: list of key and values
    :param dict2: list of key and values
    :return: matching, un-matching, unknown (dict1) and additional (dict2) items
    """
    matching_list = dict()
    un_matching_list = dict()
    unknown_list = dict()
    temp_known_keys = []

    for key, value in dict1.iteritems():
        if key in dict2:
            # do a string comparison
            if value != dict2[key]:
                un_matching_list[key] = value + "||" + dict2[key]
            else:
                matching_list[key] = value
            # store the key and filter at last
            temp_known_keys.append(key)
        else:
            unknown_list[key] = value

    additional_list = {k: v for k, v in dict2.iteritems() if k not in temp_known_keys}
    return matching_list, un_matching_list, unknown_list, additional_list


class Diff:
    def __init__(self, file):
        self.fileT_type = 'csv'
        self.data = None
        self._file_name = file
        self._res = path.join(path.dirname(__file__), 'res')
        self._no_of_records = 0
        self._delimiter = '\t'
        self.data_dict = dict()

    def read_file(self):
        with open(self._file_name, 'r') as ins:
            for line in ins:
                self.increment_recommendation_count()
                self.construct_key_value(line, self._delimiter)

    def increment_recommendation_count(self):
        self._no_of_records += 1

    @staticmethod
    def format_order_recommendations(data):
        tem_list = data.replace('\n', '').replace('\"\"', '').split(',')
        tem_list.sort()
        return tem_list

    def construct_key_value(self, line, delimiter):
        (key, value) = line.split(delimiter)
        if key not in self.data_dict:
            self.data_dict[key] = ','.join(self.format_order_recommendations(value))
        else:
            print "The key already exist : %s" % key

    def process_file(self):
        self.read_file()

import csv
import os.path as path


def gen_comp_report(diff1, diff2):
    _compare_two_files(diff1.data_dict, diff2.data_dict)


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
    return additional_list


class Diff:
    def __init__(self):
        self.fileT_type = 'csv'
        self.data = None
        self._file_name = None
        self._res = path.join(path.dirname(__file__), 'res')
        self._no_of_records = 0
        self._delimiter = '\t'
        self.data_dict = dict()

    def read_file(self):
        with open(self.file_name, 'r') as ins:
            for line in ins:
                print line

    def increment_recommendation_count(self):
        self._no_of_records += 1

    def format_order_recommendations(self, data):
        tem_list = data.replace('\n', '').replace('\"\"', '').split(',')
        tem_list.sort()
        return tem_list

    def construct_key_value(self, line, delimiter):
        (key, value) = line.split(delimiter)
        if key not in self.data_dict:
            self.data_dict[key] = ','.join(self.format_order_recommendations(value))
        else:
            print "The key already exist : %s" % key

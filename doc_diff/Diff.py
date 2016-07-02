import csv
import os.path as path
import datetime


def gen_comp_report(diff1, diff2):
    """
    It will allow to create the comparison
    results in CSV file format
    :param diff1: doc1's diff object
    :param diff2: doc2's diff object
    """
    # compute the diff of doc1 & doc2
    evaluation_results = _compare_two_files(diff1.data_dict, diff2.data_dict)
    now = datetime.datetime.now()
    _create_result_folder()

    # write the results for corresponding files
    _write_out_results(evaluation_results['common_in_doc1_and_doc2_list'],
                       './doc-diff-results/common_in_doc1-and-doc2-' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results['common_key_with_diff_values_list'],
                       './doc-diff-results/common_key_with_diff_values-' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results['exclusive_in_doc1_list'],
                       './doc-diff-results/exclusive_in_doc1-' + now.strftime("%Y-%m-%d") + '.csv')
    _write_out_results(evaluation_results['exclusive_in_doc2_list'],
                       './doc-diff-results/exclusive_in_doc2-' + now.strftime("%Y-%m-%d") + '.csv')


def _create_result_folder():
    """
    Check the result folder exists
    if not create the folder
    """
    import os
    if not path.exists('./doc-diff-results'):
        os.makedirs('./doc-diff-results')


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
    common_in_doc1_and_doc2_list = dict()
    common_key_with_diff_values_list = dict()
    exclusive_in_doc1_list = dict()
    temp_known_keys = []

    for key, value in dict1.iteritems():
        if key in dict2:
            # do a string comparison
            if value != dict2[key]:
                common_key_with_diff_values_list[key] = value + "||" + dict2[key]
            else:
                common_in_doc1_and_doc2_list[key] = value
            # store the key and filter at last
            temp_known_keys.append(key)
        else:
            exclusive_in_doc1_list[key] = value

    exclusive_in_doc2_list = {k: v for k, v in dict2.iteritems() if k not in temp_known_keys}
    return { 'common_in_doc1_and_doc2_list': common_in_doc1_and_doc2_list,
             'common_key_with_diff_values_list': common_key_with_diff_values_list,
             'exclusive_in_doc1_list': exclusive_in_doc1_list,
             'exclusive_in_doc2_list': exclusive_in_doc2_list }


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
        """
        Read the file from the location
        and iterate the list of lines
        """
        with open(self._file_name, 'r') as ins:
            for line in ins:
                self._no_of_records += 1  # calculate the row count
                self.construct_key_value(line, self._delimiter)

    @staticmethod
    def format_order_recommendations(data):
        """
        Format the key-value pairs
        :param data: values/recommendation
        :return: cleaned and sorted list
        """
        tem_list = data.replace('\n', '').replace('\"\"', '').split(',')
        tem_list.sort()
        return tem_list

    def construct_key_value(self, line, delimiter):
        """
        Convert each line as key-value sets
        :param line: a row from the document
        :param delimiter: separate the key and value
        """
        (key, value) = line.split(delimiter)
        if key not in self.data_dict:
            self.data_dict[key] = ','.join(self.format_order_recommendations(value))
        else:
            print "The key already exist : %s" % key

    def process_file(self):
        self.read_file()

import csv
import datetime


def write_out_results(data, filename):
    """
    Allow to write the dict data to CSV format
    :param data: dictionary list
    :param filename: filename including the path
    """
    writer = csv.writer(open(filename, 'wb'))
    for key, value in data.items():
        writer.writerow([key + '\t' + value])


def compare_two_files(dict1, dict2):
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


def format_order_recommendations(data):
    recommendation_list = data.replace('\n', '').replace('\"\"', '').split(',')
    recommendation_list.sort()
    return recommendation_list


def construct_key_value(variable, data, delimiter):
    """
    This method will update the dic with
    corresponding key : values
    :param variable: Dictionary
    :param data: each line from the file
    :return: return the updated dic
    """
    (key, value) = data.split(delimiter)
    if key not in variable:
        variable[key] = ','.join(format_order_recommendations(value))
    else:
        print "The key already exist : %s" % key
    return variable


def increment_recommendation_count(total_recommendation):
    """
    This will help to increment the recommendation count
    for each iteration
    :param total_recommendation:
    :return: Incremented value
    """
    total_recommendation += 1
    return total_recommendation


if __name__ == "__main__":

    a_priori_csv_location = "./data/pfp.csv"
    a_priori_recommendation = 0
    a_priori_list = dict()

    with open(a_priori_csv_location, "r") as ins:
        for line in ins:
            a_priori_recommendation = increment_recommendation_count(a_priori_recommendation)
            a_priori_list = construct_key_value(a_priori_list, line, '\t')

    pfp_csv_location = "./data/pfp-new.csv"
    pfp_recommendation = 0
    pfp_list = dict()

    with open(pfp_csv_location, "r") as ins:
        for line in ins:
            pfp_recommendation = increment_recommendation_count(pfp_recommendation)
            pfp_list = construct_key_value(pfp_list, line, '\t')

    evaluation_results = compare_two_files(a_priori_list, pfp_list)

    now = datetime.datetime.now()

    # write the results for corresponding files
    write_out_results(evaluation_results[0], './results/matching_list_' + now.strftime("%Y-%m-%d") + '.csv')
    write_out_results(evaluation_results[1], './results/un_matching_list_' + now.strftime("%Y-%m-%d") + '.csv')
    write_out_results(evaluation_results[2], './results/unknown_list_' + now.strftime("%Y-%m-%d") + '.csv')
    write_out_results(evaluation_results[3], './results/additional_list_' + now.strftime("%Y-%m-%d") + '.csv')

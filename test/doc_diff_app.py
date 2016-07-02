from doc_diff import Diff
from doc_diff import gen_comp_report

if __name__ == '__main__':
    # Data file location
    a_priori_csv_location = "./data/a-priori.csv"
    pfp_csv_location = "./data/pfp.csv"

    # Process a-priori.csv data file
    a_priori_diff = Diff(a_priori_csv_location)
    a_priori_diff.process_file()

    # Process pfp.csv data file
    pfp_diff = Diff(pfp_csv_location)
    pfp_diff.process_file()

    gen_comp_report(a_priori_diff, pfp_diff)
##Input: Usage: typosquatting.py -d domain -e 1-20
##Output: Matching domains

import argparse
import Levenshtein
import logging 

argument_parser = argparse.ArgumentParser(
    prog='Typosquatting.py',
    description=('Print candidate domains for typosquatting based on edit' 
                 ' distance calculation. Reads from a csv whois database file'
                 ' with newly registered domain names')
)
argument_parser.add_argument("-d", "--domain")
argument_parser.add_argument("-e", "--edit_distance")
argument_parser.add_argument("-w", "--whois_file", required=False)

arguments = argument_parser.parse_args() 

class TypoSquatting:
    def __init__(self, original_domain, edit_distance=1, 
        whois_csv_file = 'whois_csv_files/full-database.csv'):

        self.original_domain = original_domain
        self.edit_distance = edit_distance 
        self.whois_csv_file = whois_csv_file

    @staticmethod
    def get_domain_name_from_file(whois_csv_line):
        _, domain_name, *_ = str(whois_csv_line).split(',')
        yield domain_name

    def read_whois_csv_file_by_line(self):
        for line_in_whois_file in open(self.whois_csv_file, 'rb'):
            yield line_in_whois_file 

    def is_similar(self, original_domain, domain_from_whois):
        return (Levenshtein.distance(original_domain, domain_from_whois) 
        <= int(self.edit_distance))

    def get_similar_domain_names_from_whois_databasefile(self):
        for line in self.read_whois_csv_file_by_line():
            for domain_name in self.get_domain_name_from_file(line):
                if self.is_similar(self.original_domain, domain_name):
                    yield domain_name

typosquatting = TypoSquatting(original_domain = arguments.domain, 
    edit_distance=arguments.edit_distance,
)

for domain in typosquatting.get_similar_domain_names_from_whois_databasefile():
    print(domain)
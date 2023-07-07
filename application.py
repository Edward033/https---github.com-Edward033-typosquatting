from typosquatting import TypoSquatting
import argparse

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

typosquatting = TypoSquatting(original_domain = arguments.domain, 
    edit_distance=arguments.edit_distance,
)

for domain in typosquatting.get_similar_domain_names_from_whois_databasefile():
    print(domain)
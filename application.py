from typosquatting import TypoSquatting

typosquatting = TypoSquatting(original_domain = arguments.domain, 
    edit_distance=arguments.edit_distance,
)

for domain in typosquatting.get_similar_domain_names_from_whois_databasefile():
    print(domain)
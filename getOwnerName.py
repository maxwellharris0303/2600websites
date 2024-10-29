import whois

def get_owner_name(url):
    domain = whois.whois(url)
    # print(domain.registrar)
    return domain.registrar

# get_owner_name("http://currentwellnessraleigh.com/")
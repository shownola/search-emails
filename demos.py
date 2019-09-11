from random import choice
from string import ascii_lowercase as letters

######### Functions to generate a list of emails #################

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def generate_emails(length_of_name, list_of_domains, total_emails):
    emails = []
    for num in range(total_emails):
        emails.append(generate_name(length_of_name)+"@"+get_domain(list_of_domains))
    return emails

print(generate_name(10))
print(get_domain(), [...])

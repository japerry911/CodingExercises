"""
---Subdomains---
A website domain like "discuss.leetcode.com" consists of various subdomains. At 
the top level, we have "com", at the next level, we have "leetcode.com", and at 
the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", 
we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this 
domain received), followed by a space, followed by the address. An example of a count-paired 
domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired 
domains, (in the same format as the input, and in any order), that explicitly counts the number 
of visits to each subdomain.
"""

from typing import List


def subdomains(cpdomains: List[str]) -> List[str]:
    return_list = list()
    domain_visits_dict = dict()

    # loop through each cpdomain entry
    for cpdomain_object in cpdomains:
        cpdomain_object_split = cpdomain_object.split(" ")

        # pull visits number from the split list
        visits = cpdomain_object_split[0]
        # split the domains by period and place into variable
        split_domain = cpdomain_object_split[1].split(".")
        split_domain_len = len(split_domain)

        for i in range(0, split_domain_len):
            domain = ".".join(split_domain)

            # checks if the domain is currently in dictionary, and adds if not existing
            if domain not in domain_visits_dict.keys():
                domain_visits_dict[domain] = 0

            # adds the visits to corresponding dictionary domain key
            domain_visits_dict[domain] += int(visits)

            # deletes the front of split_domain list
            split_domain.pop(0)

    # converts dictionary into list with the following format: [visits domain]
    for domain, visits in domain_visits_dict.items():
        return_list.append("{} {}".format(visits, domain))

    print(return_list)

    return return_list

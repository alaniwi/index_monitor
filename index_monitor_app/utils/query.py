import requests

def do_query(index_node,
             filter_strings=[],
             facet_names=[]):

    url = f'https://{index_node}/esg-search/search'

    params = {'limit': '0',
              'type': 'Dataset',
              'format': 'application/solr+json'}

    if facet_names:
        params['facets'] = ','.join(facet_names)
        
    for filter_string in filter_strings:
        k, v = filter_string.split("=", 1)
        params[k] = v

    response = requests.get(url, params)

    resp = {
        'status_code': response.status_code
    }

    if response.status_code == 200:
        
        j = response.json()
        resp['num_found'] = j["response"]["numFound"]

        facet_counts = {}
        for facet_name in facet_names:
            lst = j["facet_counts"]["facet_fields"][facet_name]
            counts = dict(zip(lst[::2], lst[1::2]))
            facet_counts[facet_name] = counts

        resp['facet_counts'] = facet_counts

    return resp
    


if __name__ == '__main__':
    from pprint import pprint

    index_node = 'esgf-index1.ceda.ac.uk'
    filter_strings = ['project!=input4mips', 'mip_era=CMIP6']
    facet_names = ['index_node', 'data_node']
               
    pprint(do_query(index_node, filter_strings, facet_names))

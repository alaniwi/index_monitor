#!/usr/bin/env python3

import django
django.setup()

from index_monitor_app.models import QueryType, Filter, Facet

q_types = {'CMIP6-basic':
               {'filter_strings': ['project!=input4mips', 'mip_era=CMIP6'],
                'facet_names': ['index_node', 'data_node']},
           
           'general-index':
               {'filter_strings': [],
                'facet_names': ['index_node']},
           }



def create_query_types():
    
    for name, d in q_types.items():

        filters = [Filter.objects.get_or_create(value=filter_string)[0]
                   for filter_string in d["filter_strings"]]
        
        facets =  [Facet.objects.get_or_create(name=facet_name)[0]
                   for facet_name in d["facet_names"]]

        query_type, created = QueryType.objects.get_or_create(name=name)

        if created:
            for filter in filters:
                query_type.filters.add(filter)
            for facet in facets:
                query_type.facets.add(facet)
            print("created {}".format(name))

if __name__ == '__main__':
    create_query_types()

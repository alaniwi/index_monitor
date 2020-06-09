#!/usr/bin/env python3

import django
django.setup()

from index_monitor_app.models import QueryType, Filter, Facet


def create_cmip6_basic_query_type():
    
    filters = [Filter.objects.get_or_create(value=filter_string)[0]
               for filter_string in ['project!=input4mips', 'mip_era=CMIP6']]

    facets =  [Facet.objects.get_or_create(name=facet_name)[0]
               for facet_name in ['index_node', 'data_node']]

    query_type = QueryType.objects.create(name='CMIP6-basic')

    for filter in filters:
        query_type.filters.add(filter)

    for facet in facets:
        query_type.facets.add(facet)

    return query_type


if __name__ == '__main__':
    create_cmip6_basic_query_type()

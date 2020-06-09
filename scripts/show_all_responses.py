#!/usr/bin/env python3

import django
django.setup()

from index_monitor_app.models import Response


responses = Response.objects.all().order_by("datetime")

for response in responses:

    print("Date: ", response.datetime)
    print("Index node: ", response.index_node.name)
    #print("Client: ", response.client.name)

    query_type = response.query_type
    facets = query_type.facets.all()
    filters = query_type.filters.all()
    print("Query type:")
    print("    name:", query_type.name)
    print("    facets:", [facet.name for facet in facets])
    print("    filters:", [filter.value for filter in filters])

    print("http status code: ", response.status_code)
    if response.status_code == 200:
    
        print("Num found:", response.data.num_found)
        for facet in facets.order_by('name'):
            counts = response.data.facet_value_counts.filter(
                facet_value__facet=facet)
                
            print("Counts for facet '{}':".format(facet.name))
            for fvc in counts.order_by('facet_value__value'):
                print("    {}: {}".format(fvc.facet_value.value, fvc.count))
    print()
    

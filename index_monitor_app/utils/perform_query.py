from django.utils.timezone import now
from socket import gethostname

from index_monitor_app.models import \
    Host, Response, ResponseData, Facet, FacetValue, FacetValueCount, \
    QueryType

from index_monitor_app.utils.query import do_query


def perform_query_by_name(index_node_name, query_type_name):

    index_node, _ = Host.objects.get_or_create(name=index_node_name)
    query_type = QueryType.objects.get(name=query_type_name)
    perform_query(index_node, query_type)
    

def perform_query(index_node, query_type):
    """
    do a query and log the results
    """

    when = now()

    resp = do_query(index_node.name,
                    [filter.value for filter in query_type.filters.all()],
                    [facet.name for facet in query_type.facets.all()])

    client, _ = Host.objects.get_or_create(name=gethostname())
    
    response = Response.objects.create(
        index_node=index_node,
        status_code=resp['status_code'],
        datetime=when,
        client=client,
        query_type=query_type)

    if response.status_code == 200:
        
        response_data = ResponseData.objects.create(
            num_found=resp['num_found']
        )
        for facet_name, counts in resp['facet_counts'].items():
            for value, count in counts.items():
                facet, _ = Facet.objects.get_or_create(name=facet_name)
                facet_value, _ = \
                    FacetValue.objects.get_or_create(facet=facet,
                                                     value=value)
                facet_value_count = \
                    FacetValueCount.objects.create(count=count,
                                                  facet_value=facet_value,
                                                  response_data=response_data)
        response.data = response_data
        response.save()

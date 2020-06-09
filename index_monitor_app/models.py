# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Host(models.Model):
    name = models.CharField(unique=True, null=False,
                            blank=False, max_length=80)

    def __str__(self):
        return str(self.name)


class Facet(models.Model):
    name = models.CharField(unique=True, null=False,
                            blank=False, max_length=30)

    def __str__(self):
        return str(self.name)

    
class Filter(models.Model):
    value = models.CharField(unique=True, null=False,
                             blank=False, max_length=80)

    def __str__(self):
        return str(self.value)


class FacetValue(models.Model):
    facet = models.ForeignKey(Facet, blank=False, null=False)
    value = models.CharField(null=False, blank=False, max_length=50)
    unique_together = ('facet', 'value')

    def __str__(self):
        return "{}={}".format(self.facet.name, self.value)

    
class FacetValueCount(models.Model):
    count = models.IntegerField(blank=False, null=False)
    facet_value = models.ForeignKey(FacetValue, blank=False, null=False)
    response_data = models.ForeignKey('ResponseData', blank=False, null=False,
                                      related_name='facet_value_counts')
    def __str__(self):
        return "{}:{}".format(self.facet_value,
                              self.count)

    
class QueryType(models.Model):
    name = models.CharField(unique=True, null=True, blank=True, max_length=30)
    filters = models.ManyToManyField('index_monitor_app.Filter')
    facets = models.ManyToManyField('index_monitor_app.Facet')

    def __str__(self):
        return ("<query type {} (facets {}, filters {})>"
                .format(self.name,
                        ",".join(str(facet) for facet in self.facets.all()),
                        ",".join(str(filter) for filter in self.filters.all())))
        

class ResponseData(models.Model):
    num_found = models.IntegerField(blank=False, null=False)


class Response(models.Model):
    index_node = models.ForeignKey(Host, blank=False, null=False,
                                   related_name='index_node')
    status_code = models.IntegerField(blank=False, null=False)
    datetime = models.DateTimeField(blank=False, null=False)
    data = models.ForeignKey(ResponseData, blank=True, null=True)
    client = models.ForeignKey(Host, blank=True, null=True,
                               related_name='client')
    query_type = models.ForeignKey(QueryType)
    def __str__(self):
        return str("response from {} on {}"
                   .format(self.index_node, self.datetime))


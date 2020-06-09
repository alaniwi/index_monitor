#!/usr/bin/env python3

import django
django.setup()

from index_monitor_app.utils.perform_query import perform_query_by_name


if __name__ == '__main__':

    for index in ['esgf-index1.ceda.ac.uk',
                  'esgf-data.dkrz.de',
                  'esgf-node.llnl.gov',
                  'esgf-node.ipsl.upmc.fr']:
    
        perform_query_by_name(index, 'CMIP6-basic')
    

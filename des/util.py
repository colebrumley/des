'''Utility functions'''

import collections

def flatten(parent_dict, parent_key='', sep='_'):
    '''Flatten a nested dict into a single layer'''
    items = []
    for key, val in parent_dict.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(val, collections.MutableMapping):
            items.extend(flatten(val, new_key, sep=sep).items())
        else:
            items.append((new_key, val))
    return dict(items)

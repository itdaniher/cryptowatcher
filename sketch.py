import typing

Addresses = typing.NamedTuple('Addresses', [('web', str), ('btc', str), ('eth', str)])
Event = typing.NamedTuple('Event', [('uid', str), ('time', float), ('text', str), ('url', str), ('score', float)]) 
Hit = typing.NamedTuple('Hit', [('uid', str), ('time', float), ('events', list), ('url', str), ('score', float), ('addresses', Addresses)]) 

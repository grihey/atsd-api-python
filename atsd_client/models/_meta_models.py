# -*- coding: utf-8 -*-

"""
Copyright 2015 Axibase Corporation or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at

https://www.axibase.com/atsd/axibase-apache-2.0.pdf

or in the "license" file accompanying this file. This file is distributed
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing
permissions and limitations under the License.
"""


class DataType(object):
    SHORT = 'SHORT'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    LONG = 'LONG'
    DOUBLE = 'DOUBLE'


class TimePrecision(object):
    SECONDS = 'SECONDS'
    MILLISECONDS = 'MILLISECONDS'


class InvalidAction(object):
    NONE = 'NONE'
    DISCARD = 'DISCARD'
    TRANSFORM = 'TRANSFORM'


class Metric():
    def __init__(self, 
                 name,
                 label=None,
                 enabled=None,
                 dataType=None,
                 timePrecision=None,
                 persistent=None,
                 filter=None,
                 minValue=None,
                 maxValue=None,
                 invalidAction=None,
                 description=None,
                 retentionInterval=None,
                 lastInsertTime=None,
                 tags=None,
                 versioned=None):
        #: `str` metric name
        self.name = name
        #: `str`
        self.label = label
        #: `bool`
        self.enabled = enabled
        #: :class:`.DataType`
        self.dataType = dataType
        #: :class:`.TimePrecision`
        self.timePrecision = timePrecision
        #: `bool`
        self.persistent = persistent
        #: If filter is specified, metric puts that do not match the filter are discarded
        self.filter = filter
        #: `Number`
        self.minValue = minValue
        #: `Number`
        self.maxValue = maxValue
        #: :class:`.InvalidAction`
        self.invalidAction = invalidAction
        #: `str`
        self.description = description
        #: `Number`
        self.retentionInterval = retentionInterval
        #: `long` milliseconds
        self.lastInsertTime = lastInsertTime
        #: `dict`
        self.tags = tags
        #: `boolean`
        self.versioned = versioned
    
    def __repr__(self):
        return "<METRIC name={name}, label={label}, description={des}".format(name=self.name, label=self.label, des=self.description)

class Entity():
    def __init__(self, name, enabled=None, lastInsertTime=None, tags=None):
        # `str` entity name
        self.name = name
        #: `bool`
        self.enabled = enabled
        #: `long` milliseconds
        self.lastInsertTime = lastInsertTime
        #: `dict`
        self.tags = tags
        
    def __repr__(self):
        return "<Entity name={name}, enabled={enabled}, lastInsertTime={lit}, tags={tags}".format(name=self.name, enabled=self.enabled, lit=self.lastInsertTime, tags=self.tags)

class EntityGroup():
    def __init__(self, name, expression=None, tags=None):
        #: `str` group name
        self.name = name
        #: `str`
        self.expression = expression
        #: `dict`
        self.tags = tags
        
    def __repr__(self):
        return "<EntityGroup name={name}, expression={expression}, tags={tags}".format(name=self.name, expression=self.expression, tags=self.tags)
# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class DebugStats(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DebugStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'describe': 'DebugStatsUnknown',
            'unknown': 'DebugStatsUnknown',
            'handlers': 'list[DebugStatsHandler]'
        }

        self.attribute_map = {
            'describe': 'DESCRIBE',
            'unknown': 'UNKNOWN',
            'handlers': 'handlers'
        }

        self._describe = None
        self._unknown = None
        self._handlers = None

    @property
    def describe(self):
        """
        Gets the describe of this DebugStats.
        Per-method statistics.

        :return: The describe of this DebugStats.
        :rtype: DebugStatsUnknown
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        """
        Sets the describe of this DebugStats.
        Per-method statistics.

        :param describe: The describe of this DebugStats.
        :type: DebugStatsUnknown
        """
        
        self._describe = describe

    @property
    def unknown(self):
        """
        Gets the unknown of this DebugStats.
        Per-method statistics.

        :return: The unknown of this DebugStats.
        :rtype: DebugStatsUnknown
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """
        Sets the unknown of this DebugStats.
        Per-method statistics.

        :param unknown: The unknown of this DebugStats.
        :type: DebugStatsUnknown
        """
        
        self._unknown = unknown

    @property
    def handlers(self):
        """
        Gets the handlers of this DebugStats.


        :return: The handlers of this DebugStats.
        :rtype: list[DebugStatsHandler]
        """
        return self._handlers

    @handlers.setter
    def handlers(self, handlers):
        """
        Sets the handlers of this DebugStats.


        :param handlers: The handlers of this DebugStats.
        :type: list[DebugStatsHandler]
        """
        
        self._handlers = handlers

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

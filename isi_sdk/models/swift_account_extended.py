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


class SwiftAccountExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SwiftAccountExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'swiftgroup': 'str',
            'swiftuser': 'str',
            'users': 'list[str]',
            'zone': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'swiftgroup': 'swiftgroup',
            'swiftuser': 'swiftuser',
            'users': 'users',
            'zone': 'zone',
            'path': 'path'
        }

        self._id = None
        self._name = None
        self._swiftgroup = None
        self._swiftuser = None
        self._users = None
        self._zone = None
        self._path = None

    @property
    def id(self):
        """
        Gets the id of this SwiftAccountExtended.
        Unique id of swift account

        :return: The id of this SwiftAccountExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SwiftAccountExtended.
        Unique id of swift account

        :param id: The id of this SwiftAccountExtended.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SwiftAccountExtended.
        Name of Swift account

        :return: The name of this SwiftAccountExtended.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SwiftAccountExtended.
        Name of Swift account

        :param name: The name of this SwiftAccountExtended.
        :type: str
        """
        
        self._name = name

    @property
    def swiftgroup(self):
        """
        Gets the swiftgroup of this SwiftAccountExtended.
        Group with filesystem ownership of this account

        :return: The swiftgroup of this SwiftAccountExtended.
        :rtype: str
        """
        return self._swiftgroup

    @swiftgroup.setter
    def swiftgroup(self, swiftgroup):
        """
        Sets the swiftgroup of this SwiftAccountExtended.
        Group with filesystem ownership of this account

        :param swiftgroup: The swiftgroup of this SwiftAccountExtended.
        :type: str
        """
        
        self._swiftgroup = swiftgroup

    @property
    def swiftuser(self):
        """
        Gets the swiftuser of this SwiftAccountExtended.
        User with filesystem ownership of this account

        :return: The swiftuser of this SwiftAccountExtended.
        :rtype: str
        """
        return self._swiftuser

    @swiftuser.setter
    def swiftuser(self, swiftuser):
        """
        Sets the swiftuser of this SwiftAccountExtended.
        User with filesystem ownership of this account

        :param swiftuser: The swiftuser of this SwiftAccountExtended.
        :type: str
        """
        
        self._swiftuser = swiftuser

    @property
    def users(self):
        """
        Gets the users of this SwiftAccountExtended.
        Users who are allowed to access Swift account

        :return: The users of this SwiftAccountExtended.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this SwiftAccountExtended.
        Users who are allowed to access Swift account

        :param users: The users of this SwiftAccountExtended.
        :type: list[str]
        """
        
        self._users = users

    @property
    def zone(self):
        """
        Gets the zone of this SwiftAccountExtended.
        Name of access zone for account

        :return: The zone of this SwiftAccountExtended.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """
        Sets the zone of this SwiftAccountExtended.
        Name of access zone for account

        :param zone: The zone of this SwiftAccountExtended.
        :type: str
        """
        
        self._zone = zone

    @property
    def path(self):
        """
        Gets the path of this SwiftAccountExtended.
        Path to root of Swift account

        :return: The path of this SwiftAccountExtended.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this SwiftAccountExtended.
        Path to root of Swift account

        :param path: The path of this SwiftAccountExtended.
        :type: str
        """
        
        self._path = path

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

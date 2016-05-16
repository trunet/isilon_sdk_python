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


class CloudPoolExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudPoolExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'accounts': 'list[str]',
            'birth_cluster_id': 'str',
            'description': 'str',
            'name': 'str',
            'vendor': 'str',
            'id': 'str',
            'state': 'str',
            'state_details': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'accounts': 'accounts',
            'birth_cluster_id': 'birth_cluster_id',
            'description': 'description',
            'name': 'name',
            'vendor': 'vendor',
            'id': 'id',
            'state': 'state',
            'state_details': 'state_details',
            'type': 'type'
        }

        self._accounts = None
        self._birth_cluster_id = None
        self._description = None
        self._name = None
        self._vendor = None
        self._id = None
        self._state = None
        self._state_details = None
        self._type = None

    @property
    def accounts(self):
        """
        Gets the accounts of this CloudPoolExtended.
        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.

        :return: The accounts of this CloudPoolExtended.
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """
        Sets the accounts of this CloudPoolExtended.
        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.

        :param accounts: The accounts of this CloudPoolExtended.
        :type: list[str]
        """
        
        self._accounts = accounts

    @property
    def birth_cluster_id(self):
        """
        Gets the birth_cluster_id of this CloudPoolExtended.
        The guid of the cluster where this pool was created

        :return: The birth_cluster_id of this CloudPoolExtended.
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """
        Sets the birth_cluster_id of this CloudPoolExtended.
        The guid of the cluster where this pool was created

        :param birth_cluster_id: The birth_cluster_id of this CloudPoolExtended.
        :type: str
        """
        
        self._birth_cluster_id = birth_cluster_id

    @property
    def description(self):
        """
        Gets the description of this CloudPoolExtended.
        A brief description of this pool

        :return: The description of this CloudPoolExtended.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CloudPoolExtended.
        A brief description of this pool

        :param description: The description of this CloudPoolExtended.
        :type: str
        """
        
        self._description = description

    @property
    def name(self):
        """
        Gets the name of this CloudPoolExtended.
        A unique name for this pool

        :return: The name of this CloudPoolExtended.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudPoolExtended.
        A unique name for this pool

        :param name: The name of this CloudPoolExtended.
        :type: str
        """
        
        self._name = name

    @property
    def vendor(self):
        """
        Gets the vendor of this CloudPoolExtended.
        A string identifier of the cloud services vendor

        :return: The vendor of this CloudPoolExtended.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this CloudPoolExtended.
        A string identifier of the cloud services vendor

        :param vendor: The vendor of this CloudPoolExtended.
        :type: str
        """
        
        self._vendor = vendor

    @property
    def id(self):
        """
        Gets the id of this CloudPoolExtended.
        A unique name for this pool

        :return: The id of this CloudPoolExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudPoolExtended.
        A unique name for this pool

        :param id: The id of this CloudPoolExtended.
        :type: str
        """
        
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this CloudPoolExtended.
        Indicates whether this pool is in a good state (\"OK\") or disabled (\"disabled\")

        :return: The state of this CloudPoolExtended.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CloudPoolExtended.
        Indicates whether this pool is in a good state (\"OK\") or disabled (\"disabled\")

        :param state: The state of this CloudPoolExtended.
        :type: str
        """
        allowed_values = ["OK", "disabled"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )

        self._state = state

    @property
    def state_details(self):
        """
        Gets the state_details of this CloudPoolExtended.
        Gives further information to describe the state of this pool

        :return: The state_details of this CloudPoolExtended.
        :rtype: str
        """
        return self._state_details

    @state_details.setter
    def state_details(self, state_details):
        """
        Sets the state_details of this CloudPoolExtended.
        Gives further information to describe the state of this pool

        :param state_details: The state_details of this CloudPoolExtended.
        :type: str
        """
        
        self._state_details = state_details

    @property
    def type(self):
        """
        Gets the type of this CloudPoolExtended.
        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"ecs2\" for EMC Elastic Cloud Storage Service, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3

        :return: The type of this CloudPoolExtended.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloudPoolExtended.
        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"ecs2\" for EMC Elastic Cloud Storage Service, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3

        :param type: The type of this CloudPoolExtended.
        :type: str
        """
        allowed_values = ["isilon", "ecs", "ecs2", "azure", "s3", "ran"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )

        self._type = type

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

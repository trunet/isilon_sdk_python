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


class ClusterNodesAvailableNode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterNodesAvailableNode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'configuration_id': 'str',
            'description': 'str',
            'product': 'str',
            'serial_number': 'str',
            'status': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'configuration_id': 'configuration_id',
            'description': 'description',
            'product': 'product',
            'serial_number': 'serial_number',
            'status': 'status',
            'version': 'version'
        }

        self._configuration_id = None
        self._description = None
        self._product = None
        self._serial_number = None
        self._status = None
        self._version = None

    @property
    def configuration_id(self):
        """
        Gets the configuration_id of this ClusterNodesAvailableNode.
        Node configuration ID.

        :return: The configuration_id of this ClusterNodesAvailableNode.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """
        Sets the configuration_id of this ClusterNodesAvailableNode.
        Node configuration ID.

        :param configuration_id: The configuration_id of this ClusterNodesAvailableNode.
        :type: str
        """
        
        self._configuration_id = configuration_id

    @property
    def description(self):
        """
        Gets the description of this ClusterNodesAvailableNode.
        Human-readable description giving further detail on status (may be empty)

        :return: The description of this ClusterNodesAvailableNode.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ClusterNodesAvailableNode.
        Human-readable description giving further detail on status (may be empty)

        :param description: The description of this ClusterNodesAvailableNode.
        :type: str
        """
        
        self._description = description

    @property
    def product(self):
        """
        Gets the product of this ClusterNodesAvailableNode.
        Isilon product name.

        :return: The product of this ClusterNodesAvailableNode.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ClusterNodesAvailableNode.
        Isilon product name.

        :param product: The product of this ClusterNodesAvailableNode.
        :type: str
        """
        
        self._product = product

    @property
    def serial_number(self):
        """
        Gets the serial_number of this ClusterNodesAvailableNode.
        Serial number of this node.

        :return: The serial_number of this ClusterNodesAvailableNode.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this ClusterNodesAvailableNode.
        Serial number of this node.

        :param serial_number: The serial_number of this ClusterNodesAvailableNode.
        :type: str
        """
        
        self._serial_number = serial_number

    @property
    def status(self):
        """
        Gets the status of this ClusterNodesAvailableNode.
        Availability of the node.

        :return: The status of this ClusterNodesAvailableNode.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClusterNodesAvailableNode.
        Availability of the node.

        :param status: The status of this ClusterNodesAvailableNode.
        :type: str
        """
        allowed_values = ["available", "waiting", "error", "error_permanent", "working", "rebooting", "exiting"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )

        self._status = status

    @property
    def version(self):
        """
        Gets the version of this ClusterNodesAvailableNode.
        OneFS build version running on the node.

        :return: The version of this ClusterNodesAvailableNode.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ClusterNodesAvailableNode.
        OneFS build version running on the node.

        :param version: The version of this ClusterNodesAvailableNode.
        :type: str
        """
        
        self._version = version

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

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


class AuthUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'enabled': 'bool',
            'expiry': 'int',
            'gecos': 'str',
            'home_directory': 'str',
            'password': 'str',
            'password_expires': 'bool',
            'primary_group': 'GroupMember',
            'prompt_password_change': 'bool',
            'shell': 'str',
            'sid': 'str',
            'uid': 'int',
            'unlock': 'bool'
        }

        self.attribute_map = {
            'email': 'email',
            'enabled': 'enabled',
            'expiry': 'expiry',
            'gecos': 'gecos',
            'home_directory': 'home_directory',
            'password': 'password',
            'password_expires': 'password_expires',
            'primary_group': 'primary_group',
            'prompt_password_change': 'prompt_password_change',
            'shell': 'shell',
            'sid': 'sid',
            'uid': 'uid',
            'unlock': 'unlock'
        }

        self._email = None
        self._enabled = None
        self._expiry = None
        self._gecos = None
        self._home_directory = None
        self._password = None
        self._password_expires = None
        self._primary_group = None
        self._prompt_password_change = None
        self._shell = None
        self._sid = None
        self._uid = None
        self._unlock = None

    @property
    def email(self):
        """
        Gets the email of this AuthUser.
        Specifies an email address for the user.

        :return: The email of this AuthUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AuthUser.
        Specifies an email address for the user.

        :param email: The email of this AuthUser.
        :type: str
        """
        
        self._email = email

    @property
    def enabled(self):
        """
        Gets the enabled of this AuthUser.
        If true, the authenticated user is enabled.

        :return: The enabled of this AuthUser.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AuthUser.
        If true, the authenticated user is enabled.

        :param enabled: The enabled of this AuthUser.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def expiry(self):
        """
        Gets the expiry of this AuthUser.
        Specifies the Unix Epoch time when the auth user will expire.

        :return: The expiry of this AuthUser.
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """
        Sets the expiry of this AuthUser.
        Specifies the Unix Epoch time when the auth user will expire.

        :param expiry: The expiry of this AuthUser.
        :type: int
        """
        
        self._expiry = expiry

    @property
    def gecos(self):
        """
        Gets the gecos of this AuthUser.
        Specifies the GECOS value, which is usually the full name.

        :return: The gecos of this AuthUser.
        :rtype: str
        """
        return self._gecos

    @gecos.setter
    def gecos(self, gecos):
        """
        Sets the gecos of this AuthUser.
        Specifies the GECOS value, which is usually the full name.

        :param gecos: The gecos of this AuthUser.
        :type: str
        """
        
        self._gecos = gecos

    @property
    def home_directory(self):
        """
        Gets the home_directory of this AuthUser.
        Specifies a home directory for the user.

        :return: The home_directory of this AuthUser.
        :rtype: str
        """
        return self._home_directory

    @home_directory.setter
    def home_directory(self, home_directory):
        """
        Sets the home_directory of this AuthUser.
        Specifies a home directory for the user.

        :param home_directory: The home_directory of this AuthUser.
        :type: str
        """
        
        self._home_directory = home_directory

    @property
    def password(self):
        """
        Gets the password of this AuthUser.
        Changes the password for the user.

        :return: The password of this AuthUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this AuthUser.
        Changes the password for the user.

        :param password: The password of this AuthUser.
        :type: str
        """
        
        self._password = password

    @property
    def password_expires(self):
        """
        Gets the password_expires of this AuthUser.
        If true, the password should expire.

        :return: The password_expires of this AuthUser.
        :rtype: bool
        """
        return self._password_expires

    @password_expires.setter
    def password_expires(self, password_expires):
        """
        Sets the password_expires of this AuthUser.
        If true, the password should expire.

        :param password_expires: The password_expires of this AuthUser.
        :type: bool
        """
        
        self._password_expires = password_expires

    @property
    def primary_group(self):
        """
        Gets the primary_group of this AuthUser.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The primary_group of this AuthUser.
        :rtype: GroupMember
        """
        return self._primary_group

    @primary_group.setter
    def primary_group(self, primary_group):
        """
        Sets the primary_group of this AuthUser.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param primary_group: The primary_group of this AuthUser.
        :type: GroupMember
        """
        
        self._primary_group = primary_group

    @property
    def prompt_password_change(self):
        """
        Gets the prompt_password_change of this AuthUser.
        If true, prompts the user to change their password at the next login.

        :return: The prompt_password_change of this AuthUser.
        :rtype: bool
        """
        return self._prompt_password_change

    @prompt_password_change.setter
    def prompt_password_change(self, prompt_password_change):
        """
        Sets the prompt_password_change of this AuthUser.
        If true, prompts the user to change their password at the next login.

        :param prompt_password_change: The prompt_password_change of this AuthUser.
        :type: bool
        """
        
        self._prompt_password_change = prompt_password_change

    @property
    def shell(self):
        """
        Gets the shell of this AuthUser.
        Specifies the shell for the user.

        :return: The shell of this AuthUser.
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """
        Sets the shell of this AuthUser.
        Specifies the shell for the user.

        :param shell: The shell of this AuthUser.
        :type: str
        """
        
        self._shell = shell

    @property
    def sid(self):
        """
        Gets the sid of this AuthUser.
        Specifies a security identifier.

        :return: The sid of this AuthUser.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this AuthUser.
        Specifies a security identifier.

        :param sid: The sid of this AuthUser.
        :type: str
        """
        
        self._sid = sid

    @property
    def uid(self):
        """
        Gets the uid of this AuthUser.
        Specifies a numeric user identifier.

        :return: The uid of this AuthUser.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this AuthUser.
        Specifies a numeric user identifier.

        :param uid: The uid of this AuthUser.
        :type: int
        """
        
        self._uid = uid

    @property
    def unlock(self):
        """
        Gets the unlock of this AuthUser.
        If true, the user account should be unlocked.

        :return: The unlock of this AuthUser.
        :rtype: bool
        """
        return self._unlock

    @unlock.setter
    def unlock(self, unlock):
        """
        Sets the unlock of this AuthUser.
        If true, the user account should be unlocked.

        :param unlock: The unlock of this AuthUser.
        :type: bool
        """
        
        self._unlock = unlock

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

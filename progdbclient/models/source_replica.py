# coding: utf-8

"""
    Snippets API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from progdbclient.configuration import Configuration


class SourceReplica(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'human_decription': 'str',
        'machine_description': 'str',
        'is_main': 'str',
        'module': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'human_decription': 'human_decription',
        'machine_description': 'machine_description',
        'is_main': 'is_main',
        'module': 'module'
    }

    def __init__(self, id=None, name=None, human_decription=None, machine_description=None, is_main=None, module=None, _configuration=None):  # noqa: E501
        """SourceReplica - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._human_decription = None
        self._machine_description = None
        self._is_main = None
        self._module = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.human_decription = human_decription
        self.machine_description = machine_description
        self.is_main = is_main
        if module is not None:
            self.module = module

    @property
    def id(self):
        """Gets the id of this SourceReplica.  # noqa: E501


        :return: The id of this SourceReplica.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceReplica.


        :param id: The id of this SourceReplica.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SourceReplica.  # noqa: E501


        :return: The name of this SourceReplica.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceReplica.


        :param name: The name of this SourceReplica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def human_decription(self):
        """Gets the human_decription of this SourceReplica.  # noqa: E501


        :return: The human_decription of this SourceReplica.  # noqa: E501
        :rtype: str
        """
        return self._human_decription

    @human_decription.setter
    def human_decription(self, human_decription):
        """Sets the human_decription of this SourceReplica.


        :param human_decription: The human_decription of this SourceReplica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and human_decription is None:
            raise ValueError("Invalid value for `human_decription`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                human_decription is not None and len(human_decription) < 1):
            raise ValueError("Invalid value for `human_decription`, length must be greater than or equal to `1`")  # noqa: E501

        self._human_decription = human_decription

    @property
    def machine_description(self):
        """Gets the machine_description of this SourceReplica.  # noqa: E501


        :return: The machine_description of this SourceReplica.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this SourceReplica.


        :param machine_description: The machine_description of this SourceReplica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and machine_description is None:
            raise ValueError("Invalid value for `machine_description`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                machine_description is not None and len(machine_description) < 1):
            raise ValueError("Invalid value for `machine_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._machine_description = machine_description

    @property
    def is_main(self):
        """Gets the is_main of this SourceReplica.  # noqa: E501


        :return: The is_main of this SourceReplica.  # noqa: E501
        :rtype: str
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this SourceReplica.


        :param is_main: The is_main of this SourceReplica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and is_main is None:
            raise ValueError("Invalid value for `is_main`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                is_main is not None and len(is_main) < 1):
            raise ValueError("Invalid value for `is_main`, length must be greater than or equal to `1`")  # noqa: E501

        self._is_main = is_main

    @property
    def module(self):
        """Gets the module of this SourceReplica.  # noqa: E501


        :return: The module of this SourceReplica.  # noqa: E501
        :rtype: int
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this SourceReplica.


        :param module: The module of this SourceReplica.  # noqa: E501
        :type: int
        """

        self._module = module

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SourceReplica, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceReplica):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceReplica):
            return True

        return self.to_dict() != other.to_dict()

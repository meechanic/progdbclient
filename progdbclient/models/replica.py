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


class Replica(object):
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
        'is_installation': 'str',
        'location': 'str',
        'replica_collection': 'str',
        'module': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'human_decription': 'human_decription',
        'machine_description': 'machine_description',
        'is_main': 'is_main',
        'is_installation': 'is_installation',
        'location': 'location',
        'replica_collection': 'replica_collection',
        'module': 'module'
    }

    def __init__(self, id=None, name=None, human_decription=None, machine_description=None, is_main=None, is_installation=None, location=None, replica_collection=None, module=None, _configuration=None):  # noqa: E501
        """Replica - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._human_decription = None
        self._machine_description = None
        self._is_main = None
        self._is_installation = None
        self._location = None
        self._replica_collection = None
        self._module = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.human_decription = human_decription
        self.machine_description = machine_description
        self.is_main = is_main
        self.is_installation = is_installation
        self.location = location
        self.replica_collection = replica_collection
        if module is not None:
            self.module = module

    @property
    def id(self):
        """Gets the id of this Replica.  # noqa: E501


        :return: The id of this Replica.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Replica.


        :param id: The id of this Replica.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Replica.  # noqa: E501


        :return: The name of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Replica.


        :param name: The name of this Replica.  # noqa: E501
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
        """Gets the human_decription of this Replica.  # noqa: E501


        :return: The human_decription of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._human_decription

    @human_decription.setter
    def human_decription(self, human_decription):
        """Sets the human_decription of this Replica.


        :param human_decription: The human_decription of this Replica.  # noqa: E501
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
        """Gets the machine_description of this Replica.  # noqa: E501


        :return: The machine_description of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this Replica.


        :param machine_description: The machine_description of this Replica.  # noqa: E501
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
        """Gets the is_main of this Replica.  # noqa: E501


        :return: The is_main of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this Replica.


        :param is_main: The is_main of this Replica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and is_main is None:
            raise ValueError("Invalid value for `is_main`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                is_main is not None and len(is_main) < 1):
            raise ValueError("Invalid value for `is_main`, length must be greater than or equal to `1`")  # noqa: E501

        self._is_main = is_main

    @property
    def is_installation(self):
        """Gets the is_installation of this Replica.  # noqa: E501


        :return: The is_installation of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._is_installation

    @is_installation.setter
    def is_installation(self, is_installation):
        """Sets the is_installation of this Replica.


        :param is_installation: The is_installation of this Replica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and is_installation is None:
            raise ValueError("Invalid value for `is_installation`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                is_installation is not None and len(is_installation) < 1):
            raise ValueError("Invalid value for `is_installation`, length must be greater than or equal to `1`")  # noqa: E501

        self._is_installation = is_installation

    @property
    def location(self):
        """Gets the location of this Replica.  # noqa: E501


        :return: The location of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Replica.


        :param location: The location of this Replica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                location is not None and len(location) < 1):
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `1`")  # noqa: E501

        self._location = location

    @property
    def replica_collection(self):
        """Gets the replica_collection of this Replica.  # noqa: E501


        :return: The replica_collection of this Replica.  # noqa: E501
        :rtype: str
        """
        return self._replica_collection

    @replica_collection.setter
    def replica_collection(self, replica_collection):
        """Sets the replica_collection of this Replica.


        :param replica_collection: The replica_collection of this Replica.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and replica_collection is None:
            raise ValueError("Invalid value for `replica_collection`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                replica_collection is not None and len(replica_collection) < 1):
            raise ValueError("Invalid value for `replica_collection`, length must be greater than or equal to `1`")  # noqa: E501

        self._replica_collection = replica_collection

    @property
    def module(self):
        """Gets the module of this Replica.  # noqa: E501


        :return: The module of this Replica.  # noqa: E501
        :rtype: int
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this Replica.


        :param module: The module of this Replica.  # noqa: E501
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
        if issubclass(Replica, dict):
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
        if not isinstance(other, Replica):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Replica):
            return True

        return self.to_dict() != other.to_dict()
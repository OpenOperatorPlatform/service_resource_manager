# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.add_iot_device_location import AddIotDeviceLocation  # noqa: F401,E501
from swagger_server.models.iot_value import IotValue  # noqa: F401,E501
from swagger_server import util


class AddIotDevice(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, device_name: str=None, description: str=None, device_cluster: str=None, location: AddIotDeviceLocation=None, values: List[IotValue]=None):  # noqa: E501
        """AddIotDevice - a model defined in Swagger

        :param device_name: The device_name of this AddIotDevice.  # noqa: E501
        :type device_name: str
        :param description: The description of this AddIotDevice.  # noqa: E501
        :type description: str
        :param device_cluster: The device_cluster of this AddIotDevice.  # noqa: E501
        :type device_cluster: str
        :param location: The location of this AddIotDevice.  # noqa: E501
        :type location: AddIotDeviceLocation
        :param values: The values of this AddIotDevice.  # noqa: E501
        :type values: List[IotValue]
        """
        self.swagger_types = {
            'device_name': str,
            'description': str,
            'device_cluster': str,
            'location': AddIotDeviceLocation,
            'values': List[IotValue]
        }

        self.attribute_map = {
            'device_name': 'device_name',
            'description': 'description',
            'device_cluster': 'device_cluster',
            'location': 'location',
            'values': 'values'
        }
        self._device_name = device_name
        self._description = description
        self._device_cluster = device_cluster
        self._location = location
        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'AddIotDevice':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The addIotDevice of this AddIotDevice.  # noqa: E501
        :rtype: AddIotDevice
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_name(self) -> str:
        """Gets the device_name of this AddIotDevice.


        :return: The device_name of this AddIotDevice.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name: str):
        """Sets the device_name of this AddIotDevice.


        :param device_name: The device_name of this AddIotDevice.
        :type device_name: str
        """

        self._device_name = device_name

    @property
    def description(self) -> str:
        """Gets the description of this AddIotDevice.


        :return: The description of this AddIotDevice.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this AddIotDevice.


        :param description: The description of this AddIotDevice.
        :type description: str
        """

        self._description = description

    @property
    def device_cluster(self) -> str:
        """Gets the device_cluster of this AddIotDevice.


        :return: The device_cluster of this AddIotDevice.
        :rtype: str
        """
        return self._device_cluster

    @device_cluster.setter
    def device_cluster(self, device_cluster: str):
        """Sets the device_cluster of this AddIotDevice.


        :param device_cluster: The device_cluster of this AddIotDevice.
        :type device_cluster: str
        """

        self._device_cluster = device_cluster

    @property
    def location(self) -> AddIotDeviceLocation:
        """Gets the location of this AddIotDevice.


        :return: The location of this AddIotDevice.
        :rtype: AddIotDeviceLocation
        """
        return self._location

    @location.setter
    def location(self, location: AddIotDeviceLocation):
        """Sets the location of this AddIotDevice.


        :param location: The location of this AddIotDevice.
        :type location: AddIotDeviceLocation
        """

        self._location = location

    @property
    def values(self) -> List[IotValue]:
        """Gets the values of this AddIotDevice.


        :return: The values of this AddIotDevice.
        :rtype: List[IotValue]
        """
        return self._values

    @values.setter
    def values(self, values: List[IotValue]):
        """Sets the values of this AddIotDevice.


        :param values: The values of this AddIotDevice.
        :type values: List[IotValue]
        """

        self._values = values

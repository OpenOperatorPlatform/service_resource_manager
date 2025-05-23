# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PaasSFInstanceSpec(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, service_function_name: str=None, service_function_instance_name: str=None):  # noqa: E501
        """PaasSFInstanceSpec - a model defined in Swagger

        :param service_function_name: The paas_service_name of this PaasSFInstanceSpec.  # noqa: E501
        :type service_function_name: str
        :param service_function_instance_name: The service_function_instance_name of this PaasSFInstanceSpec.  # noqa: E501
        :type service_function_instance_name: str
        """
        self.swagger_types = {
            'service_function_name': str,
            'service_function_instance_name': str,

        }

        self.attribute_map = {
            'service_function_name': 'service_function_name',
            'service_function_instance_name': 'service_function_instance_name',

        }
        self._service_function_name = service_function_name
        self._service_function_instance_name = service_function_instance_name


    @classmethod
    def from_dict(cls, dikt) -> 'PaasSFInstanceSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The deployPaas of this DeployPaas.  # noqa: E501
        :rtype: DeployPaas
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_function_name(self) -> str:
        """Gets the paas_service_name of this DeployPaas.


        :return: The paas_service_name of this DeployPaas.
        :rtype: str
        """
        return self._service_function_name

    @service_function_name.setter
    def service_function_name(self, service_function_name: str):
        """Sets the service_function_name of this DeployPaas.


        :param service_function_name: The service_function_name of this DeployPaas.
        :type service_function_name: str
        """

        self._service_function_name = service_function_name

    @property
    def service_function_instance_name(self) -> str:
        """Gets the service_function_instance_name of this DeployPaas.


        :return: The service_function_instance_name of this DeployPaas.
        :rtype: str
        """
        return self._service_function_instance_name

    @service_function_instance_name.setter
    def service_function_instance_name(self, service_function_instance_name: str):
        """Sets the service_function_instance_name of this DeployPaas.


        :param service_function_instance_name: The service_function_instance_name of this DeployPaas.
        :type service_function_instance_name: str
        """

        self._service_function_instance_name = service_function_instance_name

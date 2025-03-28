# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ServicesQuery(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, service_consumer_id: str=None, query_string: str=None):  # noqa: E501
        """ServicesQuery - a model defined in Swagger

        :param service_consumer_id: The service_consumer_id of this ServicesQuery.  # noqa: E501
        :type service_consumer_id: str
        :param query_string: The query_string of this ServicesQuery.  # noqa: E501
        :type query_string: str
        """
        self.swagger_types = {
            'service_consumer_id': str,
            'query_string': str
        }

        self.attribute_map = {
            'service_consumer_id': 'serviceConsumerId',
            'query_string': 'queryString'
        }
        self._service_consumer_id = service_consumer_id
        self._query_string = query_string

    @classmethod
    def from_dict(cls, dikt) -> 'ServicesQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The servicesQuery of this ServicesQuery.  # noqa: E501
        :rtype: ServicesQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_consumer_id(self) -> str:
        """Gets the service_consumer_id of this ServicesQuery.


        :return: The service_consumer_id of this ServicesQuery.
        :rtype: str
        """
        return self._service_consumer_id

    @service_consumer_id.setter
    def service_consumer_id(self, service_consumer_id: str):
        """Sets the service_consumer_id of this ServicesQuery.


        :param service_consumer_id: The service_consumer_id of this ServicesQuery.
        :type service_consumer_id: str
        """

        self._service_consumer_id = service_consumer_id

    @property
    def query_string(self) -> str:
        """Gets the query_string of this ServicesQuery.


        :return: The query_string of this ServicesQuery.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string: str):
        """Sets the query_string of this ServicesQuery.


        :param query_string: The query_string of this ServicesQuery.
        :type query_string: str
        """

        self._query_string = query_string

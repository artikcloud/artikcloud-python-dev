# coding: utf-8

"""
    ARTIK Cloud API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UsersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_user_properties(self, user_id, properties, **kwargs):
        """
        Create User Application Properties
        Create application properties for a user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_properties(user_id, properties, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param AppProperties properties: Properties to be updated (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_user_properties_with_http_info(user_id, properties, **kwargs)
        else:
            (data) = self.create_user_properties_with_http_info(user_id, properties, **kwargs)
            return data

    def create_user_properties_with_http_info(self, user_id, properties, **kwargs):
        """
        Create User Application Properties
        Create application properties for a user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_properties_with_http_info(user_id, properties, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param AppProperties properties: Properties to be updated (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'properties', 'aid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `create_user_properties`")
        # verify the required parameter 'properties' is set
        if ('properties' not in params) or (params['properties'] is None):
            raise ValueError("Missing the required parameter `properties` when calling `create_user_properties`")

        resource_path = '/users/{userId}/properties'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'aid' in params:
            query_params['aid'] = params['aid']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'properties' in params:
            body_params = params['properties']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PropertiesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_user_properties(self, user_id, **kwargs):
        """
        Delete User Application Properties
        Deletes a user's application properties

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_properties(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_user_properties_with_http_info(user_id, **kwargs)
        else:
            (data) = self.delete_user_properties_with_http_info(user_id, **kwargs)
            return data

    def delete_user_properties_with_http_info(self, user_id, **kwargs):
        """
        Delete User Application Properties
        Deletes a user's application properties

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_properties_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'aid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user_properties`")

        resource_path = '/users/{userId}/properties'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'aid' in params:
            query_params['aid'] = params['aid']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PropertiesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_self(self, **kwargs):
        """
        Get Current User Profile
        Get's the current user's profile

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_self(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_self_with_http_info(**kwargs)
        else:
            (data) = self.get_self_with_http_info(**kwargs)
            return data

    def get_self_with_http_info(self, **kwargs):
        """
        Get Current User Profile
        Get's the current user's profile

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_self_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_self" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/users/self'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UserEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_user_device_types(self, user_id, **kwargs):
        """
        Get User Device Types
        Retrieve User's Device Types

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_device_types(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID. (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set
        :param bool include_shared: Optional. Boolean (true/false) - If false, only return the user's device types. If true, also return device types shared by other users.
        :return: DeviceTypesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_device_types_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_device_types_with_http_info(user_id, **kwargs)
            return data

    def get_user_device_types_with_http_info(self, user_id, **kwargs):
        """
        Get User Device Types
        Retrieve User's Device Types

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_device_types_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID. (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set
        :param bool include_shared: Optional. Boolean (true/false) - If false, only return the user's device types. If true, also return device types shared by other users.
        :return: DeviceTypesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'offset', 'count', 'include_shared']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_device_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_device_types`")

        resource_path = '/users/{userId}/devicetypes'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'include_shared' in params:
            query_params['includeShared'] = params['include_shared']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceTypesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_user_devices(self, user_id, **kwargs):
        """
        Get User Devices
        Retrieve User's Devices

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_devices(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set
        :param bool include_properties: Optional. Boolean (true/false) - If false, only return the user's device types. If true, also return device types shared by other users.
        :return: DevicesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_devices_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_devices_with_http_info(user_id, **kwargs)
            return data

    def get_user_devices_with_http_info(self, user_id, **kwargs):
        """
        Get User Devices
        Retrieve User's Devices

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_devices_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set
        :param bool include_properties: Optional. Boolean (true/false) - If false, only return the user's device types. If true, also return device types shared by other users.
        :return: DevicesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'offset', 'count', 'include_properties']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_devices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_devices`")

        resource_path = '/users/{userId}/devices'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'include_properties' in params:
            query_params['includeProperties'] = params['include_properties']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DevicesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_user_properties(self, user_id, **kwargs):
        """
        Get User application properties
        Get application properties of a user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_properties(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_properties_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_properties_with_http_info(user_id, **kwargs)
            return data

    def get_user_properties_with_http_info(self, user_id, **kwargs):
        """
        Get User application properties
        Get application properties of a user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_properties_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'aid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_properties`")

        resource_path = '/users/{userId}/properties'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'aid' in params:
            query_params['aid'] = params['aid']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PropertiesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_user_rules(self, user_id, **kwargs):
        """
        Get User Rules
        Retrieve User's Rules

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_rules(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID. (required)
        :param bool exclude_disabled: Exclude disabled rules in the result.
        :param int count: Desired count of items in the result set.
        :param int offset: Offset for pagination.
        :return: RulesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_rules_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_rules_with_http_info(user_id, **kwargs)
            return data

    def get_user_rules_with_http_info(self, user_id, **kwargs):
        """
        Get User Rules
        Retrieve User's Rules

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_rules_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID. (required)
        :param bool exclude_disabled: Exclude disabled rules in the result.
        :param int count: Desired count of items in the result set.
        :param int offset: Offset for pagination.
        :return: RulesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'exclude_disabled', 'count', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_rules`")

        resource_path = '/users/{userId}/rules'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'exclude_disabled' in params:
            query_params['excludeDisabled'] = params['exclude_disabled']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'offset' in params:
            query_params['offset'] = params['offset']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RulesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_user_properties(self, user_id, properties, **kwargs):
        """
        Update User Application Properties
        Updates application properties of a user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user_properties(user_id, properties, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param AppProperties properties: Properties to be updated (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_user_properties_with_http_info(user_id, properties, **kwargs)
        else:
            (data) = self.update_user_properties_with_http_info(user_id, properties, **kwargs)
            return data

    def update_user_properties_with_http_info(self, user_id, properties, **kwargs):
        """
        Update User Application Properties
        Updates application properties of a user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user_properties_with_http_info(user_id, properties, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User Id (required)
        :param AppProperties properties: Properties to be updated (required)
        :param str aid: Application ID
        :return: PropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'properties', 'aid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_user_properties`")
        # verify the required parameter 'properties' is set
        if ('properties' not in params) or (params['properties'] is None):
            raise ValueError("Missing the required parameter `properties` when calling `update_user_properties`")

        resource_path = '/users/{userId}/properties'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'aid' in params:
            query_params['aid'] = params['aid']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'properties' in params:
            body_params = params['properties']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PropertiesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

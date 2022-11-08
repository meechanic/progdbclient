# progdbclient.ApireplicaApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apireplica_create**](ApireplicaApi.md#apireplica_create) | **POST** /apireplica/ | 
[**apireplica_delete**](ApireplicaApi.md#apireplica_delete) | **DELETE** /apireplica/{id}/ | 
[**apireplica_list**](ApireplicaApi.md#apireplica_list) | **GET** /apireplica/ | 
[**apireplica_partial_update**](ApireplicaApi.md#apireplica_partial_update) | **PATCH** /apireplica/{id}/ | 
[**apireplica_read**](ApireplicaApi.md#apireplica_read) | **GET** /apireplica/{id}/ | 
[**apireplica_update**](ApireplicaApi.md#apireplica_update) | **PUT** /apireplica/{id}/ | 


# **apireplica_create**
> Replica apireplica_create(data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import progdbclient
from progdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = progdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = progdbclient.ApireplicaApi(progdbclient.ApiClient(configuration))
data = progdbclient.Replica() # Replica | 

try:
    api_response = api_instance.apireplica_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApireplicaApi->apireplica_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Replica**](Replica.md)|  | 

### Return type

[**Replica**](Replica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apireplica_delete**
> apireplica_delete(id)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import progdbclient
from progdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = progdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = progdbclient.ApireplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.

try:
    api_instance.apireplica_delete(id)
except ApiException as e:
    print("Exception when calling ApireplicaApi->apireplica_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this replica. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apireplica_list**
> list[Replica] apireplica_list(name=name, search=search, ordering=ordering)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import progdbclient
from progdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = progdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = progdbclient.ApireplicaApi(progdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apireplica_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApireplicaApi->apireplica_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Replica]**](Replica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apireplica_partial_update**
> Replica apireplica_partial_update(id, data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import progdbclient
from progdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = progdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = progdbclient.ApireplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.
data = progdbclient.Replica() # Replica | 

try:
    api_response = api_instance.apireplica_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApireplicaApi->apireplica_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this replica. | 
 **data** | [**Replica**](Replica.md)|  | 

### Return type

[**Replica**](Replica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apireplica_read**
> Replica apireplica_read(id)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import progdbclient
from progdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = progdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = progdbclient.ApireplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.

try:
    api_response = api_instance.apireplica_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApireplicaApi->apireplica_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this replica. | 

### Return type

[**Replica**](Replica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apireplica_update**
> Replica apireplica_update(id, data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import progdbclient
from progdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = progdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = progdbclient.ApireplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.
data = progdbclient.Replica() # Replica | 

try:
    api_response = api_instance.apireplica_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApireplicaApi->apireplica_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this replica. | 
 **data** | [**Replica**](Replica.md)|  | 

### Return type

[**Replica**](Replica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


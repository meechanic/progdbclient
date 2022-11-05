# progdbclient.ApisourcereplicaApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apisourcereplica_create**](ApisourcereplicaApi.md#apisourcereplica_create) | **POST** /apisourcereplica/ | 
[**apisourcereplica_delete**](ApisourcereplicaApi.md#apisourcereplica_delete) | **DELETE** /apisourcereplica/{id}/ | 
[**apisourcereplica_list**](ApisourcereplicaApi.md#apisourcereplica_list) | **GET** /apisourcereplica/ | 
[**apisourcereplica_partial_update**](ApisourcereplicaApi.md#apisourcereplica_partial_update) | **PATCH** /apisourcereplica/{id}/ | 
[**apisourcereplica_read**](ApisourcereplicaApi.md#apisourcereplica_read) | **GET** /apisourcereplica/{id}/ | 
[**apisourcereplica_update**](ApisourcereplicaApi.md#apisourcereplica_update) | **PUT** /apisourcereplica/{id}/ | 


# **apisourcereplica_create**
> SourceReplica apisourcereplica_create(data)



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
api_instance = progdbclient.ApisourcereplicaApi(progdbclient.ApiClient(configuration))
data = progdbclient.SourceReplica() # SourceReplica | 

try:
    api_response = api_instance.apisourcereplica_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcereplicaApi->apisourcereplica_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SourceReplica**](SourceReplica.md)|  | 

### Return type

[**SourceReplica**](SourceReplica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcereplica_delete**
> apisourcereplica_delete(id)



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
api_instance = progdbclient.ApisourcereplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source replica.

try:
    api_instance.apisourcereplica_delete(id)
except ApiException as e:
    print("Exception when calling ApisourcereplicaApi->apisourcereplica_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source replica. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcereplica_list**
> list[SourceReplica] apisourcereplica_list(name=name, search=search, ordering=ordering)



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
api_instance = progdbclient.ApisourcereplicaApi(progdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apisourcereplica_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcereplicaApi->apisourcereplica_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[SourceReplica]**](SourceReplica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcereplica_partial_update**
> SourceReplica apisourcereplica_partial_update(id, data)



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
api_instance = progdbclient.ApisourcereplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source replica.
data = progdbclient.SourceReplica() # SourceReplica | 

try:
    api_response = api_instance.apisourcereplica_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcereplicaApi->apisourcereplica_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source replica. | 
 **data** | [**SourceReplica**](SourceReplica.md)|  | 

### Return type

[**SourceReplica**](SourceReplica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcereplica_read**
> SourceReplica apisourcereplica_read(id)



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
api_instance = progdbclient.ApisourcereplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source replica.

try:
    api_response = api_instance.apisourcereplica_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcereplicaApi->apisourcereplica_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source replica. | 

### Return type

[**SourceReplica**](SourceReplica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apisourcereplica_update**
> SourceReplica apisourcereplica_update(id, data)



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
api_instance = progdbclient.ApisourcereplicaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this source replica.
data = progdbclient.SourceReplica() # SourceReplica | 

try:
    api_response = api_instance.apisourcereplica_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisourcereplicaApi->apisourcereplica_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source replica. | 
 **data** | [**SourceReplica**](SourceReplica.md)|  | 

### Return type

[**SourceReplica**](SourceReplica.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


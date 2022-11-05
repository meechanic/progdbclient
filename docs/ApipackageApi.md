# progdbclient.ApipackageApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apipackage_create**](ApipackageApi.md#apipackage_create) | **POST** /apipackage/ | 
[**apipackage_delete**](ApipackageApi.md#apipackage_delete) | **DELETE** /apipackage/{id}/ | 
[**apipackage_list**](ApipackageApi.md#apipackage_list) | **GET** /apipackage/ | 
[**apipackage_partial_update**](ApipackageApi.md#apipackage_partial_update) | **PATCH** /apipackage/{id}/ | 
[**apipackage_read**](ApipackageApi.md#apipackage_read) | **GET** /apipackage/{id}/ | 
[**apipackage_update**](ApipackageApi.md#apipackage_update) | **PUT** /apipackage/{id}/ | 


# **apipackage_create**
> Package apipackage_create(data)



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
api_instance = progdbclient.ApipackageApi(progdbclient.ApiClient(configuration))
data = progdbclient.Package() # Package | 

try:
    api_response = api_instance.apipackage_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackageApi->apipackage_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackage_delete**
> apipackage_delete(id)



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
api_instance = progdbclient.ApipackageApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.

try:
    api_instance.apipackage_delete(id)
except ApiException as e:
    print("Exception when calling ApipackageApi->apipackage_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackage_list**
> list[Package] apipackage_list(name=name, search=search, ordering=ordering)



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
api_instance = progdbclient.ApipackageApi(progdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apipackage_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackageApi->apipackage_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Package]**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackage_partial_update**
> Package apipackage_partial_update(id, data)



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
api_instance = progdbclient.ApipackageApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.
data = progdbclient.Package() # Package | 

try:
    api_response = api_instance.apipackage_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackageApi->apipackage_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackage_read**
> Package apipackage_read(id)



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
api_instance = progdbclient.ApipackageApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.

try:
    api_response = api_instance.apipackage_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackageApi->apipackage_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackage_update**
> Package apipackage_update(id, data)



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
api_instance = progdbclient.ApipackageApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.
data = progdbclient.Package() # Package | 

try:
    api_response = api_instance.apipackage_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackageApi->apipackage_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


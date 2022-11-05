# progdbclient.ApimoduleApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apimodule_create**](ApimoduleApi.md#apimodule_create) | **POST** /apimodule/ | 
[**apimodule_delete**](ApimoduleApi.md#apimodule_delete) | **DELETE** /apimodule/{id}/ | 
[**apimodule_list**](ApimoduleApi.md#apimodule_list) | **GET** /apimodule/ | 
[**apimodule_partial_update**](ApimoduleApi.md#apimodule_partial_update) | **PATCH** /apimodule/{id}/ | 
[**apimodule_read**](ApimoduleApi.md#apimodule_read) | **GET** /apimodule/{id}/ | 
[**apimodule_update**](ApimoduleApi.md#apimodule_update) | **PUT** /apimodule/{id}/ | 


# **apimodule_create**
> Module apimodule_create(data)



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
api_instance = progdbclient.ApimoduleApi(progdbclient.ApiClient(configuration))
data = progdbclient.Module() # Module | 

try:
    api_response = api_instance.apimodule_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApimoduleApi->apimodule_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Module**](Module.md)|  | 

### Return type

[**Module**](Module.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apimodule_delete**
> apimodule_delete(id)



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
api_instance = progdbclient.ApimoduleApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this module.

try:
    api_instance.apimodule_delete(id)
except ApiException as e:
    print("Exception when calling ApimoduleApi->apimodule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this module. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apimodule_list**
> list[Module] apimodule_list(name=name, search=search, ordering=ordering)



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
api_instance = progdbclient.ApimoduleApi(progdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apimodule_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApimoduleApi->apimodule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Module]**](Module.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apimodule_partial_update**
> Module apimodule_partial_update(id, data)



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
api_instance = progdbclient.ApimoduleApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this module.
data = progdbclient.Module() # Module | 

try:
    api_response = api_instance.apimodule_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApimoduleApi->apimodule_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this module. | 
 **data** | [**Module**](Module.md)|  | 

### Return type

[**Module**](Module.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apimodule_read**
> Module apimodule_read(id)



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
api_instance = progdbclient.ApimoduleApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this module.

try:
    api_response = api_instance.apimodule_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApimoduleApi->apimodule_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this module. | 

### Return type

[**Module**](Module.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apimodule_update**
> Module apimodule_update(id, data)



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
api_instance = progdbclient.ApimoduleApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this module.
data = progdbclient.Module() # Module | 

try:
    api_response = api_instance.apimodule_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApimoduleApi->apimodule_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this module. | 
 **data** | [**Module**](Module.md)|  | 

### Return type

[**Module**](Module.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


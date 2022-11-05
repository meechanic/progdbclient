# progdbclient.ApifsobjectApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apifsobject_create**](ApifsobjectApi.md#apifsobject_create) | **POST** /apifsobject/ | 
[**apifsobject_delete**](ApifsobjectApi.md#apifsobject_delete) | **DELETE** /apifsobject/{id}/ | 
[**apifsobject_list**](ApifsobjectApi.md#apifsobject_list) | **GET** /apifsobject/ | 
[**apifsobject_partial_update**](ApifsobjectApi.md#apifsobject_partial_update) | **PATCH** /apifsobject/{id}/ | 
[**apifsobject_read**](ApifsobjectApi.md#apifsobject_read) | **GET** /apifsobject/{id}/ | 
[**apifsobject_update**](ApifsobjectApi.md#apifsobject_update) | **PUT** /apifsobject/{id}/ | 


# **apifsobject_create**
> FSObject apifsobject_create(data)



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
api_instance = progdbclient.ApifsobjectApi(progdbclient.ApiClient(configuration))
data = progdbclient.FSObject() # FSObject | 

try:
    api_response = api_instance.apifsobject_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApifsobjectApi->apifsobject_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FSObject**](FSObject.md)|  | 

### Return type

[**FSObject**](FSObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apifsobject_delete**
> apifsobject_delete(id)



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
api_instance = progdbclient.ApifsobjectApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fs object.

try:
    api_instance.apifsobject_delete(id)
except ApiException as e:
    print("Exception when calling ApifsobjectApi->apifsobject_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fs object. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apifsobject_list**
> list[FSObject] apifsobject_list(name=name, search=search, ordering=ordering)



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
api_instance = progdbclient.ApifsobjectApi(progdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apifsobject_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApifsobjectApi->apifsobject_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[FSObject]**](FSObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apifsobject_partial_update**
> FSObject apifsobject_partial_update(id, data)



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
api_instance = progdbclient.ApifsobjectApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fs object.
data = progdbclient.FSObject() # FSObject | 

try:
    api_response = api_instance.apifsobject_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApifsobjectApi->apifsobject_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fs object. | 
 **data** | [**FSObject**](FSObject.md)|  | 

### Return type

[**FSObject**](FSObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apifsobject_read**
> FSObject apifsobject_read(id)



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
api_instance = progdbclient.ApifsobjectApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fs object.

try:
    api_response = api_instance.apifsobject_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApifsobjectApi->apifsobject_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fs object. | 

### Return type

[**FSObject**](FSObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apifsobject_update**
> FSObject apifsobject_update(id, data)



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
api_instance = progdbclient.ApifsobjectApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this fs object.
data = progdbclient.FSObject() # FSObject | 

try:
    api_response = api_instance.apifsobject_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApifsobjectApi->apifsobject_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this fs object. | 
 **data** | [**FSObject**](FSObject.md)|  | 

### Return type

[**FSObject**](FSObject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


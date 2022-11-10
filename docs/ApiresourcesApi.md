# progdbclient.ApiresourcesApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiresources_create**](ApiresourcesApi.md#apiresources_create) | **POST** /apiresources/ | 
[**apiresources_delete**](ApiresourcesApi.md#apiresources_delete) | **DELETE** /apiresources/{id}/ | 
[**apiresources_list**](ApiresourcesApi.md#apiresources_list) | **GET** /apiresources/ | 
[**apiresources_partial_update**](ApiresourcesApi.md#apiresources_partial_update) | **PATCH** /apiresources/{id}/ | 
[**apiresources_read**](ApiresourcesApi.md#apiresources_read) | **GET** /apiresources/{id}/ | 
[**apiresources_update**](ApiresourcesApi.md#apiresources_update) | **PUT** /apiresources/{id}/ | 


# **apiresources_create**
> Resource apiresources_create(data)



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
api_instance = progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))
data = progdbclient.Resource() # Resource | 

try:
    api_response = api_instance.apiresources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiresourcesApi->apiresources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Resource**](Resource.md)|  | 

### Return type

[**Resource**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiresources_delete**
> apiresources_delete(id)



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
api_instance = progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.

try:
    api_instance.apiresources_delete(id)
except ApiException as e:
    print("Exception when calling ApiresourcesApi->apiresources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiresources_list**
> list[Resource] apiresources_list(text=text, search=search, ordering=ordering)



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
api_instance = progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))
text = 'text_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apiresources_list(text=text, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiresourcesApi->apiresources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Resource]**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiresources_partial_update**
> Resource apiresources_partial_update(id, data)



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
api_instance = progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.
data = progdbclient.Resource() # Resource | 

try:
    api_response = api_instance.apiresources_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiresourcesApi->apiresources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 
 **data** | [**Resource**](Resource.md)|  | 

### Return type

[**Resource**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiresources_read**
> Resource apiresources_read(id)



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
api_instance = progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.

try:
    api_response = api_instance.apiresources_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiresourcesApi->apiresources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 

### Return type

[**Resource**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiresources_update**
> Resource apiresources_update(id, data)



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
api_instance = progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.
data = progdbclient.Resource() # Resource | 

try:
    api_response = api_instance.apiresources_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiresourcesApi->apiresources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 
 **data** | [**Resource**](Resource.md)|  | 

### Return type

[**Resource**](Resource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# progdbclient.ApipackagetagsApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apipackagetags_create**](ApipackagetagsApi.md#apipackagetags_create) | **POST** /apipackagetags/ | 
[**apipackagetags_delete**](ApipackagetagsApi.md#apipackagetags_delete) | **DELETE** /apipackagetags/{id}/ | 
[**apipackagetags_list**](ApipackagetagsApi.md#apipackagetags_list) | **GET** /apipackagetags/ | 
[**apipackagetags_partial_update**](ApipackagetagsApi.md#apipackagetags_partial_update) | **PATCH** /apipackagetags/{id}/ | 
[**apipackagetags_read**](ApipackagetagsApi.md#apipackagetags_read) | **GET** /apipackagetags/{id}/ | 
[**apipackagetags_update**](ApipackagetagsApi.md#apipackagetags_update) | **PUT** /apipackagetags/{id}/ | 


# **apipackagetags_create**
> PackageTag apipackagetags_create(data)



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
api_instance = progdbclient.ApipackagetagsApi(progdbclient.ApiClient(configuration))
data = progdbclient.PackageTag() # PackageTag | 

try:
    api_response = api_instance.apipackagetags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackagetagsApi->apipackagetags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PackageTag**](PackageTag.md)|  | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackagetags_delete**
> apipackagetags_delete(id)



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
api_instance = progdbclient.ApipackagetagsApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.

try:
    api_instance.apipackagetags_delete(id)
except ApiException as e:
    print("Exception when calling ApipackagetagsApi->apipackagetags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackagetags_list**
> list[PackageTag] apipackagetags_list(key=key, value=value, search=search, ordering=ordering)



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
api_instance = progdbclient.ApipackagetagsApi(progdbclient.ApiClient(configuration))
key = 'key_example' # str |  (optional)
value = 'value_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apipackagetags_list(key=key, value=value, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackagetagsApi->apipackagetags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[PackageTag]**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackagetags_partial_update**
> PackageTag apipackagetags_partial_update(id, data)



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
api_instance = progdbclient.ApipackagetagsApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.
data = progdbclient.PackageTag() # PackageTag | 

try:
    api_response = api_instance.apipackagetags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackagetagsApi->apipackagetags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 
 **data** | [**PackageTag**](PackageTag.md)|  | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackagetags_read**
> PackageTag apipackagetags_read(id)



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
api_instance = progdbclient.ApipackagetagsApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.

try:
    api_response = api_instance.apipackagetags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackagetagsApi->apipackagetags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apipackagetags_update**
> PackageTag apipackagetags_update(id, data)



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
api_instance = progdbclient.ApipackagetagsApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.
data = progdbclient.PackageTag() # PackageTag | 

try:
    api_response = api_instance.apipackagetags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApipackagetagsApi->apipackagetags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 
 **data** | [**PackageTag**](PackageTag.md)|  | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# progdbclient.ApirepilcaApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apirepilca_create**](ApirepilcaApi.md#apirepilca_create) | **POST** /apirepilca/ | 
[**apirepilca_delete**](ApirepilcaApi.md#apirepilca_delete) | **DELETE** /apirepilca/{id}/ | 
[**apirepilca_list**](ApirepilcaApi.md#apirepilca_list) | **GET** /apirepilca/ | 
[**apirepilca_partial_update**](ApirepilcaApi.md#apirepilca_partial_update) | **PATCH** /apirepilca/{id}/ | 
[**apirepilca_read**](ApirepilcaApi.md#apirepilca_read) | **GET** /apirepilca/{id}/ | 
[**apirepilca_update**](ApirepilcaApi.md#apirepilca_update) | **PUT** /apirepilca/{id}/ | 


# **apirepilca_create**
> Replica apirepilca_create(data)



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
api_instance = progdbclient.ApirepilcaApi(progdbclient.ApiClient(configuration))
data = progdbclient.Replica() # Replica | 

try:
    api_response = api_instance.apirepilca_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApirepilcaApi->apirepilca_create: %s\n" % e)
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

# **apirepilca_delete**
> apirepilca_delete(id)



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
api_instance = progdbclient.ApirepilcaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.

try:
    api_instance.apirepilca_delete(id)
except ApiException as e:
    print("Exception when calling ApirepilcaApi->apirepilca_delete: %s\n" % e)
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

# **apirepilca_list**
> list[Replica] apirepilca_list(name=name, search=search, ordering=ordering)



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
api_instance = progdbclient.ApirepilcaApi(progdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.apirepilca_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApirepilcaApi->apirepilca_list: %s\n" % e)
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

# **apirepilca_partial_update**
> Replica apirepilca_partial_update(id, data)



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
api_instance = progdbclient.ApirepilcaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.
data = progdbclient.Replica() # Replica | 

try:
    api_response = api_instance.apirepilca_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApirepilcaApi->apirepilca_partial_update: %s\n" % e)
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

# **apirepilca_read**
> Replica apirepilca_read(id)



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
api_instance = progdbclient.ApirepilcaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.

try:
    api_response = api_instance.apirepilca_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApirepilcaApi->apirepilca_read: %s\n" % e)
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

# **apirepilca_update**
> Replica apirepilca_update(id, data)



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
api_instance = progdbclient.ApirepilcaApi(progdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this replica.
data = progdbclient.Replica() # Replica | 

try:
    api_response = api_instance.apirepilca_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApirepilcaApi->apirepilca_update: %s\n" % e)
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


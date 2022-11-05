# progdbclient.ApiTokenAuthApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_token_auth_create**](ApiTokenAuthApi.md#api_token_auth_create) | **POST** /api-token-auth/ | 


# **api_token_auth_create**
> AuthToken api_token_auth_create(data)





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
api_instance = progdbclient.ApiTokenAuthApi(progdbclient.ApiClient(configuration))
data = progdbclient.AuthToken() # AuthToken | 

try:
    api_response = api_instance.api_token_auth_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenAuthApi->api_token_auth_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AuthToken**](AuthToken.md)|  | 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


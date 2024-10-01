# Events
(*events*)

## Overview

REST APIs for capturing event data

### Available Operations

* [get_workspace_events_by_target](#get_workspace_events_by_target) - Load recent events for a particular workspace
* [get_workspace_targets](#get_workspace_targets) - Load targets for a particular workspace
* [post_workspace_events](#post_workspace_events) - Post events for a specific workspace
* [search_workspace_events](#search_workspace_events) - Search events for a particular workspace by any field

## get_workspace_events_by_target

Load recent events for a particular workspace

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.events.get_workspace_events_by_target(request={
    "target_id": "<id>",
})

if res.cli_event_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetWorkspaceEventsByTargetRequest](../../models/operations/getworkspaceeventsbytargetrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetWorkspaceEventsByTargetResponse](../../models/operations/getworkspaceeventsbytargetresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## get_workspace_targets

Load targets for a particular workspace

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.events.get_workspace_targets(request={})

if res.target_sdk_list is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetWorkspaceTargetsRequest](../../models/operations/getworkspacetargetsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetWorkspaceTargetsResponse](../../models/operations/getworkspacetargetsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## post_workspace_events

Sends an array of events to be stored for a particular workspace.

### Example Usage

```python
import dateutil.parser
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.events.post_workspace_events(request={
    "request_body": [
        {
            "created_at": dateutil.parser.isoparse("2024-05-07T12:35:47.500Z"),
            "execution_id": "<id>",
            "id": "<id>",
            "interaction_type": shared.InteractionType.TARGET_GENERATE,
            "local_started_at": dateutil.parser.isoparse("2024-11-03T15:10:38.542Z"),
            "speakeasy_api_key_name": "<value>",
            "speakeasy_version": "<value>",
            "success": False,
            "workspace_id": "<id>",
        },
        {
            "created_at": dateutil.parser.isoparse("2022-04-21T15:59:29.505Z"),
            "execution_id": "<id>",
            "id": "<id>",
            "interaction_type": shared.InteractionType.AUTHENTICATE,
            "local_started_at": dateutil.parser.isoparse("2022-07-17T16:15:35.191Z"),
            "speakeasy_api_key_name": "<value>",
            "speakeasy_version": "<value>",
            "success": True,
            "workspace_id": "<id>",
        },
        {
            "created_at": dateutil.parser.isoparse("2024-08-21T17:10:30.376Z"),
            "execution_id": "<id>",
            "id": "<id>",
            "interaction_type": shared.InteractionType.CONFIGURE,
            "local_started_at": dateutil.parser.isoparse("2022-06-08T00:19:02.158Z"),
            "speakeasy_api_key_name": "<value>",
            "speakeasy_version": "<value>",
            "success": True,
            "workspace_id": "<id>",
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostWorkspaceEventsRequest](../../models/operations/postworkspaceeventsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PostWorkspaceEventsResponse](../../models/operations/postworkspaceeventsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## search_workspace_events

Search events for a particular workspace by any field

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.events.search_workspace_events(request={})

if res.cli_event_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.SearchWorkspaceEventsRequest](../../models/operations/searchworkspaceeventsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.SearchWorkspaceEventsResponse](../../models/operations/searchworkspaceeventsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |
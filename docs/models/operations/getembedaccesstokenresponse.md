# GetEmbedAccessTokenResponse


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `content_type`                                                                               | *str*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `embed_access_token_response`                                                                | [Optional[shared.EmbedAccessTokenResponse]](../../models/shared/embedaccesstokenresponse.md) | :heavy_minus_sign:                                                                           | OK                                                                                           |
| `error`                                                                                      | [Optional[shared.Error]](../../models/shared/error.md)                                       | :heavy_minus_sign:                                                                           | Default error response                                                                       |
| `status_code`                                                                                | *int*                                                                                        | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `raw_response`                                                                               | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)        | :heavy_minus_sign:                                                                           | N/A                                                                                          |
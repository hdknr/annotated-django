## オーダーリファレンス状態の取得 get_order_reference_details

リクエスト:

~~~json
{
  "amazon_order_reference_id": "S03-1571525-4435073",
  "mws_auth_token": "amzn.mws.xxxxxxxx-4b78-a0ce-bddb-f079df560fa4"
}
~~~

レスポンス:

~~~json
{
  "GetOrderReferenceDetailsResponse": {
    "GetOrderReferenceDetailsResult": {
      "OrderReferenceDetails": {
        "OrderReferenceStatus": {
          "State": "Draft"
        },
        "Destination": {
          "DestinationType": "Physical",
          "PhysicalDestination": {
            "StateOrRegion": "東京都",
            "CountryCode": "JP",
            "PostalCode": "1500001"
          }
        },
        "ExpirationTimestamp": "2018-08-16T15:19:06.399Z",
        "IdList": null,
        "Constraints": {
          "Constraint": {
            "ConstraintID": "AmountNotSet",
            "Description": "The seller has not set the amount for the Order Reference."
          }
        },
        "SellerOrderAttributes": null,
        "ReleaseEnvironment": "Sandbox",
        "AmazonOrderReferenceId": "S03-1571525-4435073",
        "CreationTimestamp": "2018-02-17T15:19:06.399Z",
        "RequestPaymentAuthorization": "false"
      }
    },
    "ResponseMetadata": {
      "RequestId": "6905b8dd-2dc3-4e5d-8137-3518c2643d6a"
    }
  }
}

~~~

## 注文内容の設定 set_detail

リクエスト:

~~~json
{
  "amazon_order_reference_id": "S03-1571525-4435073",
  "order_total": "13800",
  "seller_note": null,
  "seller_order_id": "180206-140000-0000",
  "store_name": "ictact",
  "custom_information": null
}
~~~

レスポンス:

~~~json
{
  "SetOrderReferenceDetailsResponse": {
    "SetOrderReferenceDetailsResult": {
      "OrderReferenceDetails": {
        "OrderReferenceStatus": {
          "State": "Draft"
        },
        "Destination": {
          "DestinationType": "Physical",
          "PhysicalDestination": {
            "StateOrRegion": "東京都",
            "CountryCode": "JP",
            "PostalCode": "1500001"
          }
        },
        "ExpirationTimestamp": "2018-08-16T15:19:06.399Z",
        "SellerOrderAttributes": {
          "StoreName": "ictact",
          "SellerOrderId": "180206-140000-0000"
        },
        "OrderTotal": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "ReleaseEnvironment": "Sandbox",
        "AmazonOrderReferenceId": "S03-1571525-4435073",
        "CreationTimestamp": "2018-02-17T15:19:06.399Z",
        "RequestPaymentAuthorization": "false"
      }
    },
    "ResponseMetadata": {
      "RequestId": "68af00cf-c180-48d7-b4c2-3871f510ba85"
    }
  }
}

~~~

## 再取得 : get_order_reference_details

リクエスト:

~~~json
{
  "amazon_order_reference_id": "S03-1571525-4435073",
  "mws_auth_token": "amzn.mws.xxxxxxxx-4b78-a0ce-bddb-f079df560fa4"
}
~~~

レスポンス:

~~~json
{
  "GetOrderReferenceDetailsResponse": {
    "GetOrderReferenceDetailsResult": {
      "OrderReferenceDetails": {
        "OrderReferenceStatus": {
          "State": "Draft"
        },
        "Destination": {
          "DestinationType": "Physical",
          "PhysicalDestination": {
            "StateOrRegion": "東京都",
            "CountryCode": "JP",
            "PostalCode": "1500001"
          }
        },
        "ExpirationTimestamp": "2018-08-16T15:19:06.399Z",
        "IdList": null,
        "SellerOrderAttributes": {
          "StoreName": "ictact",
          "SellerOrderId": "180206-140000-0000"
        },
        "OrderTotal": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "ReleaseEnvironment": "Sandbox",
        "AmazonOrderReferenceId": "S03-1571525-4435073",
        "CreationTimestamp": "2018-02-17T15:19:06.399Z",
        "RequestPaymentAuthorization": "false"
      }
    },
    "ResponseMetadata": {
      "RequestId": "076ecde9-4959-4bdb-945f-eb7cefac0a22"
    }
  }
}

~~~

## 確認送信: confirm


リクエスト:

~~~json
{
  "amazon_order_reference_id": "S03-1571525-4435073"
}
~~~

レスポンス:

~~~json
{
  "ConfirmOrderReferenceResponse": {
    "ConfirmOrderReferenceResult": null,
    "ResponseMetadata": {
      "RequestId": "6a0de7bc-1b06-43bb-b232-c1617ba8693e"
    }
  }
}
~~~

## 状態取得 : get_order_reference_details

リクエスト:

~~~json
{                                       
  "amazon_order_reference_id": "S03-1571525-4435073",
  "mws_auth_token": "amzn.mws.xxxxxxxx-4b78-a0ce-bddb-f079df560fa4"              
}

~~~

レスポンス:

~~~json
{
  "GetOrderReferenceDetailsResponse": {
    "GetOrderReferenceDetailsResult": {
      "OrderReferenceDetails": {
        "OrderReferenceStatus": {
          "LastUpdateTimestamp": "2018-02-17T15:19:15.599Z",
          "State": "Open"
        },
        "Destination": {
          "DestinationType": "Physical",
          "PhysicalDestination": {
            "StateOrRegion": "東京都",
            "Phone": "03-3333-4444",
            "CountryCode": "JP",
            "PostalCode": "1500001",
            "Name": "吉田一郎",
            "AddressLine1": "渋谷区神宮前2-2-2"
          }
        },
        "ExpirationTimestamp": "2018-08-16T15:19:06.399Z",
        "IdList": null,
        "SellerOrderAttributes": {
          "StoreName": "ictact",
          "SellerOrderId": "180206-140000-0000"
        },
        "OrderTotal": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "Buyer": {
          "Name": "吉田一郎",
          "Email": "gmail+sandbox@gmail.com"
        },
        "ReleaseEnvironment": "Sandbox",
        "AmazonOrderReferenceId": "S03-1571525-4435073",
        "CreationTimestamp": "2018-02-17T15:19:06.399Z",
        "RequestPaymentAuthorization": "false"
      }
    },
    "ResponseMetadata": {
      "RequestId": "d015df48-4dd9-4c09-8517-9b906a021f11"
    }
  }
}
~~~

## オーソリ authorize

リクエスト:

~~~json
{
  "amazon_order_reference_id": "S03-1571525-4435073",
  "authorization_reference_id": "A-1-180206-140000-0000-a333d",
  "authorization_amount": "13800.00",
  "seller_authorization_note": null,
  "transaction_timeout": 0,
  "capture_now": false
}
~~~

レスポンス:

~~~json
{
  "AuthorizeResponse": {
    "AuthorizeResult": {
      "AuthorizationDetails": {
        "AuthorizationAmount": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "CapturedAmount": {
          "CurrencyCode": "JPY",
          "Amount": "0"
        },
        "ExpirationTimestamp": "2018-03-19T15:19:18.544Z",
        "IdList": null,
        "SoftDecline": "false",
        "AuthorizationStatus": {
          "LastUpdateTimestamp": "2018-02-17T15:19:18.544Z",
          "State": "Open"
        },
        "AuthorizationFee": {
          "CurrencyCode": "JPY",
          "Amount": "0.00"
        },
        "CaptureNow": "false",
        "SellerAuthorizationNote": null,
        "CreationTimestamp": "2018-02-17T15:19:18.544Z",
        "AmazonAuthorizationId": "S03-1571525-4435073-A061901",
        "AuthorizationReferenceId": "A-1-180206-140000-0000-a333d"
      }
    },
    "ResponseMetadata": {
      "RequestId": "53cf7525-2f10-4b4c-a7c1-20e19744e3ce"
    }
  }
}
~~~

## オーソリ状態取得 get_authorization_details

リクエスト:

~~~json
{
  "amazon_authorization_id": "S03-1571525-4435073-A061901"
}
~~~

レスポンス:

~~~json

{
  "GetAuthorizationDetailsResponse": {
    "GetAuthorizationDetailsResult": {
      "AuthorizationDetails": {
        "AuthorizationAmount": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "CapturedAmount": {
          "CurrencyCode": "JPY",
          "Amount": "0"
        },
        "ExpirationTimestamp": "2018-03-19T15:19:18.544Z",
        "IdList": null,
        "SoftDecline": "false",
        "AuthorizationStatus": {
          "LastUpdateTimestamp": "2018-02-17T15:19:18.544Z",
          "State": "Open"
        },
        "AuthorizationFee": {
          "CurrencyCode": "JPY",
          "Amount": "0.00"
        },
        "CaptureNow": "false",
        "SellerAuthorizationNote": null,
        "CreationTimestamp": "2018-02-17T15:19:18.544Z",
        "AmazonAuthorizationId": "S03-1571525-4435073-A061901",
        "AuthorizationReferenceId": "A-1-180206-140000-0000-a333d"
      }
    },
    "ResponseMetadata": {
      "RequestId": "26d482f3-5c97-470d-86d5-fe3dde8c83f1"
    }
  }
}
~~~

## キャプチャー capture

リクエスト:

~~~json

{
  "amazon_authorization_id": "S03-1571525-4435073-A061901",
  "capture_reference_id": "C-26-180206-140000-0000-1b264",
  "capture_amount": "13800.00"
}

~~~

レスポンス:

~~~json

{
  "CaptureResponse": {
    "CaptureResult": {
      "CaptureDetails": {
        "CaptureReferenceId": "C-26-180206-140000-0000-1b264",
        "CaptureFee": {
          "CurrencyCode": "JPY",
          "Amount": "0.00"
        },
        "SoftDescriptor": "AMZ*旅食",
        "IdList": null,
        "CaptureAmount": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "AmazonCaptureId": "S03-1571525-4435073-C061901",
        "CreationTimestamp": "2018-02-17T15:30:41.081Z",
        "CaptureStatus": {
          "LastUpdateTimestamp": "2018-02-17T15:30:41.081Z",
          "State": "Completed"
        },
        "SellerCaptureNote": null,
        "RefundedAmount": {
          "CurrencyCode": "JPY",
          "Amount": "0"
        }
      }
    },
    "ResponseMetadata": {
      "RequestId": "303a71a2-590c-4ead-8959-14aa8e9a57b3"
    }
  }
}
~~~

## オーソリ状態再取得 get_authorization_details


リクエスト:

~~~json
{
  "amazon_authorization_id": "S03-1571525-4435073-A061901"
}
~~~

レスポンス:

~~~json

{
  "GetAuthorizationDetailsResponse": {
    "GetAuthorizationDetailsResult": {
      "AuthorizationDetails": {
        "AuthorizationAmount": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "CapturedAmount": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "ExpirationTimestamp": "2018-03-19T15:19:18.544Z",
        "IdList": {
          "member": "S03-1571525-4435073-C061901"
        },
        "SoftDecline": "false",
        "AuthorizationStatus": {
          "LastUpdateTimestamp": "2018-02-17T15:30:42.541Z",
          "ReasonCode": "MaxCapturesProcessed",
          "State": "Closed"
        },
        "AuthorizationFee": {
          "CurrencyCode": "JPY",
          "Amount": "0.00"
        },
        "CaptureNow": "false",
        "SellerAuthorizationNote": null,
        "CreationTimestamp": "2018-02-17T15:19:18.544Z",
        "AmazonAuthorizationId": "S03-1571525-4435073-A061901",
        "AuthorizationReferenceId": "A-1-180206-140000-0000-a333d"
      }
    },
    "ResponseMetadata": {
      "RequestId": "61970dc8-1234-4c2e-96bb-78ea8e800818"
    }
  }
}

~~~

## オーダー状態取得 get_order_reference_details

リクエスト

~~~json
{                                                                                
  "amazon_order_reference_id": "S03-1571525-4435073",
  "mws_auth_token": "amzn.mws.xxxxxxxx-4b78-a0ce-bddb-f079df560fa4"
}       
~~~

レスポンス

~~~json
{                                                                                
  "GetOrderReferenceDetailsResponse": {
    "GetOrderReferenceDetailsResult": {
      "OrderReferenceDetails": {
        "OrderReferenceStatus": {
          "LastUpdateTimestamp": "2018-02-17T15:19:15.599Z",
          "State": "Open"
        },
        "Destination": {
          "DestinationType": "Physical",
          "PhysicalDestination": {
            "StateOrRegion": "東京都",
            "Phone": "03-3333-4444",
            "CountryCode": "JP",
            "PostalCode": "1500001",
            "Name": "吉田一郎",
            "AddressLine1": "渋谷区神宮前2-2-2"
          }
        },
        "ExpirationTimestamp": "2018-08-16T15:19:06.399Z",
        "IdList": {
          "member": "S03-1571525-4435073-A061901"
        },
        "SellerOrderAttributes": {
          "StoreName": "ictact",
          "SellerOrderId": "180206-140000-0000"
        },
        "OrderTotal": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "Buyer": {
          "Name": "吉田一郎",
          "Email": "gmail+sandbox@gmail.com"
        },
        "ReleaseEnvironment": "Sandbox",
        "AmazonOrderReferenceId": "S03-1571525-4435073",
        "CreationTimestamp": "2018-02-17T15:19:06.399Z",
        "RequestPaymentAuthorization": "false"
      }
    },
    "ResponseMetadata": {
      "RequestId": "8b208219-d2ae-4bb0-8688-494c437b9e2d"
    }
  }
}

~~~

## 完了 close_order_reference


~~~json
{
  "amazon_order_reference_id": "S03-1571525-4435073",
  "closure_reason": "close",
  "merchant_id": "A9FVERUG2LKDK",
  "mws_auth_token": "amzn.mws.xxxxxxxx-4b78-a0ce-bddb-f079df560fa4"
}
~~~

~~~json

{
  "CloseOrderReferenceResponse": {
    "CloseOrderReferenceResult": null,
    "ResponseMetadata": {
      "RequestId": "2d6ab9e6-c7af-4036-a1ed-040703fc04e6"
    }
  }
}

~~~

## 最終状態取得 get_order_reference_details

リクエスト:

~~~json
{                                       
  "amazon_order_reference_id": "S03-1571525-4435073",
  "mws_auth_token": "amzn.mws.xxxxxxxx-4b78-a0ce-bddb-f079df560fa4"              
}        
~~~

レスポンス:

~~~json
{                                       
  "GetOrderReferenceDetailsResponse": {
    "GetOrderReferenceDetailsResult": {                                          
      "OrderReferenceDetails": {
        "OrderReferenceStatus": {
          "ReasonDescription": "close",
          "LastUpdateTimestamp": "2018-02-17T15:35:27.392Z",
          "ReasonCode": "SellerClosed",
          "State": "Closed"
        },
        "Destination": {
          "DestinationType": "Physical",
          "PhysicalDestination": {
            "StateOrRegion": "東京都",
            "Phone": "03-3333-4444",
            "CountryCode": "JP",
            "PostalCode": "1500001",
            "Name": "吉田一郎",
            "AddressLine1": "渋谷区神宮前2-2-2"
          }
        },
        "ExpirationTimestamp": "2018-08-16T15:19:06.399Z",
        "IdList": {
          "member": "S03-1571525-4435073-A061901"
        },
        "SellerOrderAttributes": {
          "StoreName": "ictact",
          "SellerOrderId": "180206-140000-0000"
        },
        "OrderTotal": {
          "CurrencyCode": "JPY",
          "Amount": "13800.00"
        },
        "Buyer": {
          "Name": "吉田一郎",
          "Email": "gmail+sandbox@gmail.com"
        },
        "ReleaseEnvironment": "Sandbox",
        "AmazonOrderReferenceId": "S03-1571525-4435073",
        "CreationTimestamp": "2018-02-17T15:19:06.399Z",
        "RequestPaymentAuthorization": "false"
      }
    },
    "ResponseMetadata": {
      "RequestId": "0a15ade8-415e-48e2-8a2d-573e8b4b921c"
    }
  }
}
~~~

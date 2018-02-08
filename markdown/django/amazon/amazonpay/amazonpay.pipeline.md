## パイプライン(例)

### User Checkout

- begin ( [Pay with Amazon](https://pay.amazon.com/jp/developer/documentation/lpwa/201952050) )
- address ([AddressBook widget](https://pay.amazon.com/jp/developer/documentation/lpwa/201952070) / create Order Reference entity and [GetOrderReferenceDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201751970))
- payment ([Wallet widget](https://pay.amazon.com/jp/developer/documentation/lpwa/201952070)  /[GetOrderReferenceDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201751970) / [SetOrderReferenceDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201751960) )
- confirm([ConfirmOrderReference](https://pay.amazon.com/jp/developer/documentation/apireference/201751980), [GetOrderReferenceDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201751970))
- authorize([Authorize](https://pay.amazon.com/jp/developer/documentation/apireference/201752010), redirect)
- complete ( [GetAuthorizationDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201752030))

### Admin Regular

- capture ([Capture](https://pay.amazon.com/jp/developer/documentation/lpwa/201953080), [GetCaptureDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201752060))
- close ([CloseOrderReference](https://pay.amazon.com/jp/developer/documentation/apireference/201752000),[GetOrderReferenceDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201751970))

### Admin Irregular

- auth/cancel ([CloseAuthorization](https://pay.amazon.com/jp/developer/documentation/apireference/201752070), [GetAuthorizationDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201752030))
- refund([Refund](https://pay.amazon.com/jp/developer/documentation/apireference/201752080), [GetRefundDetails](https://pay.amazon.com/jp/developer/documentation/apireference/201752100) )
- order/cancel ([CloseOrderReference](https://pay.amazon.com/jp/developer/documentation/apireference/201752000))

### System

- status ([GetServiceStatus](https://pay.amazon.com/jp/developer/documentation/apireference/201752110))

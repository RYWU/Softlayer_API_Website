### SoftLayer\_Account::getHardware
#### 用途: 取得 Bare Metal 機器的資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 'topLevelLocation'

| 使用到的 Properties | 對應到右方的欄位 | objectMask |
| ------------- |:-------------:|:-------------:|
| fullyQualifiedDomainName | Device Name | - |
| primaryIpAddress | Public IP | - |
| topLevelLocation | Location | topLevelLocation |

***

### SoftLayer\_Account::getHourlyVirtualGuests
#### 用途: 取得 Virtual Server (Hourly計費) 機器的資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| fullyQualifiedDomainName | Device Name |
| primaryIpAddress | Public IP | 

***

### SoftLayer\_Account::getMonthlyVirtualGuests
#### 用途: 取得 Virtual Server (Monthly計費) 的機器資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 

| 使用到的 Properties | 對應到右方的欄位 | 
| ------------- |:-------------:|
| fullyQualifiedDomainName | Device Name |
| primaryIpAddress | Public IP | 

***

### SoftLayer\_Virtual\_Gurests::getServerRoom
#### 用途: 取得 Virtual Server 的 地點資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 'pathString'

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| pathString | Location | 

***

### SoftLayer\_Hardware::getBandwidthAllocation
#### 用途: 取得 Baremetal 的 Bandwidth Allocation
#### 參數: SoftLayer-Username, APIKey, Device_Id
#### objectMask: N/A

| 使用到的 Properties | 對應到右方的欄位 | 備註 |
| ------------- |:-------------:|:-------------:|
| N/A | Allocation | 回傳一個型態為字串的數字，隱藏單位為 GB。 (e.g. "5000") |

***

### SoftLayer\_Virtual\_Guest::getBandwidthAllocation
#### 用途: 取得 Virtual Server 的 Bandwidth Allocation
#### 參數: SoftLayer-Username, APIKey, Device_Id
#### objectMask: N/A

| 使用到的 Properties | 對應到右方的欄位 | 備註 |
| ------------- |:-------------:|:-------------:|
| N/A | Allocation | 回傳一個型態為字串的數字，隱藏單位為 GB。 (e.g. "5000") |

註： Hourly 計費的 Virtual Server 的 Bandwidth Allocation 預設皆為 'Pay As You Go'

***


### SoftLayer\_Hardware::getObject
#### 用途: 取得 Baremetal 的 Inbound Bandwith Usage, Outbound Bandwith Usage
#### 參數: SoftLayer-Username, APIKey, Device_Id
#### objectMask: inboundBandwidthUsage, outboundBandwidthUsage

| 使用到的 Properties | 對應到右方的欄位 | 
| ------------- |:-------------:|
| inboundBandwidthUsage | In | 
| outboundBandwidthUsage | Out | 

***

### SoftLayer\_Virtual\_Guest::getObject
#### 用途: 取得 Virtual Server 的 Inbound Bandwith Usage, Outbound Bandwith Usage
#### 參數: SoftLayer-Username, APIKey, Device_Id
#### objectMask: inboundPublicBandwidthUsage,outboundPublicBandwidthUsage

| 使用到的 Properties | 對應到右方的欄位 | 
| ------------- |:-------------:|
| inboundPublicBandwidthUsage | In | 
| outboundPublicBandwidthUsage | Out | 

***


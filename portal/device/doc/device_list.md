### SoftLayer\_Account::getHardware
#### 用途: 取得 Bare Metal 機器的資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 'topLevelLocation'

| 使用到的 Properties | 對應到右方的欄位 | objectMask |
| ------------- |:-------------:|:-------------:|
| fullyQualifiedDomainName | Device Name | - |
| primaryIpAddress | Public IP | - |
| primaryBackendIpAddress | Private IP | - |
| provisionDate | Start Date | - |
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
| primaryBackendIpAddress | Private IP |
| provisionDate | Start Date |

***

### SoftLayer\_Account::getMonthlyVirtualGuests
#### 用途: 取得 Virtual Server (Monthly計費) 的機器資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 'location'

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| fullyQualifiedDomainName | Device Name |
| primaryIpAddress | Public IP | 
| primaryBackendIpAddress | Private IP |
| provisionDate | Start Date | 

***

### SoftLayer\_Virtual\_Gurests::getServerRoom
#### 用途: 取得 Virtual Server 的 地點資訊
#### 參數: SoftLayer-Username, APIKey
#### objectMask: 'pathString'

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| pathString | Location | 

***

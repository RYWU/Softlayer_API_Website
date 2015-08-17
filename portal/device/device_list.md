### SoftLayer_Account::getHardware: 
#### Bare Metal 機器的資訊

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| fullyQualifiedDomainName | Device Name |
| primaryIpAddress | Public IP |
| primaryBackendIpAddress | Private IP |
| provisionDate | Start Date |
| topLevelLocation | Location |
***
### SoftLayer_Account::getHourlyVirtualGuests
#### Virtual Server (Hourly計費) 機器的資訊

| 使用到的 Properties | 對應到右方的欄位 | 備註 |
| ------------- |:-------------:|:-------------:|
| fullyQualifiedDomainName | Device Name | - |
| primaryIpAddress | Public IP | - | 
| primaryBackendIpAddress | Private IP | - |
| provisionDate | Start Date | - |
| location | Location | location 回傳 location id，需要再將 id 轉換為地點|
***
### SoftLayer_Account::getMonthlyVirtualGuests: 
#### Virtual Server (Monthly計費) 機器的資訊

| 使用到的 Properties | 對應到右方的欄位 | 備註 |
| ------------- |:-------------:|:-------------:|
| fullyQualifiedDomainName | Device Name | - |
| primaryIpAddress | Public IP | - |
| primaryBackendIpAddress | Private IP | - |
| provisionDate | Start Date | - |
| location | Location | location 回傳 location id，需要再將 id 轉換為地點|
***
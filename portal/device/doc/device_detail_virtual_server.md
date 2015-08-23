### SoftLayer\_Virtual\_Guest::getObject
#### 用途: 取得 Virtual Server 的 Device Name
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id
#### objectMask: 'location', 'operatingSystem', 'maxMemory', 'operatingSystem.passwords'

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| fullyQualifiedDomainName | Device Name |
| location | Location |
| primaryIpAddress | Public IP |
| primaryBackendIpAddress | Private IP |
| provisionDate | Start Date |
| status.keyName | Status |
| maxMemory | RAM |
| maxCpu | Processor |
| operatingSystem.passwords.username | Username |
| operatingSystem.passwords.password | Password |
| operatingSystem.passwords.modifyDate | Modified Date |

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
|operatingSystem.softwareLicense.softwareDescription.longDescription | OS |

***

### SoftLayer\_Virtual\_Guest::getObject
#### 用途: 取得 Virtual Server 的 Network 的 Status, Speed, Max Speed
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id
#### objectMask: 'primaryNetworkComponent', 'primaryBackendNetworkComponent'

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| status | Network - Status |
| speed | Network - Speed |
| maxSpeed | Network - Max Speed |

註：Public, Private 對應到的 Property

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| primaryNetworkComponent | Public Network Interface |
| primaryBackendNetworkComponent | Private Network Interface |

***

### SoftLayer\_Network\_Subnet\_IpAddress::getByIpAddress
#### 用途: 取得 Virtual Server 的 Network 的 Default Gateway
#### 參數: SoftLayer\_Username, API\_Key, IP\_Address

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| subnet.gateway | Default Gateway |

***

### SoftLayer\_Network\_Subnet\_IpAddress::getByIpAddress
#### 用途: 取得 Virtual Server 的 Network 的 Subnet Mask
#### 參數: SoftLayer\_Username, API\_Key, IP\_Address

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| subnet.netmask | Subnet Mask |

***


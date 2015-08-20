### SoftLayer_Hardware::getObject
#### 用途: 取得 Bare Metal 的 Device Name
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id
#### objectMask: 'topLevelLocation'


| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| fullyQualifiedDomainName | Device Name |
| topLevelLocation | Location |
| primaryIpAddress | Public IP |
| primaryBackendIpAddress | Private IP |
| provisionDate | Start Date |
| hardwareStatus.status | Status |
| serialNumber | Serial Number |
| manufacturerSerialNumber | MFR Serial Number |

***
### SoftLayer_Hardware::getOperatingSystem
#### 用途: 取得 Baremetal 的 OS
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| softwareLicense.softwareDescription.longDescription | OS |
***
### SoftLayer_Hardware::getMemory
#### 用途: 得 Baremetal 的 Ram
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| hardwareComponentModel.longDescription | RAM |
***
### SoftLayer_Hardware::getProcessors
#### 用途: 取得 Baremetal 的 Processor
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| hardwareComponentModel.longDescription | Processor |
***
### SoftLayer_Hardware::getMotherboard
#### 用途: 取得 Baremetal 的 Mother Board
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| hardwareComponentModel.longDescription | Mother Board |
***
### SoftLayer_Hardware::getPowerSupply
#### 用途: 取得 Baremetal 的 Power Supply
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| hardwareComponentModel.longDescription | Power Supply |
***
### SoftLayer_Hardware::getDriveControllers
#### 用途: 取得 Baremetal 的 Drive Control
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| hardwareComponentModel.longDescription | Drive Control |
***
### SoftLayer_Account::getHardware
#### 用途: 取得 Baremetal 的 IP Address
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id

| 使用到的 Properties | 對應到右方的欄位 | 備註 |
| ------------- |:-------------:|:-------------:|
| primaryIpAddress | IP Address - Public | SoftLayer_Hardware::getObject 也可以取得 |
| privateIpAddress | IP Address - Private  | SoftLayer_Hardware::getObject 也可以取得 |
| networkManagementIpAddress | IP Address - Management | SoftLayer_Hardware::getObject 也可以取得 |

***
### SoftLayer_Hardware::getObject
#### 用途: 取得 Baremetal 的 Network 的 status, speed, max speed 資訊
#### 參數: SoftLayer\_Username, API\_Key, Device\_id
#### objectMask: primaryNetworkComponent, primaryBackendNetworkComponent, remoteManagementComponent

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| status | Network - Status |
| speed | Network - Speed |
| maxSpeed | Network - Max Speed |
註：Public, Private, Management 對應到的 Property

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| primaryNetworkComponent | Public Network Interface |
| primaryBackendNetworkComponent | Private Network Interface |
| remoteManagementComponent | Management Network Interface |

***
### SoftLayer_Hardware::getObject
#### 用途: 取得 Baremetal 的 Network 的 status, speed, max speed 資訊
#### 參數: SoftLayer\_Username, API\_Key, Device\_id
#### objectMask: primaryNetworkComponent, primaryBackendNetworkComponent, remoteManagementComponent

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| status | Network - Status |
| speed | Network - Speed |
| maxSpeed | Network - Max Speed |
註：Public, Private, Management 對應到的 Property

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| primaryNetworkComponent | Public Network Interface |
| primaryBackendNetworkComponent | Private Network Interface |
| remoteManagementComponent | Management Network Interface |
***
### SoftLayer\_Network\_Subnet\_IpAddress::getByIpAddress
#### 用途: 取得 Baremetal 的 Network 的 Default Gateway
#### 參數: SoftLayer\_Username, API\_Key, IP\_Address

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| subnet.gateway | Default Gateway |
***
### SoftLayer\_Network\_Subnet\_IpAddress::getByIpAddress
#### 用途: 取得 Baremetal 的 Network 的 Subnet Mask
#### 參數: SoftLayer\_Username, API\_Key, IP\_Address

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| subnet.netmask | Subnet Mask |
***

### SoftLayer_Hardware::getRemoteManagementAccounts
#### 用途: 取得 Baremetal 的 登入帳號
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id
#### objectMask: operatingSystem.passwords

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| operatingSystem.passwords.username | Username |
***
### SoftLayer_Hardware::getObject
#### 用途: 取得 Baremetal 的 登入密碼
#### 參數: SoftLayer\_Username, API\_Key, Device\_Id
#### objectMask: operatingSystem.passwords

| 使用到的 Properties | 對應到右方的欄位 |
| ------------- |:-------------:|
| operatingSystem.passwords.password | Password |
***
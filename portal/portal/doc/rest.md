# SoftLayer API 介紹

>SoftLayer 除了提供 RPC-style API 服務，還提供了 RESTful API，只要利用 REST API 就算是使用的程式語言沒有支援 SOAP 或 XML-RPC，只要可以利用 HTTP 協定傳送要求，並可以解譯 XML 或 JSON 格式的資料，就可以透過 SoftLayer API 獲取想要的資訊。
>另外在 SoftLayer Reference 中，SoftLayer API 可以看到 SoftLayer API 所有的 Services ，以及 SoftLayer API 的資料型態。在 Reference 中 SoftLayer 的 Services 通常用 SoftLayer_Account, SoftLayer_Hardware...方式表示，Services 裡面的方法通常用SoftLayer_Account::getOpenTickets,SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber...方式表示。

## 目錄
 1. REST URLs
 2. HTTP Request Type
 3. Passing Method Parameters
 4. Alternate Ways to Set Parameter and Return Formats
 5. Using Object Masks
 6. Using Result Limits
 7. Error Handling
 8. Caveats
 9. Referenced API Components
 10. External Links

### 1. REST URLs 
一個基本的REST request 如下：
```sh
https://[username]:[apiKey]@api.[service.]softlayer.com/rest/v3/[serviceName]/[initializationParameter].[returnDatatype]
```
REST URLs 有下列幾項特性
* 所有的REST request 都必須經由HTTP SSL
* 你可以藉由 API 使用者名稱(username) 以及金鑰(key) 通過HTTP認證
* 在REST request 基本的hostname和folder 有下列兩種方式：
    - api.softlayer.com/rest/v3/
    - api.service.softlayer.com/rest/v3/
* 可以透過 api.service.softlayer.com/rest/v3/ 來存取SoftLayer專用網路上的REST API，這是一個與SoftLayer比較安全的溝通方式
* 在URL後面可以放上想要呼叫的API service，例如:"SoftLayer_Account"或"SoftLayer_Hardware_Server"
* API request 有些會要求要初始化參數(initialization parameter)，可以將參數(parameter id)放在URL後面
* SoftLayer REST API 回傳的格式有兩種，分別是XML以及JSON。可以在URL最後加上".xml"或".json"來設定希望回傳的資料格式

下面利用SoftLayer service中getObject()這個方法來做示範

SoftLayer_Account::getObject並沒有要求初始化參數(initialization parameter)，故它的URL如下:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account.json
```
SoftLayer_Hardware_Server::getObject需要設定想要抓取的server id，假設想要抓取的server id為"1234"，它的URL如下:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234.json
```
在SoftLayer裡還有許多get方法可以快速取得物件的相關特性(relational properties)，例如SoftLayer_Account API service中的getHardware()，它的URL如下:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/getHardware.json
```
想要抓取server網路組成(network components)它的URL如下:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234/getNetworkComponents.json
```
另外可以結合初始化參數(initialization parameter)以及相關特性(relational properites)還抓取特定物件的資料。
例如想要抓取server"1234"裡面id為"5678"物件的網路組成，其URL如下:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234/getNetworkComponents/5678.json
```
接著想要進一步抓取該網路的UplinkComponent，可以利用getUplinkComponent()，它的URL如下:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234/getNetworkComponents/5678/getUplinkComponent.json
```
如果想要抓取特定資料，可以利用物件遮罩(objectMask)，這部分在下面章節會說明。

### 2. HTTP Request Types
##### DELETE
使用 HTTP DELETE request可以替代service中deleteObject() 的方法。
舉例而言，傳送一個HTTP DELETE request URL如下所示，可以將domain record 1234從SoftLayer's DNS servers中移除。
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234.json
```
##### GET
可以利用 HTTP GET requests抓取物件資料，舉例來說，可以利用GTTP GET request抓取id為"1234"的 domain record:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234.json
```
##### POST
使用HTTP POST request可以替代service中createObject()或createObjects()的方法。可以利用POST一個JSON或XML結構，其中裡面有一個元素"parameter"，"parameter"裡包含的參數，為依照API services createObject()方法中所要求之參數。舉例來說，可以藉由HTTP POST request利用下面的資料以及URL在SoftLayer上的DNS server創造一個domain record。
```sh
{
    "parameters" : [
        {
            "name" : "example.org",
            "resourceRecords" : [
                {
                    "type" : "a",
                    "host" : "@",
                    "data" : "127.0.0.1"
                }
            ]
        }
    ]
}
```
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain.json
```
##### PUT
使用HTTP PUT request可以替代service中的editObject()或editObjects()的方法。可以利用PUT一個JSON或XML結構，其中裡面有一個元素"parameter"，"parameter"裡包含的參數，為依照API services editObject()方法中所要求之參數。舉例來說，可以藉由HTTP PUT request利用下面的資料以及URL在SoftLayer上的DNS servers domain 1234下5678那筆資料為為"10.0.0.1"。
```sh
{
    "parameters" : [
        {
            "data" : "10.0.0.1",
        }
    ]
}
```
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234/getResourceRecords/5678.json
```

### 3. 傳送參數 (Passing Method Parameters)
SoftLayer REST API 傳送參數的方法有兩種：

1. 把參數以字串格式放在 URL 裡傳送
2. 使用 POST 方法，以 json 格式來傳送

第一種方法，參數加在的函式後面，並把此 URL 透過 HTTPS 發送，例如我們要把參數 `hardwareID` (232354) 的主機送進 `SoftLayer_Hardware::getObject` 這個函式。可以使用的 URL 有兩種形式：

`1.` `HardwareID` 接在 `SoftLayer_Hardware` 後面，然後接 `getObject`：

```
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware/232354/getObject.json
```

`2.` `getObject` 接在 `SoftLayer_Hardware` 後面，然後接 `getObject`：

```
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware/getObject/232354.json
```

第二種方法，參數會以 json 物件的方式，用 HTTPS POST 方法傳送。例如：要新增一個 Dns Domain Resource Record，可以使用到的服務(Service)，方法(Method)，遮罩(objectMask)如下：

* 服務: SoftLayer_Dns_Domain_ResourceRecord
* 方法: createObjects

範例 json 格式如下：

```
{
  "parameters":
    [
      [
		{"host":"hosta","data":"127.0.0.1","ttl":"900","type":"a","domainId":"1234"}
        ,
        {"host":"hostb","data":"127.0.0.1","ttl":"900","type":"a","domainId":"1234"}
      ]
    ]
}
```


### 4. 使用 HTTP Request Header 來設定參數格式以及回傳格式  (Alternate Ways to Set Parameter and Return Formats)
除了在 URL 最後加上 .json, .xml 來設定回傳格式之外，你也可以在 HTTP request 的 header 裡指定 MIME-type:

例如：指定回傳 JSON 格式，Headers 可以這樣寫：

```
Content-Type:application/json
```

例如：指定回傳 plain-text 格式，Headers 可以這樣寫：

```
Content-Type:text/plain
```

### 5. 使用遮罩 (Object Masks) 篩選回傳物件

遮罩可以幫助你篩選物件的 `Relational & Count Properties` 內容。遮罩是一個接在 URL 後面的字串，每個遮罩之間可以用分號`;`隔開，且遮罩可以是一種關連式的架構，兩個物件之間的關連可以用半型句號`.`隔開。

#### 遮罩在 URL 中有以下三種格式：
1. `objectMask=(YOUR_OBJECT_MASK1);(YOUR_OBJECT_MASK2)`
2. `objectMask=[mask.(YOUR_OBJECT_MASK1);mask.(YOUR_OBJECT_MASK2)]`
3. `objectMask=mask[(YOUR_OBJECT_MASK1);(YOUR_OBJECT_MASK2)]`

##### 範例：取得 Baremetal 主機的作業系統以及網路資訊

例如，欲查詢 Baremetal 主機上的作業系統以及網路資訊，可以使用到的服務(Service)，方法(Method)，遮罩(objectMask)如下：

* 服務: SoftLayer_Hardware
* 方法: getObject
* 遮罩: operatingSystem, networkComponents (兩者都是 `Relational & Count Properties` )

遮罩在 URL 中的格式會長得像這樣： 

```
objectMask=operatingSystem;networkComponents
```
或是：

```
objectMask=[mask.operatingSystem;mask.networkComponents]
```
或是：

```
objectMask=mask[operatingSystem;networkComponents]
```

以第一種格式為例，整理上列的資訊，送出的 URL 格式如下:

```
https://USERNAME:APIKEY@api.softlayer.com/rest/v3/SoftLayer_Hardware/(Hardware_ID_You_Want_To_Query)/getObject.json?objectMask=operatingSystem;networkComponents
```
註：`operatingSystem` 這個遮罩是加在  `getObject.json` 這個是物件上，不是  `SoftLayer_Hardware`.


#### Property and sub-Property 之間透過句號`.`連接 
##### 範例：取得 Baremetal 主機的密碼

例如，欲查詢 Baremetal 主機的密碼，密碼資訊是在 SoftLayer_Hardware 物件下 operatingSystem 這個性質 (property) 底下的再細分出的 passwords 子性質。可以使用到的服務(Service)，方法(Method)，遮罩(objectMask)如下：

* 服務: SoftLayer_Hardware
* 方法: getObject
* 遮罩: operatingSystem.passwords
( `operatingSystem` 是 getObject 回傳物件的 `Relational & Count Properties`;  `passwords` 是 `operatingSystem` 所回傳物件的 `Relational & Count Properties`)

遮罩在 URL 中的格式會長得像這樣：

```
objectMask=operatingSystem.passwords
```

整理上列的資訊，送出的 URL 格式如下:

```
https://USERNAME:APIKEY@api.softlayer.com/rest/v3/SoftLayer_Hardware/(Hardware_ID_You_Want_To_Query)/getObject.json?objectMask=operatingSystem.passwords
```

#### REST API 的 objectMask 篩選器性質
REST API 處理 objectMask 的方式和 SOAP/XML-RPC APIs 有些許差異，REST 的 objectMask 可以作為子性質的篩選器來使用（子性質例如：passwords 是 operatingSystem 的子性質）。在 objectMask 指定子性質後，REST API 篩選器會自動忽略母性質的資料，僅回傳子性質的資料。

##### 範例：查詢帳號下所有 Baremetal 的 id, hostname

欲查詢帳號下所有 Baremetal 主機的 id, hostname，會使用子性質的篩選器`hardware.id`, `hardware.hostname`。完整使用到的服務(Service)，方法(Method)，遮罩(objectMask)如下：

* 服務: SoftLayer_Account
* 方法: getHardware
* 遮罩: hardware.id, hardware.hostname

整理上列的資訊，送出的 URL 格式如下:

```
https://USERNAME:APIKEY@api.softlayer.com/rest/v3/SoftLayer_Account/getHardware.json?objectMask=hardware.id;hardware.hostname
```

回傳的物件僅只有子性質 `id`, `hostname`，沒有母性質 `hardware` 的資料：

```
{
	"hostname":"ag-esx51-1",
	"id":232354
}
```

### 6. Using Result Limits

在這部分會說明有時候SoftLayer API會回傳太多資料，可以依照需求在URL後面加上resultLimit來限制回傳的資料量，設定resultLimit需利用逗號將兩個數字分開，兩個數字分別設定:
* 要傳回資料的起始位置
* 限制回傳回來資料的數量

下面利用SoftLayer_Account::getOpenTickets來做範例，下面的URL只會回傳這個帳號最前面兩個 open Tickets:
```sh
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/getOpenTickets.json?resultLimit=0,2
```

### 7. 錯誤處理 (Error Handling)

當使用的 API 錯誤時，會回傳錯誤訊息，SoftLayer REST API 回傳 XML/JSON 格式的錯誤訊息。例如以下這個 HTTP Request： 

```
https://username:apiKey@api.softlayer.com/rest/v3/Nonexistent.xml
```

這個 API call 會回傳的錯誤訊息如下：

```xml
<root>
   <error>Service does not exist</error>
</root>
```

### 8. 警告 (Caveats)

#### 指定複雜的資料型態

關於 `XML-PRC`，REST API 不能決定複雜的資料型態。在這樣的情況下，使用者可以在`complex`參數下自定義一個 `complexType`。

### 9. 本文件使用到的 API 功能介紹 (Referenced API Components)

* [SoftLayer_Hardware](http://sldn.softlayer.com/reference/services/SoftLayer_Hardware "Softlayer Baremetal 資訊"): Baremetal 主機資訊的服務 (service)
* [SoftLayer_Hardware:getObject](http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/getObject ""): 取得 Baremetal 主機資訊的方法 (method)

### 10. 參考資料 (External Links)

* [IRC/#SoftLayer](http://https://webchat.freenode.net/ "Softlayer channel on IRC")

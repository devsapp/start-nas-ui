# start-nas-ui 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-nas-ui&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-nas-ui" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-nas-ui&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-nas-ui" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-nas-ui&type=packageDownload">
  </a>
</p>

<description>

> ***通过函数计算快速部署一个如Windows 可视化的能浏览、编辑、上传和下载NAS中的文件的应用***

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |  硬盘挂载 |  VPC |  其它 |     
| --- |  --- |   --- |   --- |   --- |   
| 权限/策略 | AliyunFCFullAccess |  AliyunNASFullAccess |  AliyunVPCReadOnlyAccess |  AliyunECSFullAccess |     


</table>

<codepre id="codepre">

# 代码 & 预览

- [:smiley_cat: 源代码](https://github.com/devsapp/start-nas-ui/tree/main/src)

        

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-nas-ui) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-nas-ui)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init start-nas-ui -d start-nas-ui`   
    - 进入项目，并进行项目部署：`cd start-nas-ui && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

本项目是将世界上最好用的 UI FileManager 项目部署到阿里云 Serverless 平台（函数计算 FC）。
通过 Serverless Devs 开发者工具，您只需要几步，就可以体验 Serverless 架构，带来的降本提效的技术红利。

通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-nas-ui) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-nas-ui)  该应用

![](https://img.alicdn.com/imgextra/i3/O1CN01FKvi6D1KrQmUy2L80_!!6000000001217-2-tps-1465-982.png)

> 函数计算各region可用区请参考: [https://help.aliyun.com/document_detail/72959.html](https://help.aliyun.com/document_detail/72959.html)

部署完成之后，您可以看到系统返回给您的案例地址，例如：
![图片alt](https://img.alicdn.com/imgextra/i1/O1CN01FbMHNY1PvcSGTBzmB_!!6000000001903-2-tps-2520-920.png)

1. 部署成功后， 打开 domain url 地址，按照安装指引完整安装（数据库配置选择 PDO），就得到一个 web 版 windows 用户体验的文件管理系统。
 ![](https://img.alicdn.com/imgextra/i2/O1CN01KkJoBE1PbT2w3zmxb_!!6000000001859-2-tps-1034-832.png)
2. 快捷进入 NAS 根目录管理
  ![](https://img.alicdn.com/imgextra/i1/O1CN013QtzXr1HCGK5I5qh7_!!6000000000721-2-tps-1280-712.png)
3. 其他 Tips:
   - 进入管理页面后，可以点击左上角的 kod 图标从管理页面返回首页。
   - 如果升级提醒，一般建议直接忽视。
   - 一个 NAS 盘最好对应一个新的函数计算服务， 不要部署多个应用对应不同的 NAS 盘但是 SeerviceName 是一样的

**添加 OSS Bucket 管理**
![](https://img.alicdn.com/imgextra/i2/O1CN01e6dygX1znDLioRfQe_!!6000000006758-2-tps-1210-756.png)

> 在本地使用该项目时，不仅可以部署，还可以进行更多的操作，例如查看日志，查看指标，进行多种模式的调试等，这些操作详情可以参考[函数计算组件命令文档](https://github.com/devsapp/fc#%E6%96%87%E6%A1%A3%E7%9B%B8%E5%85%B3) ;

#### 费用详情
1. 函数计算计算资源每个月都有40万 GB-秒 免费额度
    > 如果是操作 NAS 文件相关，每个月的免费额度一般够用。没有操作即没有函数调用不会产生计算资源消耗，即使的页面一直开着
2. 函数计算请求响应流量为 0.5元/GB。
    > 上传文件属于入流量，不计费， 只有下载文件和应用本身网页(占比很小)消耗流量。

#### 注意事项
1. 项目默认部署了一个 keep-warm 函数，如果您想优化冷启动体验（冷启动大约 10s-20s），可以打开定时触发器启用， 会增加一点计算资源消耗。
    ![](https://img.alicdn.com/imgextra/i2/O1CN01LzMzc71te9qJtBaMf_!!6000000005926-2-tps-1741-392.png)
2. 项目Yaml中，声明了`actions`，并且将 Web UI FileManager 工程上传到 NAS，执行函数的时候， nginx 配置 `root /mnt/nas/.fc-nas-filemgr;` 指定了 web 的目录在 NAS 上。
3. 该示例中默认使用 sqlite 数据库 (位于 NAS)。
4. NAS 挂载点的交换机最好在 FC 的可用区， 或者在对应的 VPC 里面新增一个 FC 支持的可用区的交换机。

<details>
<summary>函数计算支持的可用区</summary>

| **地域** | **地域ID** | **函数计算支持的可用区** |
| --- | --- | --- |
| 华东1（杭州） | cn-hangzhou | cn-hangzhou-f、cn-hangzhou-g、cn-hangzhou-h |
| 华东2（上海） | cn-shanghai | cn-shanghai-b、cn-shanghai-e、cn-shanghai-g、cn-shanghai-f |
| 华北1（青岛） | cn-qingdao | cn-qingdao-c |
| 华北2（北京） | cn-beijing | cn-beijing-h、cn-beijing-c、cn-beijing-e、cn-beijing-f |
| 华北3（张家口） | cn-zhangjiakou | cn-zhangjiakou-b、cn-zhangjiakou-a |
| 华北5（呼和浩特） | cn-huhehaote | cn-huhehaote-a、cn-huhehaote-b |
| 华南1（深圳） | cn-shenzhen | cn-shenzhen-e、cn-shenzhen-d |
| 西南1（成都） | cn-chengdu | cn-chengdu-a、 cn-chengdu-b |
| 中国香港 | cn-hongkong | cn-hongkong-c |
| 新加坡 | ap-southeast-1 | ap-southeast-1a、ap-southeast-1b |
| 澳大利亚（悉尼） | ap-southeast-2 | ap-southeast-2a、ap-southeast-2b |
| 马来西亚（吉隆坡） | ap-southeast-3 | ap-southeast-3a |
| 印度尼西亚（雅加达） | ap-southeast-5 | ap-southeast-5a、ap-southeast-5b |
| 日本（东京） | ap-northeast-1 | ap-northeast-1b、ap-northeast-1a |
| 英国（伦敦） | eu-west-1 | eu-west-1a |
| 德国（法兰克福） | eu-central-1 | eu-central-a、eu-central-1a、eu-central-1b |
| 美国（硅谷） | us-west-1 | us-west-1a、us-west-1b |
| 美国（弗吉尼亚） | us-east-1 | us-east-1b、us-east-1a |
| 印度（孟买） | ap-south-1 | ap-south-1a、ap-south-1b |
</details>

[文档详情](https://help.aliyun.com/document_detail/72959.html)

## 参考
使用开源的 UI 文件管理系统: [https://github.com/kalcaddle/kodbox](https://github.com/kalcaddle/kodbox)

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>
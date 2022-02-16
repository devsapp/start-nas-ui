# 阿里云 NAS UI文件管理系统案例

- [阿里云 NAS UI文件管理系统案例](#阿里云-nas-ui文件管理系统案例)
  - [快速体验](#快速体验)
  - [参考](#参考)

## 快速体验

- 初始化项目：`s init start-nas-ui -d start-nas-ui`
- 进入项目后：
  - 将 s.yaml 中对应的 NAS 信息改成成您自己的，如下图:
    - ![](https://img.alicdn.com/imgextra/i4/O1CN01CfRqMv234ZCoI2ZyN_!!6000000007202-2-tps-870-414.png)
  - 执行 `s fc-nas-filemgr nas upload -r code/kodbox /mnt/nas/.fc-nas-filemgr` 将 web 管理工程上传到 NAS
  - 部署：`s deploy`
- 部署过程中可能需要阿里云密钥的支持，部署完成之后会获得到临时域名可供测试
> 浏览器打开域名登录，默认初始化账号和密码是 admin/admin， 您可以登录后， 就得到一个 web 版 windows 用户体验的文件管理系统

![](https://img.alicdn.com/imgextra/i3/O1CN01WRjMv428OKNAu7gjq_!!6000000007922-2-tps-1733-1007.png)

## 参考
使用开源的 UI 文件管理系统: [https://github.com/kalcaddle/kodbox](https://github.com/kalcaddle/kodbox)

---

> - Serverless Devs 项目：https://www.github.com/serverless-devs/serverless-devs
> - Serverless Devs 文档：https://www.github.com/serverless-devs/docs
> - Serverless Devs 钉钉交流群：33947367

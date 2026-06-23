# Cloudflare 给 AI agent 开了个临时账号，让它们能写完代码直接上线，公网可见

**作者**: DracoVibeCoding

**来源**: https://mp.weixin.qq.com/s/7NepTVavn5IhHCTjrqx17A

---

## 摘要

Cloudflare推出“Temporary Accounts”临时账号功能，实现AI时代的“无摩擦力部署”。该功能允许AI Agent无需繁琐的登录授权，即可将生成的网站项目直接部署至Cloudflare并公网可见，极大简化了项目预览与Demo流程。临时部署有效期为60分钟，期间用户可随时申领使其持久化，超时则自动释放，显著提升了AI代码落地的效率。

---

## 正文

DracoVibeCoding DracoVibeCoding

在小说阅读器读本章

去阅读

6月19日，Cloudflare上线了Agent时代又一重磅基建： Cloudflare Temporary Accounts~

> https://blog.cloudflare.com/temporary-accounts/

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGj3Y0XicduIoE449katIohrGuKib3lJibImAvPR81hgLYLRticsrVDjKkVBzmtic0BQLo9r9skIXZLV93sWaOHLaX60ic0vqiaoPiaA5m4/640?from=appmsg)

啥意思？

过去，你想要部署上线一个网站项目需要经过很麻烦的授权验证流程：

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgoZSnXMUA3rn0LoILicvb5tkE3knkJqEtbicTiarB2vbZKjKLpp81vysM7SzcDcvFiamIr6zzOcckgmNtzsCnLCkicoCIcvZG4rgiaU/640?from=appmsg)

而现在，你用Agent写出来的网站项目可以在不需要任何auth(登录)的情况下，通过Cloudflare提供的temporary deployment accounts直接部署到Cloudflare上（60分钟时限），极大程度上方便了网站项目的预览和demo，并且可以在60分钟内可以随时申领该网站使其持久化，否则将会自动释放。

Cloudflare官方blog中把这个过程称为：无摩擦力部署

> 冷知识：
> 
> Cloudflare 通常被认为是世界上最大的 **CDN（Content Delivery Network，内容分发网络）公司之一，同时也是全球最大的网络安全 / DDoS 防护** 服务商之一。
> 
> ✨ **几个关键数据点：**
> 
> •
> 
> 🌏 **网络规模** ：Cloudflare 的网络覆盖全球 330+ 个城市，300+ 个数据中心
> 
> •
> 
> 📊 **流量占比** ：据称处理全球约 20% 的 Web 流量（这个数字公司自己披露，不同来源有差异）
> 
> •
> 
> 🛡️ **安全能力** ：平均每天阻止 1500-2000 亿次网络威胁（含 DDoS 攻击、恶意机器人等）
> 
> •
> 
> ⚡ **核心业务** ：CDN 加速、DDoS 防护、WAF（Web 应用防火墙）、DNS、Workers 边缘计算、Zero Trust 安全等

如何实现Cloudflare temporary deployment？步骤如下：

> 以下采用KIMI Code+K2.7 Code演示

1.

把这篇官方blog文章喂给你的Agent：https://blog.cloudflare.com/temporary-accounts/

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjUHMmhwwhXK9IftD0bStHe5dlPr7lOQHdMyvUJMj6G4XAII0uO0nnuVEW6dmgL2nF3haJGL3QLb9xhickAOdicribM0xs7DFBoh8/640?from=appmsg)

2.

然后让Agent写一个网站项目，并且使用Cloudflare temporary accounts部署上线

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjaol9hC9VO5bguuzKFsHgEQ7SpMKnRPIenazy71miafVhGyYTJic2afUh7sKdIXSONlR9LRWbde3RCVW7AcIicsY7f7NZPXicMtJc/640?from=appmsg)

3.

大概5分钟之后，网站上线！你就可以用来做demo了~ 60分钟内可以把这个链接发给任何人进行浏览~

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjj8VTll8AHDiceaI6qwDyoUtba3ewr6LAGhxXuka5HPbnTXoRNDzOr3uVUZiaQl3j1TiaalLtEpJNSsILdAOKbibKjLLRCtUGNYiac/640?from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_jpg/0m9F5vC1OGhAhl4sGtBFw9OWQQwfdPSgBpDFx6wyxPpXugnV8gfAsurlSXlLrtxTRnKgQjx485x9qvk7aPe3IhMvhiaEH1fpPIpATy1VxHos/640?from=appmsg)

4.

如果你对这个项目，那么你可以点击那个Claim URL：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGj80yr7hSdxj07JTK0DEru4OcQ49DuNx6CddsEzhBwRicj7mcBzeZuuHl3mG7cOWvlwWU5OqXmA2u31icmUx4JB9Zytg6E0hprrg/640?from=appmsg)

5.

在登录Cloudflare之后，会出现一个Claim Accounts的界面（也就是用你的Cloudflare账户来认领这个网页）

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhibvfxKJ66Asgk2gcY7icFp2q78pM5bwWUcSPDgRgpHdrMSkVq7agic7Xrog2tT02Lv5a5mgX3mpB6pFOezwjINvuyJSC8d5Iibbk/640?from=appmsg)

6.

认领成功之后，你的这个网站位于：

> Caring Radium --> Workers & Pages --> Deployments
> 
> 注意：你的名字可能是Caring Radium/Happy Panda/Bright Nebula之类的其他随机名字

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjddZs9umNHlny0Gicic6ghfgSZIUicfGKGJzrV7hN14dur8YccgbOMsTEkt7yyR3Y1Rc0QrZkN4MBmg3WKRmj3gPEjpkhWfueXGI/640?from=appmsg)

7.

如果你想把这个项目挪到你的正式账号（而不是类似于Radium Caring这种随机名字），则需要在项目所在目录内输入下面的命令：

```
npx wrangler login
```
![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgUnE9PJ8POowhtn7Bs6Ta11OHgrWzqpIpIibFBzZubN4iakFWY4zNdhfpka7JXueKbwyOnnePgY1LSabeTSFGyn9TD4icTRPNvwM/640?from=appmsg)

8.

然后点击命令行给出的链接，在浏览器打开Cloudflare的wrangle授权页：

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGh6ic8QPQdOOtlHeMm2sicKCJLBHoZlfDGHcAF0P7VBibUnj9KSWbx4PSAXvDH0UBBlHaudjhupxbtwhHjUz0qIFAlwl5a7HsUwTA/640?from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjEXub82GT2NbGpUkeH2iaBl0KsukGqQkLJcyRct6ODBH5gEu6tYh4t0UP7r1libDaHu2NxZFZed6O7Ek1BwADXlKQAKMKpc0J3I/640?from=appmsg)

9.

点击上面页面的&#x27;Authorize&#x27;后提示授权成功：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjibg5HUTI9TcrxuMEepbEbHViboXIFGsFahb2pGb2lBQ1Sn2vZW8JaA56O0TQlE4b3DcaQAcr57tQCgHcUq2aD2v7Oc6d3ejGh4/640?from=appmsg)

10.

然后在网站项目的目录下输入：

```
npx wrangler deploy
```

> 注意：Agent需要为你准备好wrangler.toml，否则会报错

选择你的正式账号名称：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGgic3jgC1JHvIzz6wxpzDicNx1tMB6uXgLJwEaELBpZ7EMwKZ5QaKhujdP4xRelV46hzjyGsF0T9D1J8YYT1ibsgMYwIIibVEm4jAo/640?from=appmsg)

11.

几秒之后部署成功：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGh2h1OcncJRfCqTxjtg59geexB78WNn2Tx4Bw9dtTEzFZTReRynbouaEibZUs5cEwIicj2ZyQK43eA50dqA9BYXxVnHrjOfYGiaXk/640?from=appmsg)

12.

你就可以在你的Cloudflare正式账号下看到该项目了

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGiaibdYFKIgIDxUaGiapluCJMiajsPE2DW51zNCEhv77icHmXxtlMQ4JyQU5q4uhdmcm9BoGwtdeODd5m2lPQJYibwfmNdW3bGXr776Y/640?from=appmsg)

比如我的这个正式网址就是：

> https://open-design-cloudflare-demo.dracohu2004.workers.dev

13.

你还可以进一步使用你自己的域名来定制该网站：

> 前提条件，你需要在Cloudflare拥有自己的域名

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhIKmDOvTgZ0TXBVsmkrupkXWCVxKoMED7eZDVglFlpwf2hriaeGyBoxqH6M05LhDPqtV5vibLKyUENmPhoiaSMYuFaylp0UiaQ5JA/640?from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjbrYDE4kQIAPTAIpoicBrPW84fHMseaoCic9TXkL3mGIGSIKMSCFLNmeqia9icEyc2VFSVAycyW8QmvNibqiaXzfUicoQx8KpO9snDG8/640?from=appmsg)

14.

最终，你的网站项目就变成了 https://cloudflare-demo.aigc24.com/ 这种非常正式的域名

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhKYGric0KYm5NmQMmZp5l4Zg55xWMLFswsQAZIX6yVAQB4Ricfu7PYyJsCm6ib7FiajAsrRP3Siaibibz0rTFlaUusiaYPicicJecEOxj3E/640?from=appmsg)

---

## 写在最后：

我认为Cloudflare这次提供的Cloudflare Temporary Accounts代表了Agent时代所有互联网基建厂商的一种基础思路，也就是把Agent的开发和部署过程中的各种摩擦力打到0。

大概率阿里云、腾讯云、火山云等国内的云厂商在未来也会陆续跟进。

后面要看Apple、Google、腾讯、手机厂商能否把App、小程序的摩擦力也打下来。

当摩擦力真的为0的时候，就是Agent开发的应用真的成为‘日抛型应用’的阶段；你交付给别人的任何交付物都可以是以应用的形式来承载~ （网站、App、小程序、etc.）

离这一天，可能没有想象中的那么远了。

继续滑动看下一个

Draco正在VibeCoding

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
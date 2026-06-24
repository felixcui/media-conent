# Codex+Hyperframes快速实现NoteBookLM平替

**作者**: DracoVibeCoding

**来源**: https://mp.weixin.qq.com/s/zHvQhtTpucYBtz1nyd62zg

---

## 摘要

本文介绍了如何利用Codex结合Hyperframes快速打造NoteBookLM平替，以提升学习效率。作者强调Codex是强大的全能Agent，通过两步即可将枯燥文字转化为结构化视频：第一步是在Codex中安装Hyperframes插件（也可选用Remotion或Manim等开源框架）生成包含动效的知识讲解视频；第二步是引入Open Design来扩充视频模板。

---

## 正文

DracoVibeCoding DracoVibeCoding

在小说阅读器读本章

去阅读

如果你还没有在用Codex，你可能正在错过目前全球最强大的Agent！

注意，我说的是Agent，而不是Coding Agent！

Codex不仅可以用来Coding，更是学习、工作的超级助手！

后续我会撰写一系列如何使用Codex重构Coding、工作和学习的技巧，敬请期待！

今天是第一篇：如何使用Codex+Hyperframes打造NoteBookLM平替~

---

在学习新的知识概念时，如果只是面对枯燥和非结构化的文字，摩擦力会很大。

如果把学习内容变成结构化、可视化的视频内容，效率会提升很多~

有了Codex，你现在每次只需要5分钟就能轻松生成下面这样的知识讲解类的视频了：

具体步骤如下：

---

### 步骤一：搞定视频生成框架 - Hyperframes

> demo视频中的Slides页面、动效等全部都是通过HeyGen的Hyperframes生成~
> 
> 首先在Codex中搜索并安装Hyperframes插件：

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgYiapw6FiacF84mtjIbWtT3Unfibo1ibJfb0XuW5nBaPRAG43k8jUMGUzRdOK1KQySia6aVo5P48M8NjxqYWHQd9aYUcDV20KaXDdA/640?from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgvQdLRLUtEZfnlolKSO2ydtAgXbN7iacX4GjZ7wy3mx9ocZ8eosq7PkYOdgOEPZ1vp6ykgL9P9EHDya9ma31MtJoeBQFDp95nw/640?from=appmsg)

> 建议你马上让Codex使用 Hyperframes来针对特定知识点生成一条视频来感受一下，可以先搞个1分钟以内的视频，Codex应该3分钟就搞定了~

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgMeMPXuGfgUFW07jCa5J7eY4dlXPOgMykyz0B0AiaDjAzc19htM7rqDvZ70A2pWKic6QDse3fCRNCPBc5d2SxsBiaGMialjksK1jc/640?from=appmsg)

> 当然，Remotion也能实现类似功能~ （不过今天讲解的流程都是通过Hyperframes实现的）

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhxiaS9ibCt8LrvOiaNUOP1SfvKF76cTibWqgV00JXCcAOVWriaRzib808ZltdCbfBAOgLk72unj13mLicvdcuSvKqS1OJGnT90FChuKM/640?from=appmsg)

> 如果你面对的更多是关于数学、物理类的知识内容，你还可以让Codex把Manim也引入进来，坐标、曲线等的动效生成更丝滑！
> 
> 仓库地址：https://github.com/3b1b/manim

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiaKPDLicSPJmrnlibdibsuhFB4YG4zYYPlgpN8hTgUHJtt8WCLBD2dGx8gJQKVSKoUgGvPI6hzg0sH9tZrXKvOz4PO6s38KdTx1P8/640?from=appmsg)

> 不论是Hyperframes还是Remotion，亦或是Manim都是直接用代码来生成视频；强烈建议你多花一些时间了解和使用这些开源框架！这些框架都是开源的，你可以在Codex中使用，也可以在任何用着顺手的Agent中使用！

### 步骤二：扩充模板 - Open Design

> 如果你觉得Hyperframes的模板依然不够丰富，你可以让Codex引入Open Design：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiaoNicVYibsxkh2rKZ49Em36SYIeUNroRbslicHfGpmwHaDWzEJZfrhqGLyc9W5gPyLVibMic56mWoH4nM1HvfCfpgc3udiblbicwnKXk/640?from=appmsg)

> 直接把该仓库的地址（https://github.com/nexu-io/open-design）发给Codex，让它引入即可：

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjHD42uBxiaQTk5zQGL0MTGABxwCAgvqfSAOhO6Z7eBiaD6Nbm2Ow7x3gRIk7YAqpl8NUVPNicfrzVxkKpG87JLicJsMX2nKceGvI0/640?from=appmsg)

> Codex应该会对这个仓库进行提炼，将适合用于生成Hyperframes视频的模板提取到项目文件夹中保存~

### 步骤三：解决背景音乐BGM - MiniMax CLI

> 背景音乐BGM都是通过MiniMax Cli生成，接下来安装MiniMax CLI
> 
> 你可以在对话框中直接向Codex要求安装MiniMax cli （mmx cli）

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGhWuIRSiaicyVJyXLPaNia6Niccfxf01QoEX0n1NrYgwEaQJBqLsFmjtOwodwxDAMzH7xfw2Y4NrrTcLDVaxZ3V0WxE5AgWOYsx7co/640?from=appmsg)

- 然后，你需要一个MiniMax的token plan （支持coding、音乐、TTS语音、视频）- 由于并不打算用MiniMax的token plan来coding（因为已经有Codex了），因此 买最便宜的￥49足够用了！

> Token Plan订阅地址：https://platform.minimaxi.com/subscribe/token-plan?tab=individual

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhPHicDPXnEuEs4P2HwJHfSUIhW14opGOZ9jr1hZOJeUicjZzrbBuSgMJiaHicPwMlUaic1bapicEt0FlWuSnFQIcCQu8av52bjMSrLk/640?from=appmsg)

```
mmx auth login
```

> 注意：国内站是 api.minimax.com，国际站是 api.minimax.io，我之前提供的是国内站购买地址，所以别弄错~

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhu3M5MkTrMJbYOnEmqWaeDMIaL4omiad2k3PZDApOaBlSteRKunDXkNp88T9sxyKD653lToYoWpict8wibiaAXpCibEF333qJCWPA4/640?from=appmsg)

> 在MiniMax网页版登录后确认授权~

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjibYsVc1Jk3OiakpOWFKabnQvOU8eaEDdGgpSScoqcqqXOibzGxJdKdFmdlgymibTuZsm0IQunbHibxxlSwGicXws1o08iaUsQamVq5E/640?from=appmsg)

> 授权成功后返回终端，会显示MMX CLI相关信息和token余量

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGjm43awAMZceq61NvwBCvcvt8Xv9lYibBwKh3bXiaczPUUMIS3jFl1P6pMz3M0oPibG4CMhr72n5Qy6m6QUkyKUico1a0OjR4PqHDE/640?from=appmsg)

> 然后，你可以让Codex确认一下它是否可以使用mmx cli生成音乐：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGgVRj203icXEO2ic9IqSVZPVA4wIZ9kjlgOoia6MVyqvic2g0qExyIptk4UAdsoKlQe3jx72d2jqibbSCPLD1BjKcRjEiaCsbiaCuVHRM/640?from=appmsg)

> OK，到这里，你已经拥有了可以生成视频内容的Hyperframes和生成背景音乐BGM的MiniMax CLI~
> 
> 其实MiniMax CLI也能生成TTS语音，但自然度比较一般，所以我们接下来接入火山引擎的doubao-TTS-2.0，我认为目前自然度和性价比最高的方案~

### 步骤四：接入TTS语音 - 火山引擎 doubao-TTS-2.0

- 首先，你需要有个火山引擎的账号，并且充一点钱

> 然后访问：https://console.volcengine.com/speech/app
> 
> 创建应用并获取App ID（其实使用默认的default项目就行）

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGgM2xKmrFgqJBtUcficD2wfmJibOrX5ZicP7CUFYexMwD20K80ibJOCFZQnJNwdHI5bCPsXjdaw0oMvtkxQbbtzolXUOKaIJYV7VvY/640?from=appmsg)

> 然后访问doubao语音页面：https://console.volcengine.com/speech/service/10035
> 
> 开通语音合成2.0服务

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjYTDh0wsEJWVGVoN51GA0nahIXaDCcicnBWTtarJ1MNRJ3bcbZjHicqz4NSZQHfbeJenPmrAxmfibVyCv7MdvwacDfibUPm3HMHvE/640?from=appmsg)

> 拉到页面底部，把App ID、Access TOKEN、Secret KEY复制出来备用

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiajPAnI3MTE4zZRpcHUtz5qL0THXJQIk5RzGhemFOLiaVggfYMH4qpj6eSEbcAOlMtT9EPYseEMFjgcFb4bP6zqicvXibzjuaVsc4/640?from=appmsg)

> 然后访问：https://console.volcengine.com/speech/new/voices?projectName=default
> 
> 找到自己细化你的音色：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGghE6gFh8nG109OUjSJhNNaJaENz8icf3sM7ohY2RbsBWxn8jBdaFZjsCxJfic0GRSaK7ic0qvxfGaDASwkjxKuz3yiaOrz4yiaQ9jY/640?from=appmsg)

> 遇到喜欢的声音可以把voice ID复制出来备用

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGh8UoTLKLuv5K2K2RjbhZiaVHYHuHAcNC7blqdDoHScpwDNFj5S3icUpjHoCQTfF6vxlwfpibdyJicO6J2CBtMcjvMksEcJG8YLhXw/640?from=appmsg)

> 我比较喜欢的女性声音ID是偏播客/对谈类的：zh\_female\_mizai\_saturn\_bigtts

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiakfkPxgiatJlfYuU7icVFwZZIGN2MicX9cica81JrhXOSv1icf8tspPbyH5Mn8griahLQO28JVubibI35DH9kOpPia2qBaAo1ZkicEia4Lg/640?from=appmsg)

> 然后，请把以上步骤获取的VOLCENGINE\_TTS\_APP\_ID、VOLCENGINE\_TTS\_ACCESS\_TOKEN、VOLCENGINE\_TTS\_VOICE\_TYPE写入项目的.env文件中；
> 
> 此外，还有个恒定值：VOLCENGINE\_TTS\_RESOURCE\_ID="seed-tts-2.0"
> 
> 然后请使用下面的方法，让Codex来调通火山引擎TTS2.0：

---

使用doubao TTS的方法如下，你可以把以下内容直接复制粘贴给你的Agent：

#### 1\. 准备环境变量

```
export VOLCENGINE_TTS_ACCESS_TOKEN="你的 Access Token"
export VOLCENGINE_TTS_APP_ID="你的 App ID"
export VOLCENGINE_TTS_VOICE_TYPE="你的音色 voice_type"
export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-2.0"
```

其中：

- `VOLCENGINE_TTS_ACCESS_TOKEN`
	：接口鉴权 token
- `VOLCENGINE_TTS_APP_ID`
	：火山引擎应用 ID
- `VOLCENGINE_TTS_VOICE_TYPE`
	：要使用的音色 ID
- `VOLCENGINE_TTS_RESOURCE_ID`
	：模型资源 ID，Doubao TTS 2.0 通常为 `seed-tts-2.0`

#### 2\. 请求地址

```
POST https://openspeech.bytedance.com/api/v1/tts
```

请求头：

```
Content-Type: application/json
Authorization: Bearer; <VOLCENGINE_TTS_ACCESS_TOKEN>
```

如果遇到 401 / 403，优先检查：

- token 是否正确或过期
- `Authorization`
	格式是否正确
- appid 与 token 是否匹配
- `resource_id`
	是否已开通权限

#### 3\. 请求体结构

核心 JSON 如下：

```
{
  "app": {
    "appid": "${VOLCENGINE_TTS_APP_ID}",
    "token": "${VOLCENGINE_TTS_ACCESS_TOKEN}",
    "cluster": "volcano_tts"
  },
"user": {
    "uid": "demo-user"
  },
"audio": {
    "voice_type": "${VOLCENGINE_TTS_VOICE_TYPE}",
    "encoding": "mp3",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0,
    "sample_rate": 44100
  },
"request": {
    "reqid": "唯一请求 ID",
    "text": "要合成的文本",
    "operation": "query",
    "with_frontend": 1,
    "frontend_type": "unitTson",
    "resource_id": "${VOLCENGINE_TTS_RESOURCE_ID}"
  }
}
```

注意： `resource_id` 放在 `request` 里，不是 `audio` 里。

#### 4\. curl 调用示例

```
REQ_ID=$(python3 - <<'PY'
import uuid
print(uuid.uuid4())
PY
)

curl -X POST 'https://openspeech.bytedance.com/api/v1/tts'\
  -H 'Content-Type: application/json'\

  -H "Authorization: Bearer; ${VOLCENGINE_TTS_ACCESS_TOKEN}"\

  -d @- <<JSON > response.json

{
  "app": {
    "appid": "${VOLCENGINE_TTS_APP_ID}",
    "token": "${VOLCENGINE_TTS_ACCESS_TOKEN}",
    "cluster": "volcano_tts"
  },
  "user": {
    "uid": "demo-user"
  },
  "audio": {
    "voice_type": "${VOLCENGINE_TTS_VOICE_TYPE}",
    "encoding": "mp3",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0,
    "sample_rate": 44100
  },
  "request": {
    "reqid": "${REQ_ID}",
    "text": "你好，这是火山引擎 TTS 合成测试。",
    "operation": "query",
    "with_frontend": 1,
    "frontend_type": "unitTson",
    "resource_id": "${VOLCENGINE_TTS_RESOURCE_ID}"
  }
}
JSON
```

接口成功时会返回 base64 编码的 MP3 数据。

#### 5\. 返回值处理

成功响应通常类似：

```
{
  "code": 3000,
  "message": "Success",
  "data": "base64-encoded-mp3",
  "reqid": "..."
}
```

把 `data` 解码后写入 MP3 文件：

```
python3 - <<'PY'
import base64, json
from pathlib import Path

result = json.loads(Path('response.json').read_text())
if result.get('code') != 3000 or not result.get('data'):
    raise SystemExit(f"TTS failed: {result}")

Path('demo.mp3').write_bytes(base64.b64decode(result['data']))
print('saved: demo.mp3')
PY
```

#### 6\. Python 完整示例

```
import base64
importos
importuuid
frompathlibimport Path

importrequests

url ="https://openspeech.bytedance.com/api/v1/tts"
access_token = os.environ["VOLCENGINE_TTS_ACCESS_TOKEN"]

payload = {
    "app": {
        "appid": os.environ["VOLCENGINE_TTS_APP_ID"],
        "token": access_token,
        "cluster": "volcano_tts",
    },
    "user": {
        "uid": "demo-user",
    },
    "audio": {
        "voice_type": os.environ["VOLCENGINE_TTS_VOICE_TYPE"],
        "encoding": "mp3",
        "speed_ratio": 1.0,
        "volume_ratio": 1.0,
        "pitch_ratio": 1.0,
        "sample_rate": 44100,
    },
    "request": {
        "reqid": str(uuid.uuid4()),
        "text": "你好，这是火山引擎 TTS 合成测试。",
        "operation": "query",
        "with_frontend": 1,
        "frontend_type": "unitTson",
        "resource_id": os.environ.get("VOLCENGINE_TTS_RESOURCE_ID", "seed-tts-2.0"),
    },
}

resp = requests.post(
    url,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer; {access_token}",
    },
    json=payload,
    timeout=60,
)
resp.raise_for_status()
result = resp.json()

if result.get("code") !=3000ornot result.get("data"):
    raiseRuntimeError(f"TTS failed: {result}")

Path("demo.mp3").write_bytes(base64.b64decode(result["data"]))
print("saved: demo.mp3")
```
再次强调，以上内容是给Codex读的，不需要你自己通读和弄懂！

---

OK，你现在配置好了.env中的环境变量，也有了火山引擎TTS的配置方法，让Codex完成最终的配置

> 注意：配置方法我已经通过飞书文档提前发给了Codex，因此下面的截图没有显示该部分内容~

![image](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGgq3xRSPhjDZkt3GiaCy9CPmRVMucgIWlCW1pVs0NzXQLDAUSWA5xL35h6jZOBicWQXMnUMNQGpibW3tibuuDN7QDHxIPVRYXCYajA/640?from=appmsg)

> 1-2分钟之后，Codex就调通了TTS语音的接口~

---

### 步骤五：搞定封面图 - Codex自带的image\_gen

> 由于Codex在带GPT-Image-2，因此，如果你希望制作的内容在小红书或者视频号上进行传播，那么建议直接让Codex使用image\_gen来搞定封面

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGgbOvbEqLrqRfRn9umpUPNearMtCTXsLkKVticWKdHaPciadib7Fibbr4oehUMfh7xDDR4csNcv8vgu2QP676zBR3HYNXBlicrYiaIicE/640?from=appmsg)

> 当然，如果你用的不是原生Codex没有GPT-Image-2功能也不要紧，你可以让Codex用代码来绘制一张封面，或者进一步接入即梦等国内绘图模型来实现封面的绘制！
> 
> 这些内容就不在本文赘述了~

---

如果你已经走到了这一步，恭喜，你的Codex已经成为了NoteBookLM平替！可以在几分钟内针对任何知识或者材料进行视频化解读了！

当然，这只是个起点，如果你拥有的是原生的Codex + GPT-Image-2的能力，你完全可以进一步实现（用GPT-Image-2生成的图片来代替Hyperframes用代码写出来的页面）类似下面这样视觉冲击力更强的视频甚至播客内容：

---

Echo本文开篇，在最近深度使用Codex的过程中，我似乎窥见了AI Agent时代好的教育应该是一种什么样子~

我会在未来的文章中继续给大家分享我的思考和实践！

敬请期待！

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
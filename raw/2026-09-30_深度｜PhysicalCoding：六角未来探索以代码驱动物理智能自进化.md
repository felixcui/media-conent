# 深度｜Physical Coding：六角未来探索以代码驱动物理智能自进化

**作者**: Z Potentials

**来源**: https://mp.weixin.qq.com/s/hdEosKnnPizqXejekooLQw

---

## 摘要

六角未来提出Physical Coding路线，主张以代码作为物理智能理解世界、组织行动与自我改进的统一语言，通过Code as World显式描述任务状态与约束、Code as Policy组织规划验证与失败恢复，并构建HexaAnything自进化体系，将验证过的执行经验用于训练模型，从而突破VLA与WAM在可检查性与可修正性上的局限。

---

## 正文

Z Potentials Z Potentials

在小说阅读器读本章

去阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/f95SMEAicvFttdkR840dCs89Ngp6vv6p3RnP63CYdM5ucdBj4ia0YWkKicx1Dky5PcM8Dzl28S8gJEHM5SMBwYZI2u57p654vEQwwe9MF56luU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0) ![](https://mmbiz.qpic.cn/mmbiz_png/f95SMEAicvFvHN1xmWqDvvNRf4o2r0zVBjG1TkDiaIa9BIiaIMN5PApp8qg1DSz7xFzW7x1aMzG0Ofb8s1hiaywiahGhicpia7CiaiaocTTIF8UegZuM/640?wx_fmt=png&from=appmsg)

在数字世界里，代码本身就是任务的载体：把任务写成代码，照着代码执行，改进也都写回代码。Coding Agent就是这么干的——自己写程序、调工具、跑测试，把验证过的改动存成可复用的版本；这些成功的轨迹，接着还能拿来训练下一代模型。

想把这套思路搬到物理世界，有个坎得先迈过去：任务走到哪了、搞砸是因为什么，这些都得能查、能改才行。机器人得判断物体位置、任务完成没有、出错后怎么补救，但在原生VLA/WAM的接口里，这些判断全藏在模型内部，从外面看不见，自然也无法检查和修正。

六角未来在技术报告《Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence》里给出了他们的答案，一条以代码为中心的路线，叫Physical Coding：把任务相关的世界状态用代码显式写出来，让代码来组织规划、行动和验证；物理世界的反馈回来后，再据此修改工具和工作流程；最后把验证过的执行经验拿去训练模型。

## 01 VLA与WAM：会预测动作和画面，但并未真正理解真实世界

VLA做的事，大致是把观测和语言指令，直接变成机器人动作。尽管评测时分数高，但不等于它真的听懂了指令且照做了。报告在LIBERO的三组任务里做了对照：训练时把语言指令去掉，QwenGR00T的平均成功率仍有92.3%；保留指令时是96.2%，只差3.9个百分点。也就是说，这类测试里场景和任务往往高度对应，模型未必真理解了指令，更可能是认出场景后，直接复现了和它对应的那套动作。报告还提到，其他相关评测实验发现，一些公开VLA只要稍微换个视角、改一下机器人初始状态，或挪一下物体位置，成功率就会明显下滑。

WAM让模型不只输出动作，还预测接下来画面会怎么变。但以烤箱仿真任务为例，它生成一段烤箱门缓缓关上的视频，画面合理、动作连贯，但无法判断门外的食材究竟有没有全部放进去。其他相关视频模型的研究也在说同一件事：生成得逼真，不等于它真的理解物理上发生了什么。

所以六角未来认为，物理智能缺的不是更多动作、更漂亮的画面，而是一套能查、能改的“任务状态”：任务目标是什么、哪些条件已满足、失败后如何补救，都得变成看得见、改得动的对象。要是这些判断全藏在模型黑盒里，机器人做错时，我们很难分清它是看错了目标、漏了步骤，还是错误地以为任务已经完成，如果不知道错在哪，也就更难把这次纠错，更不要说把这次纠错“举一反三”。

## 02 Physical Coding：以代码理解世界，以行动提升智能

科学认识世界的一条重要路径，是将经验、规律转化为形式化的表达，并在同一表达空间中不断积累、迭代。

**六角未来认为** **，** **代码可以成为智能理解世界、作用于世界并改进自身的统一语言** **，** 为表征世界、组织行动与进化智能自身提供共同的载体。它可以描述对象、状态与约束，也可以把规划、判断和行动组织成可执行的程序。代码本身又是能够被读取、检查和修改的对象，因此，智能体可以分析并改进自己使用的工具与工作流。这构成了工程意义上的“自指”。

六角未来提出的Physical Coding **，** 以两种相互耦合的代码表征为核心：Code as World（代码即世界）用于描述与任务相关的对象、状态、关系、约束与进度；Code as Policy（代码即策略）负责组织规划、工具调用、验证与失败恢复。二者协同运作，Code as World为行动提供当前状态，Code as Policy据此组织行动；行动又带来新的观测，帮助系统更新状态、调整后续步骤。

## 03 HexaAnything：构建自进化体系

## 基于这一思路，六角未来构建了Pyhsical Coding Agent：HexaAnything，模型负责生成和调整Code as World与Code as Policy；Harness负责把它们运行起来，组织观测、记忆、工具调用、验证和恢复。感知、规划与控制工具，以及VLA/WAM等动作模型，都可以接入 Harness，作为工具参与任务执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f95SMEAicvFtaBdSt6hCCmeTzkBF60rmQzHwWj2MCLO4UBpWicpiap0EKqPdJnz3DZWtxzkY0SBCCAJo4GMnZk5YmLq1FBW8IrUicIBDelia3JgI/640?wx_fmt=png&from=appmsg)

**报告讨论了一种“执行—反馈—更新—再执行”的物理自进化机制：一次失败的执行可以用于定位问题，推动工具或流程改进；经过验证的执行经验可以转化为训练数据，支持下一版本模型的学习；候选更新通过独立评估后，再进入下一轮执行，如此形成闭环。在这基础上，报告提出了四个相互耦合的进化对象：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f95SMEAicvFs5Pc7BTlticZibzk5M2n2oNoeQCwI4LMKnwrwKEv3en8y4nrXicSibx0IiaYHLAqyl5VQL3e7VcxNVkmm8QXoUGp2PsKrROaV0eQqg/640?wx_fmt=png&from=appmsg)

**Harness：通过Harness组织任务执行，也记录执行中的轨迹与反馈。这些记录可以帮助定位工具、状态表示、工作流或验证机制中的问题，为修改Harness提供依据。**

**数据与环境：通过筛选和验证的执行记录可以成为训练样本，失败与纠正记录也可以用于构建新的任务和测试场景，扩展系统能够学习和检验的经验。**

**模型与算法：经过验证的数据进一步用于模型训练，能够使执行经验逐步转化为模型自身的能力。更新后的模型再参与任务执行与问题诊断，为下一轮Harness改进提供新的依据。**

**本体与硬件：长期来看，六角未来希望将这一循环与改进进一步延伸到机器人本体与计算硬件，通过执行中暴露出的感知盲区、运动限制或时延问题，调整传感器、执行器、控制接口和计算资源。**

六角未来的判断有两层。一层是表征：在当前架构下，3D与动作表征会破坏掉原有的语言表征，牺牲LLM/VLM原有的理解与推理能力；而代码本身也是语言，用代码写空间状态与动作，不必引入额外表征进入模型。另一层是失败之后的出路：以动作模型为主体时，一次失败只说明数据落在分布之外，要么补示教、要么叠规则，出路都在系统之外；当它只是被调用的工具，失败可以被定位到某个函数或某条判据，改动留在代码里，下一次从改好的版本开始。把VLA/WAM放在工具位置，是因为把它放在主体位置，系统就失去了自己改自己的可能。

## 04 从改进执行到训练模型，这套方法目前走到了哪一步？

围绕Physical Coding，六角未来已在任务执行、模型学习和工具迭代三个方面取得初步进展，并将同一套系统用于仿真科学实验与真实机器人任务，取得一定成效。

- **Harness：显著提升复杂长程任务的执行能力**

HexaAnything的思路是：把任务拆成步骤、记录状态、写清完成条件和失败后的补救办法，串成一条能跑的工作流。智能体每做一步，就回头检查任务进展到哪了，再决定下一步怎么走，VLA作为工具，由系统根据需要调用。

在RoboCasa365上， **由GPT-5.6-Sol驱动的HexaAnything Harness将总体成功率从原生XR-1的56.6%提升至61.1%。其中，Composite-Seen的成功率从54.8% 提升至61.5%，Composite-Unseen从34.3%提升至38.3%。都超过了当前榜单第一。**

装烤肉三明治这种长程任务，成功率直接从17%拉到48%。这些结果至少说明：把理解任务、动手做、验证结果串起来，智能体确实能把复杂长程任务做得更好。

- **Model：执行经验回流训练，迭代模型能力**

六角未来基于Qwen3.8-27B开展后训练，将Harness回流的状态判断样本与执行轨迹纳入训练数据，与通用数据共同用于微调，得到HexaModel v0.1。这些执行轨迹保留了任务如何被拆解、工具如何被调用、结果如何被验证，以及失败后如何恢复的过程，为模型学习规划、工具使用和恢复行为提供了具体样本。

训练完成后，我们将HexaModel放回相同的Harness， **与基座模型进行比较，总体成功率从60.5%提升至61.7%，Composite-Unseen的成功率由37.3%提升至39.5%。**

- **Tool：工具在反馈中实现改进**

在RoboDojo的仿真折衣实验中，六角未来将一项可复用的抓取与放置工具作为改进对象，让HexaAnything读取失败轨迹、定位问题并修改工具代码，再由相同的任务评估器检验新版本，使执行反馈直接参与工具的迭代。

最初的工具将衣物当作刚性物体处理，因尺寸限制拒绝了所有调用。后续修改逐步加入适用于薄层衣料的夹取方式，调整双臂同步动作、手腕姿态和放置高度，使工具能够更好地处理衣物折叠。 **在相同的5个测试种子上，工具版本的成功次数从0/5提升至4/5。**

- **仿真科学实验**

六角未来搭建仿真实验环境PhyBench，设置了弹簧劲度系数、重力加速度和耦合振子的简正模频率三类测量任务。环境提供实验目标、装置与仪器，智能体需要自行设计实验过程，操作装置、收集数据、完成分析，并提交有证据支持的定量结论。

以弹簧实验为例，Code as World记录实验条件与测量结果，Code as Policy组织操作与分析，使每个定量结论都能够追溯到相应的测量记录，整个过程保留在同一个可检查的工作流中。在 HexaAnything 里 **搭配GPT-6-Astra、Opus 5.5等前沿模型，三类实验的平均相对误差均低于5%。**

![](https://mmbiz.qpic.cn/mmbiz_png/f95SMEAicvFsnoGTcxtIdCiaa0Td94rKz88pFxtcGeLdSnyGmLmwKghtv2iacBkwIiceUj1iaiaI9U6FmK4VY4ficfj3DnibtibmRbibHQ9mMv3vTA180/640?wx_fmt=png&from=appmsg)
- **真机实验**

六角未来还搭建了URAI（Universal Robot–Agent Interface），将Harness接入AgileX PiPER-X双臂平台，让人和智能体能够共用同一套机器人操作工具：人通过相机图像上的划线标注指定操作，智能体通过 API 提交相应的像素坐标与参数，二者调用相同的规划与控制代码。

六角未来使用GPT-6-Astra对七项桌面任务进行了三次测试：拧瓶盖、井字棋对弈、将积木放入碗中、热狗装盘、倾倒积木三次均成功，投掷积木、折叠衣物各成功一次。 **与已公开结果相比，部分任务的完成速度提升了2.4–3.5倍，放积木入碗任务的输出Token用量仅为Robocurve的1/4.7。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f95SMEAicvFs4ZRicibyibjicEFmHzvjc3p4Dfh6KfHygIAEZv5YvcYHFAvb2yxsSXdwzjgcYicLkaajic4zMpY9wAIgATIIwKicbViaV3oxwV3BwpeI/640?wx_fmt=png&from=appmsg)

## 05 真实应用驱动智能，让物理世界持续进化

物理智能的持续进化，应当从真实需求出发。数据的价值，在于它所承载的真实问题、环境约束与行动反馈。高质量数据应在解决实际问题的过程中持续积累，而非脱离应用、单纯为训练而“制造”。

就像LLM从互联网文本社区中诞生，Coding Agent则脱胎于代码社区，这些数据都是因为人类活动而自然存在的，LLM、Coding Agent将这部分数据压缩为“智能”，而“Physical Coding”的数据也广泛存在于人类物理世界活动中。工业设计、工艺流程、设备控制、运行与检验记录，都是人为了把生产跑起来而写下的。它们本就是对条件、动作与判定的形式化表达。这部分数据承载的正是“物理智能”，在实际应用中把这部分数据回收，方能实现价值最大化。

应用是最好的Benchmark。智能的价值，需要在持续使用中接受检验：能否降低成本、提升效率，回应不断变化的需求，真正为人类产生价值。应用连接需求、数据、评价与迭代，让能力增长拥有来自现实世界的方向与尺度。

Physical Coding正在探索将这样的迭代路径引入物理世界。当越来越多的物理过程能够被AI通过代码描述、检验与改进，进入持续迭代的将是一个完整的系统：既包括感知、推理与行动的物理智能，也包括承载智能的对应硬件的设计范式，与人类生产活动的交互范式。若能将人类物理活动纳入代码的迭代过程中，将极大加速生产效率，提升生产力水平，使人类物理活动迈向更自然的全新水平。

这也是六角未来希望推动的长期变化：以真实需求牵引应用，以应用积累经验，再以代码将经验转化为可验证、可复用的改进。随着这一路径延伸到更多场景，AI的进步将持续转化为生产与生活中的实际改善，让物理世界具备在使用中学习、在反馈中进化的能力。

References:https://arxiv.org/abs/2609.35432

https://hexafuture.ai/blog/physical-coding

https://github.com/HexaFuture/PhysicalCoding

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f95SMEAicvFuyO9LHuaYyK7eIoUvOTNKbB4kWn4A2PxeHdKAR6z9IYWImqhYFGezWRrsLIiaZyyoZMibIBI2AsgJPeSkhXjHXjcnlXJLTfHQXA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

不喜欢

知道了

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过
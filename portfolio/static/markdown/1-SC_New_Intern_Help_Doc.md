## SC Group Intern Help Doc
Last modified time: Sept. 18th, 2021

### 写在前面 | Intro
Hey，我是靳轶乔，希廷老师2021年的实习生。这里是一些我汇总的信息，从入职到check out，或许有所帮助。注意本文档是中英文混合，因为是来自我不同时期写的文档。

For English readers: I guess this is already post-COVID era when you see this doc. So the policies about VPN and work-from-home must be different. You can try copying & pasting the followings into Google Translate. Please note that this doc is written in Chinese and English interchangeably because it was compiled from multiple source docs I wrote at different times.


### 入职前 ｜ Before you are in
* 了解我们组在做哪些方向，可以关注“微软学术合作”、“微软研究院AI头条”公众号，从历史消息里搜一搜“SC”或者“社会计算组”
    * 可以参考这篇 [SC组之前实习生的介绍](https://mp.weixin.qq.com/s/DYgVtbtzjCtRw3EMMg_cXg) 以及我们的项目,比如 [PENS](https://mp.weixin.qq.com/s/5vFDKPwqUv1qMSQ6lr17yA)、[MIND](https://mp.weixin.qq.com/s/5X25oq4TPezO3u8g5WHCqw)
    * our research is interdisciplinary, so it might help if you have taken CogSci or Linguistics classes before
* 从 [Microsoft Research Lab](https://www.microsoft.com/en-us/research/group/social-computing-beijing/) 的网站了解我们组的 publication
* 问 mentor 要项目相关的paper，从论文的 Related Works 部分顺藤摸瓜，了解所做领域相关的方法。
* 弄一台Windows设备，我当时没有弄，结果struggle了很长时间 ... 直到我弄了一台 ... 如果不想从头装系统，至少要弄个虚拟机。访问内部文件夹方便很多
* 学一些和项目潜在相关的 package，见文末 [Packages](#packages) 
* 关于网课：如果你在做Graph相关，可以简要看看 [CS224W](http://web.stanford.edu/class/cs224w/) ([Link to Bilibili](https://www.bilibili.com/video/BV1RZ4y1c7Co?share_source=copy_web)) ；如果你在做 LM 相关，可看[CS224N](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/index.html#schedule) ([Link to Bilibili](https://www.bilibili.com/video/BV1Eb411H7Pq?share_source=copy_web))；重点在于看一下这些课的 slides，过一遍 basic concepts


### 刚入职 | Day One
* SC 组老师同学们有一个大群，入职当天你的 mentor 会加你进去，你需要提前准备一下你的中文自我介绍；SC 组 intern 也有一个小群
* 关注 MSRA Interns' Family 的群消息，一般遇到什么问题搜一下聊天记录都能有不错的解决方案
* 更新你的 LinkedIn profile
* 办完工牌后可以往工卡里充值，位置就在 Tower 1 的3层，微软桥最南侧
* 从 [GetConnected](https://getconnected.microsoft.com/deviceRegister/) 配置VPN，全称叫 MSFTVPN，这样可以访问内部文件

### 入职后 | When you are in
* 每天 5:00 - 5:30 pm 在 Teams 上的讨论组里发 Daily，汇报当日完成的工作，格式可参考：

```
8.12
Done
    * [Code] 实现完方法v3并完成初步debug
Doing
    * [Paper] 改好论文的算法部分初稿
    * [Paper] 论文 Related Work 补充 Content-based Method
Todo
    * [Paper] 在Gephi中可视化小部分样例
```

* 每周一给 mentor 发 Weekly Report 并 CC 给 Intern Support [msrainte@microsoft.com](msrainte@microsoft.com)，汇报上周完成的工作及本周计划，中英文均可。Weekly Report 可以直接写在邮件里，也可写在 word 里作为附件。格式参考：

```
TITLE: Weekly Report (9.06-9.10) | YOUR_NAME
---------------------------------------------
BODY:
Dear YOUR_MENTOR_NAME & Intern Support team,

Greetings from YOUR_NAME, an intern at MSRA SC Group. 
My weekly report for last week (9.06-9.10) is as follows: 
上周完成的工作
* item 1 
* item 2
* ...

本周计划
* item 1 
* item 2
* ...

Best regards,
YOUR_NAME
```

* SC组的组会一般在周二下午，1个半小时时间，其中1个小时讲，半个小时讨论；具体 Topic 提前一周确定并由谢老师在周一通知大家
* 组会是 FTE 和 intern 轮流讲 paper，预计你入职第2-3个月就会轮上了，做好准备；如果你有事讲不了，提前一周通知 Chaozhuo 老师
* 申请 GCR Sandbox: [Reserve GCR Dev Node](https://dev.azure.com/msresearch/GCR/_wiki/wikis/GCR.wiki/4107/Reserving-a-Linux-Sandbox)， 每个实习生可以拿到一个Windows和一台Linux(带V100或者P100)
  * 连接 Linux 的 GCR 可以通过 [X2Go](https://wiki.x2go.org/doku.php/download:start) 来使用图形界面
  * Windows 的 GCR 可以用 Jumptainer + Remote Desktop 连接
  * GCR 可能会自行重启，请关注下 GCR 相关邮件
  * **GCR 记得及时续期，否则逾期会被立即回收！！**
  * 如果有关于 GCR 的疑问，或者需要重启，可发邮件给 GCRSupport ([gcrsupp@microsoft.com](gcrsupp@microsoft.com))
* **借笔记本**：可以让mentor帮忙申请 [Toybox](http://msratoybox/Mgmt.aspx)。注意 Toybox 要一位 FTE 批准，需要给 ToyboxAdmin ([msratoyboxadmin@microsoft.com](msratoyboxadmin@microsoft.com))MSRA IT Support 发邮件并 CC 给 mentor ，并取得 mentor 的 approval，格式参考：

```
Dear MSRA IT Support,
 
Greetings from YOUR_NAME, an intern at MSRA SC team. 
My mentor is YOUR_MENTOR_NAME. Currently I am working mobile.
 
Just politely asking if I can borrow a device from your office
so that I will be able to work in our office building?
 
Thanks for your help and wish to hear back from you!
 
Best regards,
YOUR_NAME
```

mentor 回复：
```
Sure, please go ahead and borrow a device.
```
* 等收到 IT Support 确认邮件后，去 12230-12238 IT Helpdesk 取设备，大约要等待 1-2 小时装系统；刚借时默认可以借1周，等1周过后可发邮件给 IT Support 续借，如果你是Mobile intern，在公司没有工位，可以续借1个月+。
* 如何在公司外用Mac打开Intern Support的共享文件夹：打开一个Finder，Go -> Connent to Server -> `smb://msralpa/Users/Intern_MUST_Read` -> `v-YOUR_ALIAS+YOUR_PASSWORD`. Note the slashes `/` and the backslashes `\\`
* 预定会议可以用 Overlook
* 绝不要带外部设备进来，除了你的手机。如果带的话需要向 IT Support ([msrait@microsoft.com](msrait@microsoft.com)) 申请。收到确认邮件后去 IT Support 贴 tag。我没有试过，似乎很难批
* 当你 Onsite 并有工位后，可以发邮件找 IT Support 拿工位电脑的 Admin 权限
```
TITLE: Applying Admin privilege for seat YOUR_SEAT_NUMBER | YOUR_NAME
---------------------------------------------
BODY:
Dear MSRA IT Support,

Greetings from YOUR_NAME, an intern at MSRA SC team. 
Shall I obtain the administrator access on my seat? 
This is for installing the X2Go Client and connect to
my Linux GCR Sandbox so that I can work on the projects.

My alias is YOUR_ALIAS and my seat is YOUR_SEAT_NUMBER.
Thanks for your help and wish to hear back from you!

Best regards,
YOUR_NAME

```

### 资源汇总 | Resources
#### 关于写论文 | Writing
* [Turnitin](https://www.turnitin.com/): Plagarism detector. 查重和查语法错误的神器，如果你是留学生的话一定熟悉，收费；官网的订阅价格比较贵，可以从某宝租账号
* [Grammarly](https://app.grammarly.com/): 查语法错误，免费
* [Thesaurus](https://www.thesaurus.com/): 查同近义词
* [Quillbot](https://quillbot.com/): Paraphrasing Tool，可以对英文句子进行同义转述
* [List of Greek letters and math symbols (Overleaf)](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols) 查找论文可用的数学符号

#### 关于论文画图 | Drawing
* [ml-visuals](https://github.com/dair-ai/ml-visuals) by dair-ai. The README of this GitHub repo is linked to a [Google Slide](https://docs.google.com/presentation/d/11mR1nkIR9fbHegFkcFq8z9oDQ5sjv8E3JJp1LfLGKuk/edit?usp=sharing), which contains lots of elements for drawing.

#### 关于会议投稿 | Conference
* [AI Conference Deadlines](https://aideadlin.es/?sub=ML,CV,NLP,RO,SP,DM): 汇总各 ML 会议的Deadline
* [Conference Acceptance Rate](https://github.com/lixin4ever/Conference-Acceptance-Rate): 汇总各会议的接收率

#### 关于搜索论文
* [OpenReview](https://openreview.net/): Find out the ways in which reviewers potentially attack your papers 
* [Google Scholar](https://scholar.google.com/): For literature review
* [DBLP](https://dblp.org/): For literature review


### General Tips 
* If you are from a university outside mainland China, your mentors may appear to be stricter than your college professors or your lab leaders. However, this mentoring style is good for you to make progress. The key is **immediate feedback**
* People here work because of self motivation. I knew many folks who worked onsite through the Spring Festival. So forget the American Pie try not to slack off.
* If you have special arrangements at school, talk to your mentor as early as possible
* MSRA is probably the only place where you can write academic papers as a **corporate intern**. So cherish the opportunities.

### About Paper

#### 读论文 | When you read
* You may want to spend an entire day digesting the first paper in this field (4h+ in reading and 4h+ in note-taking.
* Later spend one or two hours reading each additional paper

#### 方法设计 | Idea Evaluation
* Get some initial experimental results and discuss with your mentor.
* Fill the idea evaluation document or make a slide to illustrate your ideas. You MUST do so unless you have already earned a Ph.D. in public speaking (just kidding ...). It is so hard to paint a big picture of your works before you write them down.
* Get a drawing tool to visualize your ideas. I used GoodNotes for drawing and EverNotes for recording ideas, and send the exported PDFs of those sketches to my mentor before our in-person discussions. 
* DO NOT ALWAYS ask why, because too many questions really hamper the overall productivity of your team. Think before you ask and only ask if you definitely consider your question as valuable and necessary. Gradually you will know WHY. 

#### 写码 | When you code
* Choose a usable baseline. Every application-centric project must have baselines.
* Find a nice template to formulate your code and make your work more human-readable. For example [PyTorch Template](https://github.com/victoresque/pytorch-template.git)
* Use a config file to load & store parameters. This way, you can manage the hyperparameters in a centralized way.
* Use [Tensorboard](https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html) to visualize your model and the training / test results. Both Tensorflow and PyTorch are supported. 
* Start especially early on ANY code related to data processing. You don't know what will happen when you handle those data, such as format errors, network issues, etc. I once made a mistake in my data processing pipeline, and it ruined almost ALL my training data.


#### 写作 | When you write
* Insert a table to record EACH notation you use throughout the paper. This will make your life much easier if your algorithm is complicated and your paper has a lot of potentially conflicting notations 
* DO NOT create new nicknames for already-existing terminology.
* DO NOT mix-use the upper & lowercase alpha of the same letter on different variables (e.g. Using $\mathbf{e}$ for an embedding and then using $E$ for the set of edges in some graph)
* For all terminologies used in your paper, make sure your definition is correct. At the very least, it should agree with the definition given in Wikipedia
* Start early on writing. Set an early deadline for the paper, approximately 1 week before the final deadline. I failed to do so, and struggled & almost ran out of time (and ran out of hair, too ...)
* Don't treat your paper as a technical report. Use formal English.
* Better spend >3 days on the case study. At least you should start early on that and build a demo so that when the deadline is approaching, it won't seem too daunting to handle all at once.
* Before starting on the actual paper, work on a draft (e.g. [DRAFT]AAAI22 YOUR_PAPER_TITLE). You can use it later as a clipboard when you write the actual paper. 

### 交稿前 | Before Deadline
* Download a PDF version of the paper and search for linking errors in the paper which start with "??"

### 交稿后 | After Deadline
* You may want to put your submission on [Arxiv.org](https://arxiv.org/). But remember to ask the conference committee about the policies before you do so.
* Compare the final version of your work (the ones revised by your mentor) with your initial drafts. This is the way to IMPROVE your writing in your future submissions. When I wrote my first draft, I felt like a genius. As my mentor revised the paper, my previous writing really paled and I came to learn how the masters and pros do things.

### 离职前 | Before you Checkout
* Write a nice *README* file for your projects. Start at least one week on this *README* before you check out.
* Take pictures with your mentors & bosses. Highly recommend the *Wall* at the *Sky Garden* (13F) and the *Microsoft Research* sign (13-14F).
* Fill out the *Performance Assessment* and the *Internship Survey*. They can be found in a email like *InternSupport - Intern Exit Notice - YOUR_NAME* from MSRA Intern Support.

## Appendix
### Packages
<span id="packages"></span>
Below is a seemingly daunting list of packages to learn. However, you don't need to master each of them. A better way is to start with some demos on their GitHub pages and their official documentation.

#### 应学 | Packages You Should learn
* [transformers](https://huggingface.co/transformers/quicktour.html)
  * a.k.a. pytorch-pretrained-bert
* [pytorch_geometric](https://pytorch-geometric.readthedocs.io/en/latest/notes/introduction.html) 
  * Deep Learning on Graphs. 用于实现各种 GNN. 你可以直接尝试 [example 目录](https://github.com/pyg-team/pytorch_geometric/tree/master/examples) 下的样例
  * 另一个功能类似的 package 是 Amazon 的 [DGL](https://www.dgl.ai/)

#### 可学 | Packages You Might Want to Learn
* networkx
  * For graph construction. If you work on GNN-related projects, this may be helpful
  * It has helpful functions for graph construction, e.g. `networkx.convert_matrix.from_pandas_edgelist`, which directly constructs a graph from pandas dataframe
  * You can also output *.gexf files from a networkx graph for visualization in **Gephi**
* SpaCy
  * For constituency parser, NER, tagging,
* allennlp
  * The Semantic Role Labeling function is helpful

#### 软件 | Softwares to Learn
* [Gephi](https://gephi.org/): For graph visualization. You may want to chec out this PDF [tutorial](https://gephi.org/tutorials/gephi-tutorial-visualization.pdf). There is a free [Udemy Tutorial](https://www.udemy.com/course/gephi/). I recommend you use Gephi on Windows with [Java 8 SDK](https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=All&field_architecture_target_id=All&field_java_package_target_id=All) installed. 

#### 其他 | Misc
* LEARN **[PEP8](https://www.python.org/dev/peps/pep-0008/)**!! Otherwise you won't be able to understand your own code two months later.


### 写在最后 | Last
When I first got in, I was just a 3rd year college student. I went through periods of [Imposter Syndrome](https://en.wikipedia.org/wiki/Impostor_syndrome) that I've never experienced during my college life. My mentor and my fellow interns really gave me huge support. As said in [this article](https://mp.weixin.qq.com/s/OqfS5TZVMVoJCDpIvXy9ig), MSRA (and especially our group) emphasizes more on your growth and potentials. This is a learning environment meant to nurture future talents in engineering. So cherish your days and enjoy your life here ~
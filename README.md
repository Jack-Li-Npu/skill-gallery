# Skill Gallery

把实际工作中反复用到的方法，整理成可以安装、查看成果、持续改进的 agent skills。

[浏览 Skills](#skills) · [查看作品](examples/open-source-project-article/README.md) · [安装](#安装) · [新增 Skill](CONTRIBUTING.md)

## Skills

| Skill | 用途 | 输入 → 产物 |
| --- | --- | --- |
| [开源项目实测图文](skills/open-source-project-article/SKILL.md) | 体验开源项目，制作面向技术读者的中文文章 | GitHub 地址 → 实测、社区案例、配图、公众号排版稿 |

## 开源项目实测图文

给一个项目地址，先跑官方示例，再找真实使用案例，最终整理成可阅读、可修改的中文图文。

<a href="examples/open-source-project-article/README.md"><img src="examples/open-source-project-article/images/hero.png" alt="Craft Anything 文章作品：把喜欢的网站和软件，做成自己的版本" width="900"></a>

**[查看作品与验证范围](examples/open-source-project-article/README.md) · [阅读 Skill](skills/open-source-project-article/SKILL.md)**

- **介绍和上手完整。** 概览、部署与开始使用、实战与使用案例、结语；设备要求放在第二部分。
- **结果有依据。** 官方示例优先，社区案例必须检索；分开记录本机实测、他人结果与使用设想。
- **先写内容，再生成图。** 从读者处境、介绍和结果提取视觉简报。正文首图 16:9，封面分别构图为 2.35:1 与 1:1。
- **形成发布产物。** Markdown、图片、英文架构图、三种字体、doocs/md 排版与图文包；保留代码主题、Mac 圆点和复制兼容性检查。

这是工作流指导，依赖代理当前可用的搜索、命令行、浏览器、图像生成和排版工具。仓库没有内置运行环境或一键渲染程序；完整工具要求见 [环境说明](skills/open-source-project-article/references/workspace.md)。

### 使用示例

```text
使用 $open-source-project-article，为这个项目制作中文技术文章：
https://github.com/storytold/craft-anything

面向有技术基础的读者。先运行官方示例，加入有实际结果图片的社区案例。
交付 Markdown、配图、公众号排版稿和两种封面；暂不公开发布。
```

也可以只修改已经写好的文章：

```text
使用 $open-source-project-article，按新的标题修改首图和两张封面。
从现有介绍中提取画面内容，保留正文，并同步更新嵌入图片的 HTML 和图文包。
```

## 安装

在 Codex 中让内置安装器安装指定目录：

```text
使用 $skill-installer，从 https://github.com/Jack-Li-Npu/skill-gallery
安装 skills/open-source-project-article。
```

手动安装时，下载仓库，将整个 `skills/open-source-project-article/` 文件夹复制到代理识别的 skills 目录。Codex 的项目级目录为 `.agents/skills/`，用户级目录为 `~/.agents/skills/`。保留 references 与 agents 子目录；已有同名技能时先比较差异，避免覆盖个人定制。[官方安装与目录说明](https://learn.chatgpt.com/docs/build-skills)

其他支持 `SKILL.md` 的代理可以读取核心指导，`agents/openai.yaml` 是 Codex 界面元数据。当前验证来自 Codex 工作流，未宣称在其他代理上完成兼容性测试。

## 目录

```text
skills/       可独立安装的技能；每个文件夹一个 SKILL.md
examples/     使用请求、实际产物预览与验证范围
catalog.json  统一目录数据，供未来网页筛选与展示使用
docs/         Gallery 展示与维护约定
```

新增技能时先提供一个有实际产物的例子，再加入目录。每项保留输入、输出、依赖、版本和验证状态。分类按任务用途组织，例如内容制作、研究分析、开发工具；有实际技能后再增加分类，不预先摆空栏目。

未来网页可直接读取 `catalog.json`，增加分类筛选、搜索和安装入口；技能正文仍以 `skills/` 为唯一维护来源。[展示设计](docs/gallery-design.md)

## 来源与许可

本仓库原创说明与自有示例资产使用 [MIT](LICENSE)。示例图片中的产品名称不表示该项目认可本仓库。

文章工作流会按需使用 [doocs/md](https://github.com/doocs/md) 与 [Humanizer-CN](https://github.com/AlexBybye/humanizer-CN)，本仓库不复制它们的源码或技能全文；各自许可独立适用。当前公开示例只包含自制插画和本机运行截图，不包含第三方博主图片、私人样文或测试日志。

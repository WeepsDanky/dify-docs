# 集成 Langfuse

### 1 什么是 Langfuse

Langfuse 是一个开源的 LLM 工程平台，可以帮助团队协作调试、分析和迭代他们的应用程序。

{% hint style="info" %}
Langfuse 官网介绍：[https://langfuse.com/](https://langfuse.com/)
{% endhint %}

***

### 2 如何配置 Langfuse

1. 在[官网注册](https://langfuse.com/)并登录 Langfuse
2. 在 Langfuse 内创建项目，登录后在主页点击 **New** ，创建一个自己的项目，**项目**将用于与 Dify 内的**应用**关联进行数据监测。

<figure><img src="../../../.gitbook/assets/image (249).png" alt=""><figcaption><p>在 Langfuse 内创建项目</p></figcaption></figure>

为项目编辑一个名称。

<figure><img src="../../../.gitbook/assets/image (251).png" alt=""><figcaption><p>在 Langfuse 内创建项目</p></figcaption></figure>

3. 创建项目 API 凭据，在项目内左侧边栏中点击 **Settings** 打开设置

<figure><img src="../../../.gitbook/assets/image (253).png" alt=""><figcaption><p>创建一个项目 API 凭据</p></figcaption></figure>

在 Settings 内点击 **Create API Keys** 创建一个项目 API 凭据。

<figure><img src="../../../.gitbook/assets/image (252).png" alt=""><figcaption><p>创建一个项目 API 凭据</p></figcaption></figure>

复制并保存 **Secret Key** ，**Public Key，Host**

<figure><img src="../../../.gitbook/assets/image (254).png" alt=""><figcaption><p>获取 API Key 配置</p></figcaption></figure>

4. 在 Dify 内配置 Langfuse，打开需要监测的应用，在侧边菜单打开**监测**，在页面中选择**配置。**

<figure><img src="../../../.gitbook/assets/image (255).png" alt=""><figcaption><p>配置 Langfuse</p></figcaption></figure>

点击配置后，将在 Langfuse 内创建的 **Secret Key, Public Key, Host** 粘贴到配置内并保存。

<figure><img src="../../../.gitbook/assets/image (256).png" alt=""><figcaption><p>配置 Langfuse</p></figcaption></figure>

成功保存后可以在当前页面查看到状态，显示已启动即正在监测。

<figure><img src="../../../.gitbook/assets/image (257).png" alt=""><figcaption><p>查看配置状态</p></figcaption></figure>

***

### 3 在 Langfuse 内查看监测数据

配置完成后， Dify 内应用的调试或生产数据可以在 Langfuse 查看监测数据。

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption><p>在 Dify 内调试应用</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (258).png" alt=""><figcaption><p>在 Langfuse 内查看应用数据</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption><p>在 Langfuse 内查看应用数据</p></figcaption></figure>

### 4 监测数据清单  

#### Workflow /Chatflow Trace信息
**用于追踪workflow以及chatflow**

| Workflow                            | LangFuse Trace        |
|-------------------------------------|-----------------------|
| workflow_app_log_id/workflow_run_id | id                    |
| user_session_id                     | user_id               |
| workflow_{id}                       | name                  |
| start_time                          | start_time            |
| end_time                            | end_time              |
| inputs                              | input                 |
| outputs                             | output                |
| 模型token消耗相关                         | usage                 |
| metadata                            | metadata              |
| error                               | level                 |
| error                               | status_message        |
| [workflow]                          | tags                  |
| conversation_id/workflow时无          | session_id            |
| conversion_id                       | parent_observation_id |
 
**Workflow Trace Info**
- workflow_id - Workflow的唯一标识
- conversation_id - 对话ID
- workflow_run_id - 此次运行的ID
- tenant_id - 租户ID
- elapsed_time - 此次运行耗时
- status - 运行状态
- version - Workflow版本
- total_tokens - 此次运行使用的token总数
- file_list - 处理的文件列表
- triggered_from - 触发此次运行的来源
- workflow_run_inputs - 此次运行的输入数据
- workflow_run_outputs - 此次运行的输出数据
- error - 此次运行中发生的错误
- query - 运行时使用的查询
- workflow_app_log_id - Workflow应用日志ID
- message_id - 关联的消息ID
- start_time - 运行开始时间
- end_time - 运行结束时间
- workflow node executions - workflow节点运行信息
- Metadata
  - workflow_id - Workflow的唯一标识
  - conversation_id - 对话ID
  - workflow_run_id - 此次运行的ID
  - tenant_id - 租户ID
  - elapsed_time - 此次运行耗时
  - status - 运行状态
  - version - Workflow版本
  - total_tokens - 此次运行使用的token总数
  - file_list - 处理的文件列表
  - triggered_from - 触发来源

#### Message Trace信息
**用于追踪llm对话相关**

| Message                        | LangFuse Generation/Trace |
|--------------------------------|---------------------------|
| message_id                     | id                        |
| user_session_id                | user_id                   |
| message_{id}                   | name                      |
| start_time                     | start_time                |
| end_time                       | end_time                  |
| inputs                         | input                     |
| outputs                        | output                    |
| 模型token消耗相关                    | usage                     |
| metadata                       | metadata                  |
| error                          | level                     |
| error                          | status_message            |
| ["message", conversation_mode] | tags                      |
| conversation_id                | session_id                |
| conversion_id                  | parent_observation_id     |

**Message Trace Info**
- message_id - 消息ID
- message_data - 消息数据
- user_session_id - 用户的session_id
- conversation_model - 对话模式
- message_tokens - 消息中的令牌数
- answer_tokens - 回答中的令牌数
- total_tokens - 消息和回答中的总令牌数
- error - 错误信息
- inputs - 输入数据
- outputs - 输出数据
- file_list - 处理的文件列表
- start_time - 开始时间
- end_time - 结束时间
- message_file_data - 消息关联的文件数据
- conversation_mode - 对话模式
- Metadata 
  - conversation_id - 消息所属对话的ID
  - ls_provider - 模型提供者
  - ls_model_name - 模型ID
  - status - 消息状态
  - from_end_user_id - 发送用户的ID
  - from_account_id - 发送账户的ID
  - agent_based - 是否基于代理
  - workflow_run_id - 工作流运行ID
  - from_source - 消息来源
  - message_id - 消息ID

#### Moderation Trace信息
**用于追踪对话审查**

| Moderation            | LangFuse Generation/Trace   |
|-----------------------|-----------------------------|
| user_id               | user_id                     |
| moderation            | name                        |
| start_time            | start_time                  |
| end_time              | end_time                    |
| inputs                | input                       |
| outputs               | output                      |
| metadata              | metadata                    |
| [moderation]          | tags                        |
| message_id            | parent_observation_id       |

**Message Trace Info**
- message_id - 消息ID
- user_id: 用户id
- workflow_app_log_id workflow_app_log_id
- inputs - 审查的输入数据
- message_data - 消息数据
- flagged - 是否被标记为需要注意的内容
- action - 执行的具体行动
- preset_response - 预设响应
- start_time - 审查开始时间
- end_time - 审查结束时间
- Metadata
  - message_id - 消息ID
  - action - 执行的具体行动
  - preset_response - 预设响应

#### Suggested Question Trace信息
**用于追踪建议问题**

| Suggested Question         | LangFuse Generation/Trace   |
|----------------------------|-----------------------------|
| user_id                    | user_id                     |
| suggested_question         | name                        |
| start_time                 | start_time                  |
| end_time                   | end_time                    |
| inputs                     | input                       |
| outputs                    | output                      |
| metadata                   | metadata                    |
| [suggested_question]       | tags                        |
| message_id                 | parent_observation_id       |


**Message Trace Info**
- message_id - 消息ID
- message_data - 消息数据
- inputs - 输入的内容
- outputs - 输出的内容
- start_time - 开始时间
- end_time - 结束时间
- total_tokens - 令牌数量
- status - 消息状态
- error - 错误信息
- from_account_id - 发送账户的ID
- agent_based - 是否基于代理
- from_source - 消息来源
- model_provider - 模型提供者
- model_id - 模型ID
- suggested_question - 建议的问题
- level - 状态级别
- status_message - 状态信息
- Metadata
  - message_id - 消息ID
  - ls_provider - 模型提供者
  - ls_model_name - 模型ID
  - status - 消息状态
  - from_end_user_id - 发送用户的ID
  - from_account_id - 发送账户的ID
  - workflow_run_id - 工作流运行ID
  - from_source - 消息来源

#### Dataset Retrieval Trace信息
**用于追踪知识库检索**  

| Dataset Retrieval         | LangFuse Generation/Trace   |
|---------------------------|-----------------------------|
| user_id                   | user_id                     |
| dataset_retrieval         | name                        |
| start_time                | start_time                  |
| end_time                  | end_time                    |
| inputs                    | input                       |
| outputs                   | output                      |
| metadata                  | metadata                    |
| [dataset_retrieval]       | tags                        |
| message_id                | parent_observation_id       |

**Dataset Retrieval Trace Info**
- message_id - 消息ID
- inputs - 输入内容
- documents - 文档数据
- start_time - 开始时间
- end_time - 结束时间
- message_data - 消息数据
- Metadata
  - message_id消息ID
  - ls_provider模型提供者
  - ls_model_name模型ID
  - status消息状态
  - from_end_user_id发送用户的ID
  - from_account_id发送账户的ID
  - agent_based是否基于代理
  - workflow_run_id工作流运行ID
  - from_source消息来源

#### Tool Trace信息
**用于追踪工具调用**

| Tool                       | LangFuse Generation/Trace   |
|----------------------------|-----------------------------|
| user_id                    | user_id                     |
| tool_name                  | name                        |
| start_time                 | start_time                  |
| end_time                   | end_time                    |
| inputs                     | input                       |
| outputs                    | output                      |
| metadata                   | metadata                    |
| ["tool", tool_name]        | tags                        |
| message_id                 | parent_observation_id       |

**Tool Trace Info**
- message_id消息ID
- tool_name工具名称
- start_time开始时间
- end_time结束时间
- tool_inputs工具输入
- tool_outputs工具输出
- message_data消息数据
- error错误信息，如果存在
- inputs消息的输入内容
- outputs消息的回答内容
- tool_config工具配置
- time_cost时间成本
- tool_parameters工具参数
- file_url关联文件的URL
- Metadata
  - message_id消息ID
  - tool_name工具名称
  - tool_inputs工具输入
  - tool_outputs工具输出
  - tool_config工具配置
  - time_cost时间成本
  - error错误信息
  - tool_parameters工具参数
  - message_file_id消息文件ID
  - created_by_role创建者角色
  - created_user_id创建者用户ID

#### Generate Name Trace信息
**用于追踪会话标题生成**

| Generate Name              | LangFuse Generation/Trace   |
|----------------------------|-----------------------------|
| user_id                    | user_id                     |
| generate_name              | name                        |
| start_time                 | start_time                  |
| end_time                   | end_time                    |
| inputs                     | input                       |
| outputs                    | output                      |
| metadata                   | metadata                    |
| [generate_name]            | tags                        |

**Generate Name Trace Info**
- conversation_id对话ID
- inputs输入数据
- outputs生成的会话名称
- start_time开始时间
- end_time结束时间
- tenant_id租户ID
- Metadata
  - conversation_id对话ID
  - tenant_id租户ID
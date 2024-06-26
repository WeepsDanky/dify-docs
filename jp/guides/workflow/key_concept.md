# 重要な概念

### 1 ノード

**ノードはワークフローの重要な構成要素**であり、異なる機能を持つノードを接続することで、ワークフローの一連の操作を実行します。

ワークフローの主要なノードについては[ノード説明](node/)を参照してください。

***

### 2 変数

**変数はワークフロー内の前後ノードの入力と出力をつなぎ合わせるために使用され**、プロセス中の複雑な処理ロジックを実現します。

* ワークフローでは開始時に実行変数を定義する必要があります。例えば、チャットボットでは入力変数 `sys.query`を定義する必要があります。
* ノードでは一般的に入力変数を定義する必要があります。例えば、問題分類器の入力変数を `sys.query`として定義します。
* 変数を参照する際には、プロセス上流のノードの変数のみを参照できます。
* 変数名が重複しないように、ノード名は重複しないようにします。
* ノードの出力変数は通常、システム固定変数であり、編集できません。

***

### 3 チャットフローとワークフロー

**応用シーン**

* **チャットフロー**：対話型シナリオに向いており、カスタマーサービス、セマンティック検索、その他の応答を構築する際に多段階のロジックが必要な対話式アプリケーションに適しています。
* **ワークフロー**：自動化およびバッチ処理のシナリオに向いており、高品質な翻訳、データ分析、コンテンツ生成、電子メール自動化などのアプリケーションに適しています。

**使用方法**

<figure><img src="../../.gitbook/assets/output.png" alt=""><figcaption><p>チャットフロー入口</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/output (4).png" alt=""><figcaption><p>ワークフロー入口</p></figcaption></figure>

**利用可能なノードの違い**

1. 終了ノードはワークフローの終了ノードであり、プロセス終了時にのみ選択できます。
2. 回答ノードはチャットフロー用で、テキスト内容をストリーミング出力するために使用され、プロセスの中間ステップでも出力をサポートします。
3. チャットフローにはチャットメモリ（Memory）が内蔵されており、複数回の対話の履歴メッセージを保存および伝達するために使用されます。これはLLMや問題分類などのノードで有効にすることができますが、ワークフローにはメモリ関連の設定がなく、有効にできません。
4. チャットフローの開始ノードに内蔵されている変数には、`sys.query`、`sys.files`、`sys.conversation_id`、`sys.user_id`が含まれます。ワークフローの開始ノードに内蔵されている変数には、`sys.files`、`sys_id`が含まれます。
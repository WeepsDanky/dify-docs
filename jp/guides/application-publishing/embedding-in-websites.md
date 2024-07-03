# ウェブサイトへの埋め込み

Dify Apps は iframe を使用してウェブサイトに埋め込むことができます。これにより、Dify App をウェブサイト、ブログ、またはその他のウェブページに統合できます。

Dify Chatbot Bubble Button をウェブサイトに埋め込む際に、ボタンのスタイル、位置、その他の設定をカスタマイズできます。

## Dify Chatbot Bubble Button のカスタマイズ

Dify Chatbot Bubble Button は、以下の設定オプションでカスタマイズできます。

```javascript
window.difyChatbotConfig = {
    // 必須：Dify によって自動的に生成されます
    token: 'YOUR_TOKEN',
    // オプション：デフォルトは false です
    isDev: false,
    // オプション：isDev が true の場合、デフォルトは '[https://dev.udify.app](https://dev.udify.app)'、それ以外の場合は '[https://udify.app](https://udify.app)' です
    baseUrl: 'YOUR_BASE_URL',
    // オプション：`id` 以外の有効な HTMLElement 属性（例：`style`、`className` など）を受け入れます
    containerProps: {},
    // オプション：ボタンのドラッグを許可するかどうか、デフォルトは `false` です
    draggable: false,
    // オプション：ボタンのドラッグを許可する軸、デフォルトは 'both'、'x'、'y'、'both' のいずれかを指定できます
    dragAxis: 'both',
};
```

## デフォルトのボタンスタイルの上書き

CSS 変数または `containerProps` オプションを使用して、デフォルトのボタンスタイルを上書きできます。CSSの優先度に基づいてこれらの方法を適用し、希望のカスタマイズを実現します。

### 1.CSS 変数の変更

以下の CSS 変数をカスタマイズに使用できます。

```css
/* ボタンの下端からの距離、デフォルトは `1rem` */
--dify-chatbot-bubble-button-bottom

/* ボタンの右端からの距離、デフォルトは `1rem` */
--dify-chatbot-bubble-button-right

/* ボタンの左端からの距離、デフォルトは `unset` */
--dify-chatbot-bubble-button-left

/* ボタンの上端からの距離、デフォルトは `unset` */
--dify-chatbot-bubble-button-top

/* ボタンの背景色、デフォルトは `#155EEF` */
--dify-chatbot-bubble-button-bg-color

/* ボタンの幅、デフォルトは `50px` */
--dify-chatbot-bubble-button-width

/* ボタンの高さ、デフォルトは `50px` */
--dify-chatbot-bubble-button-height

/* ボタンの角丸、デフォルトは `25px` */
--dify-chatbot-bubble-button-border-radius

/* ボタンのボックスシャドウ、デフォルトは `rgba(0, 0, 0, 0.2) 0px 4px 8px 0px)` */
--dify-chatbot-bubble-button-box-shadow

/* ボタンホバー時の変形、デフォルトは `scale(1.1)` */
--dify-chatbot-bubble-button-hover-transform
```

例えば、ボタンの背景色を #ABCDEF に変更するには、次の CSS を追加します。

```css
#dify-chatbot-bubble-button {
    --dify-chatbot-bubble-button-bg-color: #ABCDEF;
}
```

### 2.`containerProps` を使用する

`style` 属性を使用してインラインスタイルを設定します。

```javascript
window.difyChatbotConfig = {
    // ... 他の設定
    containerProps: {
        style: {
            backgroundColor: '#ABCDEF',
            width: '60px',
            height: '60px',
            borderRadius: '30px',
        },
        // ちょっとしたスタイル変更の場合、style 属性に文字列を使用することもできます。
        // style: 'background-color: #ABCDEF; width: 60px;',
    },
};
```

`className` 属性を使用して CSS クラスを適用します。


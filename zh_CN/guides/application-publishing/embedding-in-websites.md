# 嵌入网站

Dify 应用可以使用 iframe 嵌入到网站中。这允许你将 Dify 应用集成到你的网站、博客或任何其他网页中。

当你在网站中使用 Dify 聊天机器人气泡按钮时，你可以自定义按钮的样式、位置和其他设置。

## 自定义 Dify 聊天机器人气泡按钮

Dify 聊天机器人气泡按钮可以通过以下配置选项进行自定义：

```javascript
window.difyChatbotConfig = {
    // 必填项，由 Dify 自动生成
    token: 'YOUR_TOKEN',
    // 可选项，默认为 false
    isDev: false,
    // 可选项，当 isDev 为 true 时，默认为 '[https://dev.udify.app](https://dev.udify.app)'，否则默认为 '[https://udify.app](https://udify.app)'
    baseUrl: 'YOUR_BASE_URL',
    // 可选项，可以接受除 `id` 以外的任何有效的 HTMLElement 属性，例如 `style`、`className` 等
    containerProps: {},
    // 可选项，是否允许拖动按钮，默认为 `false`
    draggable: false,
    // 可选项，允许拖动按钮的轴，默认为 `both`，可以是 `x`、`y`、`both`
    dragAxis: 'both',
};
```

## 覆盖默认按钮样式

你可以使用 CSS 变量或 `containerProps` 选项来覆盖默认按钮样式。根据 CSS 优先级使用这些方法实现自定义样式。

### 1.修改 CSS 变量

支持以下 CSS 变量进行自定义：

```css
/* 按钮距离底部的距离，默认为 `1rem` */
--dify-chatbot-bubble-button-bottom

/* 按钮距离右侧的距离，默认为 `1rem` */
--dify-chatbot-bubble-button-right

/* 按钮距离左侧的距离，默认为 `unset` */
--dify-chatbot-bubble-button-left

/* 按钮距离顶部的距离，默认为 `unset` */
--dify-chatbot-bubble-button-top

/* 按钮背景颜色，默认为 `#155EEF` */
--dify-chatbot-bubble-button-bg-color

/* 按钮宽度，默认为 `50px` */
--dify-chatbot-bubble-button-width

/* 按钮高度，默认为 `50px` */
--dify-chatbot-bubble-button-height

/* 按钮边框半径，默认为 `25px` */
--dify-chatbot-bubble-button-border-radius

/* 按钮盒阴影，默认为 `rgba(0, 0, 0, 0.2) 0px 4px 8px 0px)` */
--dify-chatbot-bubble-button-box-shadow

/* 按钮悬停变换，默认为 `scale(1.1)` */
--dify-chatbot-bubble-button-hover-transform
```

例如，要将按钮背景颜色更改为 #ABCDEF，请添加以下 CSS：

```css
#dify-chatbot-bubble-button {
    --dify-chatbot-bubble-button-bg-color: #ABCDEF;
}
```

### 2.使用 `containerProps` 选项

使用 `style` 属性设置内联样式：

```javascript
window.difyChatbotConfig = {
    // ... 其他配置
    containerProps: {
        style: {
            backgroundColor: '#ABCDEF',
            width: '60px',
            height: '60px',
            borderRadius: '30px',
        },
        // 对于较小的样式覆盖，也可以使用字符串作为 `style` 属性的值：
        // style: 'background-color: #ABCDEF; width: 60px;',
    },
}
```

使用 `className` 属性应用 CSS 类：

```javascript
window.difyChatbotConfig = {
    // ... 其他配置
    containerProps: {
        className: 'dify-chatbot-bubble-button-custom my-custom-class',
    },
};
```

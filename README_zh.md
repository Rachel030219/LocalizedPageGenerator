# Localized Page Generator

翻译管理灵感来源于 Android 的多语言页面生成工具。

[English version](README.md)

## 使用

#### 1. 编辑 `config.py`

设置你自己的模板文件与输出文件夹，比如：

```python
template_path = 'template.html'
output_dir = 'public'
```

然后生成的基于 `template.html` 的文件就会被输出到 "public" 文件夹。

#### 2. 添加语言

翻译源应当存储在 "sources/locales" 文件夹，以 `lpgdb` （Localized Page Generator DataBase）为后缀名，语言为文件名，且包括这样子的内容：

```
key>value
```

 `key` 就是模板中访问译文的键（见下文）， `value` 是键所对的值。 形如 `zh.lpgdb` 的文件会生成一个 `zh` 文件夹，内含基于模板和 `zh.lpgdb` 的 `index.html` 。

此外， `key` 周围的空格会被去掉，但是 `value` 的不会。

#### 3. 在模板中访问译文

被使用译文替换的文字应该看起来像 `%locales/key%` ， `key` 与 `.lpgdb` 里面那个一致。

看看 [template.html](sources/template.html) 作为示例。

#### 4. 输出

这个工具只会生成不同语言的页面，所以你可能还需要一个 `index.html` 来切换。此外，可能还需要 favicon 之类的东西，所以， LPG 会自动将 `resources` 文件夹里的东西扔进输出文件夹。

最后就可以愉快哒 `lpg_execute.py` 辣！

## TODO

- [x] 基础功能
- [ ] 语言回退
- [ ] 翻译文件夹自定义
- [ ] 输出自定义
- [ ] 命令行支持

## Credit

[Android Open Source Project (AOSP)](https://source.android.com/) 提供灵感

## LICENSE

MIT License
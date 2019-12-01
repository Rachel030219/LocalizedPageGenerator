# Localized Page Generator

A tool to generate pages of multiple languages with Android-inspired translation management.

[中文页面](README_zh.md)

## Usage

#### 1. Modify `config.py`

Set your own template file and output directory, for example:

```python
template_path = 'template.html'
output_dir = 'public'
```

Then the files published based on `template.html` will be published to "public" folder.

#### 2. Add languages

The translation sources should be stored in "sources/locales" folder, with `lpgdb` (Localized Page Generator DataBase) as the extension and the language as file name, which contain lines such as:

```
key>value
```

 `key` is how you access your translations in the template (described below), the `value` is the text. Files like  `en.lpgdb` generate a folder named `en` , containing an `index.html` based on template and `en.lpgdb`

BTW, spaces around `key` will be stripped, but for `value` not.

#### 3. Access translations in the template

The text to be replaced should look like `%locales/key%` , with the `key` the same as the one in the `.lpgdb` file.

Refer to [template.html](sources/template.html) as an example.

#### 4. Publish

This tool only generates pages of different languages, so you may need an extra `index.html` to switch between them. Things like favicon may also be needed, thus, LPG will automatically copy files in `resources` to the output folder.

Now you can happily run `lpg_execute.py` !

## TODO

- [x] Fundamental features
- [ ] Language fallback
- [ ] Translation source customization
- [ ] Output file customization
- [ ] Command line support

## Credit

[Android Open Source Project (AOSP)](https://source.android.com/) for inspiration

## LICENSE

MIT License
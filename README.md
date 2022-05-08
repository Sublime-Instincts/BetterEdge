# BetterEdge

![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/ST-Build%204107+-orange?style=for-the-badge&logo=sublime-text) ![Tag](https://img.shields.io/github/v/tag/Sublime-Instincts/BetterEdge?style=for-the-badge&logo=github&sort=semver) ![Syntax tests](https://img.shields.io/github/workflow/status/Sublime-Instincts/BetterEdge/syntax_test?color=green&label=Syntax%20Tests&logo=github&logoColor=white&style=for-the-badge)

A Sublime Text package that offers enhanced syntax highlighting, snippets, completions and much more for [Edge](https://docs.adonisjs.com/guides/views/introduction) templates. Read more for the full documentation.

## Features

- Indentation for code blocks.
- Snippets for common code blocks.
- Key bindings to make your life easier.
- Enhanced syntax highlighting for Edge templates.
- Autocompletions for built in tags, global helpers etc.

## Installation

#### Package Control
This package is not available on Package Control. To use it, follow the steps given below.

1. Copy the github url (without the `.git` at the end).
2. Select `Package Control: Add Repository` and paste the copied github url into the input panel and press <kbd>enter</kbd>.
3. Now use `Package Control: Install Package` and search for `BetterEdge` and install it.

## Documentation

### How to use this package ?

By default, this package supports the following Edge extensions: `.edge`, `html.edge`, `htm.edge`.

Since a user can have more than one templating language package installed, this package doesn't support `.html` directly. To get highlighting for `.html` files with Edge code and all the other features this package provides, you can follow any of the two approaches given below

1. Go to the bottom right status bar item that displays information on current syntax and click on that when the currently open file is any `.html` file. From there go to `Open all with current extensions as ...` and scroll to select `Edge`. You should now be good to go.

2. When the currently open file has any of the aforementioned file extensions, from the main menu, go to `Preferences -> Settings -- Syntax Specific`. This should open a 2 column new window, with the default settings on the right and a user settings on the left. In the user settings, add the following, save & close.

```json
{
    "extensions": [
        ".html"
    ]
}
```

### Key bindings

- The key bindings are configured so that pressing <kbd>shift + {</kbd> **twice** will automatically add spaces on both sides for the inner brace expression block & place the cursor in the center, like so `{{ | }}`.
- You can use <kbd>ctrl + /</kbd> for inserting Edge style comments (`{{-- This is a comment --}}`)

If you already have these in your user settings, then just copy the Twig related portions into them.

### Snippets

`BetterEdge` only adds basic snippets for common code blocks. If you want more snippets, then please follow the official documentation on
[snippets](https://www.sublimetext.com/docs/completions.html#snippets) and create your own.

If you want to ignore the snippets that are provided by default, you can use the `ignored_snippets` setting.

`"ignored_snippets": ["BetterEdge/*"]`

## Issues & Feature requests.

There is always scope for improvements so please do report any bug(s) that you encounter or request for feature(s) that this package should support.

Please follow the issue & feature request templates that have been setup while reporting any bug(s) or requesting for feature(s) (So as to stay as organised as possible).

## Acknowledgements.

The [syntax_test.yml](https://github.com/Sublime-Instincts/BetterEdge/.github/workflows/syntax_test.yml) is taken & used (with some modifications) from the official [Packages](https://github.com/sublimehq/Packages) repository. So full credit goes to them for it.

## License
The MIT License (MIT)

Copyright 2022 &copy; Ashwin Shenoy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

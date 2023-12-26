# Markdown Source File


---
__Advertisement ;)__

- __[text](web link)__ - inset text here....
- __[text](web link)__ - insert text here....

Use this as Promotion for you work

---


# h1 - Heading - Title
## h2 - Sub Heading
### h3 - Sub Heading
#### h4 - Sub Heading
##### h5 - Sub Heading
###### h6 - Sub Heading


## Horizontal Rules

___
---
***


## Typographic Replacement

enables typographer option to see result.
(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,, -- ---

## Emphasis - Special Keys

this is being *created* on a **Friday** ~~Saturday~~

using special characters either side of the text:-

*
_
**
__
~~

**This is bold text**
**This is bold**
*This is italic*
*This is italic*
~~Strikethrough~~


## Block Quote

> blockquote can also be nested
>>....by using additional greater-than signs right next to each other....
> > >...or with spaces in between arrows.


## Lists

Unordered

+ Create a list starting a line with '+', '-', or '*'*
+ Sub-lists are made by indenting 2 spaces:
    - Marker character change forces new list start:
        * Ac tristique volutpat at
        + Facilisis in pretium nisl aliquet
        - Nulla volutpat aliquam velit
+ Very easy!

* list
  * indent
        1. number

Ordered

1. Lorem ipsum dolar sit amet
2. Consectetur adispiscing elit
3. Interger molestie lorem at massa

1. You can use sequential numbers...
1. ...or keep all the numbers as '1.'


Starting numbering with offset:

57. foo
1. bar


## Code

Inline 'code'

Indented code
    
    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


Block code "fences"

...
Sample text here ...
...

Syntax highlighting


... js
var foo = function (bar) {
    return bar++;
};

console.log(foo(5));
...


''' html
<p>A paragraph example</p>
'''

''' javascript
let num = mMath.random();
'''

## Table

| Heading | header | head |
| --- | --- | --- |
| content | more content | text |
| more | more | more |

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


## Links

Link without a title
[this is the description](http:github.com)

Link with a title with title
[Github website](http:github.com/ "Github")


## Images

Like links, Images also have a footnote style syntax

![Alt text][id]

![alt text](http://piscsum.photos/200/200)

![alt text](http://piscsum.photos/200/200 "image")

reference in the document defining the URL location:

[id]: http://piscsum.photos/200/200 "image"


## Plugins

`markdown-it` supports
[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).

## Variable
this paragraph has some 'variable' inline code


### [Emojies](https://github.com/markdown-it/markdown-it-emoji)

> Classic markup: :wink: :cry: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

see [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.

### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)

* 19^th^
* H~2~O

### [\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Inserted text++

### [\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Marked text==

### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)

Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.

### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)

Term 1

:   Definition 1
with lazy continuation.

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

*Compact style:*

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b

### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)

This is HTML abbreviation example.

It converts "HTML", but keep intact partial entries like "xxxHTMLyyy" and so on.

*[HTML]: Hyper Text Markup Language

### [Custom containers](https://github.com/markdown-it/markdown-it-container)

::: warning
*Danger Alert*
:::


## Colored text

```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```

However, it adds it as a new line starting with either - + ! # or starts and ends with @@


For coloring texts in GitHub README.md, you can use SVG <text>


One way to add color to a README is by utilizing a service that provides placeholder images.

For example this Markdown can be used:

- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `#f03c15`
- ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) `#c5f015`
- ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `#1589F0`

To create a list of any colors you like:

# f03c15 #f03c15
# c5f015 #c5f015
# 1589F0 #1589F0


Now since May 2022, Github can accept LATEX code on Markdown, so you can use the \color{namecolor} inside the $$$$ Block, like the example below:

Basic
Code Appearing
$${\color{red}Red}$$ $${\color{red}Red}$$
$${\color{green}Green}$$ $${\color{green}Green}$$
$${\color{lightgreen}Light \space Green}$$ $${\color{lightgreen}Light \space Green}$$
$${\color{blue}Blue}$$ $${\color{blue}Blue}$$
$${\color{lightblue}Light \space Blue}$$ $${\color{lightblue}Light \space Blue}$$
$${\color{black}Black}$$ $${\color{black}Black}$$
$${\color{white}White}$$ $${\color{white}White}$$

More then one color

$${\color{red}Welcome \space \color{lightblue}To \space \color{orange}Stackoverflow}$$


At the time of writing, GitHub Markdown renders color codes like `#ffffff` (note the backticks!) with a color preview. Just use a color code and surround it with backticks.

For example:

'#00ff00'
'rgba(0,0,0,1)'

This feature has limited availability, as the docs state:
[Supported color models](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#supported-color-models "Supported color models]")

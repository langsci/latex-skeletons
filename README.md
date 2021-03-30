# latex-skeletons
These templates are the ready-to-use LaTeX sources to compile Language Science Press publications.
They can be obtained as packed `.zip` files from [our website](https://langsci-press.org/templatesAndTools) or the [`gh-pages`](https://github.com/langsci/latex-skeletons/tree/gh-pages) branch.

The templates in this GitHub repository work with TeX Live 2020 and up to date CTAN sources.

## Which files should I use? 
This depends on your role:

* If you are the author for a monograph, you need the monograph skeleton in the [`/skeleton/`](skeleton/) folder.
* If you are an editor for a collection of papers, you need the monograph for edited volumes from [`/editedskeleton/`](editedskeleton/) folder.
  Feel free to supply your contributing authors with a copy of the [`/paper/`](paper/) folder, which they can use to write their paper. 
* If you are a contributing author in a collection of papers, you'll need the [`/paper/`](paper/) folder structure.

## How do I compile the sources?
There are some recipes in the `Makefile`. For most purposes, it suffices to compile `main.tex` with XeLaTeX, then compiling the bibliography with `biber` (run on file `main`), and compiling `main.tex` with XeLaTeX again so that the bibliography and ToC appear.

## Where do I enter my meta data?
Here is an overview. These settings are for `skeleton` and `editedskeleton` only. The meta data for `paper` are inserted directly in `main.tex`.

File | Setting | Meaning | 
---- | ------- | ------- |
`main.tex` | `\addbibresource{<file.bib>}` | The location of your bibliographical database. The recommended file name is `localbibliography.bib`.
`main.tex` | option `multiauthors` | Enable this option if there is more than one editor/author.
`main.tex` | option `booklanguage=<language>` | Set this option if you are writing in another language than English. Currently supported are: `chinese`, `french`, `german`, `portuguese`. Please get in touch if you need another.
`localmetadata.tex` | `\title` | The book's title of either monograph or collected volume.
`localmetadata.tex` | `\subtitle` | The book's subtitle of either monograph or collected volume.
`localmetadata.tex` | `\author` | The name of all contributing author(s) or editor(s). Individuals are separated by `and`. Please see [this Wiki page](https://github.com/langsci/langscibook/wiki/Inserting-authors-and-editors-with-langsci-affiliations) for details.
`localmetadata.tex` | `\BackBody` | The blurb displayed on the back cover.
`localmetadata.tex` | `\Series` | The shorthand of the series you are publishing your book in.
`localseealso.tex`  |           | Recipes for links in the Indexes.

## Where can I get technical support?
The Support Contact details are [listed on our website](https://langsci-press.org/about).

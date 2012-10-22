# -*- coding: utf-8 -*-
#
# Getting Started with Xapian documentation build configuration file, created by
# sphinx-quickstart on Sun Oct 30 10:34:37 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import re
from docutils import nodes, utils
from docutils.parsers.rst import roles
from docutils.parsers.rst.roles import set_classes
from sphinx.directives.code import LiteralInclude, directives

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Getting Started with Xapian'
_authors = u'Olly Betts, Richard Boulton, Dan Colish, Justin Finkelstein, James Aylett'
copyright = u'2011, 2012 ' + _authors

github_project_url = 'https://github.com/jaylett/xapian-docsprint/blob/master'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'GettingStartedwithXapiandoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'GettingStartedwithXapian.tex', u'Getting Started with Xapian Documentation',
   _authors, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# Cause todos to be displayed.
todo_include_todos = True

# Default to setting 'py' tag if none are set, and set highlight language
# appropriately.

last_example = None

if tags.has('php'):
    highlight_language = 'php'
    ext = '.php'
elif tags.has('cc'):
    highlight_language = 'c++'
    ext = '.cc'
else:
    tags.add('py')
    highlight_language = 'python'
    ext = '.py'


def github_link_node(name, rawtext, options=()):
    try:
        base = github_project_url
        if not base:
            raise AttributeError
    except AttributeError, err:
        raise ValueError(
            'github_project_url configuration value is not set (%s)' % str(err))
    slash = '/' if base[-1] != '/' else ''
    ref = base + slash + rawtext
    if not options:
        options = {}
    set_classes(options)
    node = nodes.reference(name, utils.unescape(name), refuri=ref,
                           **options)
    return node


def xapian_code_example_filename(ex):
    return "code/%s/%s%s" % (highlight_language, ex, ext)

def xapian_code_example_command(ex):
    if highlight_language == 'python':
        return "python %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'php':
        return "php %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'c++':
        return "g++ `xapian-config --cxxflags` %s -o %s `xapian-config --libs`\n./%s" \
            % (xapian_code_example_filename(ex), ex, ex)
    else:
        return "???"

class XapianCodeExample(LiteralInclude):
    option_spec = {
        'linenos': directives.flag,
        'tab-width': int,
        'language': directives.unchanged_required,
        'encoding': directives.encoding,
        'pyobject': directives.unchanged_required,
        'lines': directives.unchanged_required,
        'start-after': directives.unchanged_required,
        'end-before': directives.unchanged_required,
        'prepend': directives.unchanged_required,
        'append': directives.unchanged_required,
        'emphasize-lines': directives.unchanged_required,
        'marker': directives.unchanged_required,
    }

    def run(self):
        global last_example
        last_example = self.arguments[0]
        filename = xapian_code_example_filename(last_example)
        if not os.path.exists(filename):
            return [nodes.literal(text = 'No version of example %s in language %s - patches welcome!'
                % (last_example, highlight_language))]
        self.arguments[0] = "/" + filename
        if not 'start-after' in self.options and not 'end-before' in self.options:
            if 'marker' in self.options:
                marker = self.options['marker']
                del self.options['marker']
            else:
                marker = 'example code'
            self.options['start-after'] = 'Start of ' + marker
            self.options['end-before'] = 'End of ' + marker
        return super(XapianCodeExample, self).run()

# Usage:
# .. xapianexample:: search_filters2
directives.register_directive('xapianexample', XapianCodeExample)

class XapianRunExample(LiteralInclude):
    option_spec = {
        'args': directives.unchanged_required,
    }

    def run(self):
        filename = xapian_code_example_filename(self.arguments[0])
        if not os.path.exists(filename):
            return [nodes.literal(text = 'No version of example %s in language %s - patches welcome!'
                % (last_example, highlight_language))]
        command = xapian_code_example_command(filename)

        if 'args' in self.options:
            def esc_char(match):
                return "=%02x" % ord(match.group(0))
            args = self.options['args']
            command = "%s %s" % (command, args)
            esc_args = re.sub(r'[^-A-Za-z0-9 .]', esc_char, args)
            esc_args = re.sub(r' ', r'_', esc_args)
            fullout = "%s.%s.out" % (filename, esc_args)
            print "[%s]" % fullout
            if os.path.exists(fullout):
                filename = fullout
            else:
                filename = filename + ".out"
        else:
            filename = filename + ".out"

        self.options['prepend'] = '$ ' + command
        # FIXME: Only want this syntax highlighting for lines starting '$'.
        # self.options['language'] = 'sh'
        self.options['language'] = 'none'
        self.arguments[0] = "/" + filename
        return super(XapianRunExample, self).run()

# Usage:
# .. xapianrunexample:: search_filters2
directives.register_directive('xapianrunexample', XapianRunExample)

def xapian_code_example_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    if ex == '^' and last_example:
        ex = last_example
    code_path = xapian_code_example_filename(ex)
    return [github_link_node(code_path, code_path, options)], []


def xapian_code_example_short_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    if ex == '^' and last_example:
        ex = last_example
    return [
        github_link_node(
            os.path.basename(ex) + ext,
            xapian_code_example_filename(ex), options)
        ], []


def xapian_example_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    return [github_link_node(ex, ex, options)], []


def xapian_example_short_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    return [github_link_node(os.path.basename(ex), ex, options)], []

# Usage:
#
# The previous example was :xapian-code-example:`^`.
#
# The foo example is in :xapian-code-example:`foo`.
roles.register_local_role('xapian-code-example', xapian_code_example_role)
roles.register_local_role('xapian-basename-code-example', xapian_code_example_short_role)
roles.register_local_role('xapian-basename-example', xapian_example_short_role)
roles.register_local_role('xapian-basename-example', xapian_example_role)

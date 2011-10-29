Databases
=========

Pretty much all Xapian operations revolve around a Xapian database.  Before
performing a search, details of the documents to be searched need to be put
into the database; the search process then refers to the database to
efficiently determine the best matches for a given query.  The process of
putting documents into the database is usually referred to as _indexing_.

The main information stored in a database is a mapping each term to a list
of all the documents it occurs in, together with various statistics about
these occurrences.  It may also store the full text, or extracts, from the
documents, so that result summaries can be displayed.  Databases can also
contain additional data such as tables for spelling correction and synonym
expansion; developers can even store arbitrary key-value pairs in part of
the database.

Xapian databases store data in custom formats which allow searches to be
performed extremely quickly; Xapian does not use a relational database as
its datastore.  There are several database backends; the main backend in
the 1.2 release series of Xapian is called the "Chert" backend.  This
stores information in the filesystem (under a given path).  If you're
familiar with data storage structures, you might be interested to know that
this backend uses a B+-tree structure with copy-on-write, but don't worry
if that doesn't mean anything to you!

Most backend formats (and certainly the main backend format for each
release) will allow updates to be grouped into transactions, and will allow
at least some old versions of the database to be searched while new ones
are being written.

As well as the main backend, there is a "remote" database backend which
allows the database to be located on a different machine and accessed via a
custom TCP protocol. It is possible to perform searches across multiple
databases at once, and Xapian will handle merging the results together
appropriately. This can be used to handle datasets which are too large for
a single machine, by performing searches across multiple remote databases.

Xapian has also special support for replicating databases to multiple
machines, such that only the parts of the database which have been modified
are copied; this can be useful for redundancy and load-balancing purposes.

Xapian also supports a simple file format for listing the locations of a
set of databases (either on the local file system, or remote databases).
Such files are called stub-databases_, and can be used to point to a
database when the physical database location may vary; for example, because
a new database is being built nightly, and is named according to the date
on which it was built.
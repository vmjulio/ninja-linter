# Ninja Linter 
## The Ninja SQL Style Guide

Ultimate style guide for SQL queries. 

# Getting Started

To get started just run the cli

```shell
$ echo "  SELECT a  +  b FROM tbl;  " > test.sql
$ ninjalinter lint test.sql
== [test.sql] FAIL
L:   1 | P:   1 | L003 | Single indentation uses a number of spaces not a multiple of 4
L:   1 | P:  14 | L006 | Operators should be surrounded by a single space unless at the start/end of a line
L:   1 | P:  27 | L001 | Unnecessary trailing whitespace
```

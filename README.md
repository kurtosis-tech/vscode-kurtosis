# Kurtosis Starlark VSCode Extension (Official) (Pre-release)

The Official Kurtosis Starlark VSCode extension enriches developer experience when writing Kurtosis packages in Starlark. The specific features supported are:

1. Syntax Highlighting
2. Auto-completion of Kurtosis defined Starlark instructions and types
3. Hover preview for functions 
4. Method signature suggestions for Kurtosis defined Starlark instructions and types

This extension is currently under continuous development and may feel little rough around the edges. There are many exciting capabilities added to this extension in upcoming months; meanwhile if you encounter any issues - please report them using `kurtosis feedback` and we shall incorporate them.

## Requirements
1. Kurtosis version >= 0.73.0
2. VSCode version >= 1.74.2

## Extension Settings
1. `klsp.trace.server`: It controls the logging for language server requests/responses. The default value is `off`, and other valid values are `verbose` and `debug
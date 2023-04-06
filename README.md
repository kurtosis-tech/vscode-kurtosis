# Kurtosis Starlark VSCode Extension (Official)

The Official Kurtosis Starlark VSCode extension enriches the developer experience when writing Kurtosis packages in [Starlark](https://docs.kurtosis.com/concepts-reference/starlark). The specific features supported are:

1. Syntax Highlighting
2. Auto-completion of Kurtosis defined Starlark instructions and types
3. Hover preview for functions 
4. Method signature suggestions for Kurtosis defined Starlark instructions and types

This extension is currently under continuous development and may feel little rough around the edges. We do plan to add more features to this extension in the future. Should you encounter any issues or have a feature you'd like to see added let us know using the  `kurtosis feedback` command or [email us](mailto:feedback@kurtosistech.com) and we'll get back to you as soon as we can.

## Requirements
1. Kurtosis version >= 0.73.0
2. VSCode version >= 1.74.2

## Extension Settings
1. `klsp.trace.server`: It controls the logging for language server requests/responses. The default value is `off`, and other valid values are `verbose` and `debug

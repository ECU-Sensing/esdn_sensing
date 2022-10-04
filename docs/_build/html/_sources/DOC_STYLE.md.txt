# Documentation Styling Guide

#### Preface:
All modules added to this codebase **must be documented**, including all the submodules/classes/functions/etc. Code will have to adhere to this strict styling guide or it will not be included in the main distribution. 

This will be reviewed during the pull request process!

## Style:
Luckily, the style we chose is fairly standard to Python development and so many will not have difficulty adhering to these guidelines. Many docstring generation tools will utilize the same formatting; a great example is [AutoDocstring](https://github.com/NilsJPWerner/autoDocstring) created for [VSCode](https://code.visualstudio.com/). 

### Main Components:
* Every module should include license boilerplate
* Every module should include author information
* Every function, class, etc. should be documented

Main of our styling requirements mirror that of [Google Python Docstring Guidelines](https://google.github.io/styleguide/pyguide.html). 

### Requirements
#### Naming
 Our naming requirements are pulled directly from the [Google Python Docstring Guidelines](https://google.github.io/styleguide/pyguide.html). See table below.

 |Type          | Public       | Internal    |
 |--------------|--------------|-------------|
 | Packages | lower_with_under ||
 | Modules | lower_with_under | _lower_with_under|
 | Classes| CapWords | _CapWords |
 | Exceptions | CapWords| | 
 | Functions | lower_with_under() | _lower_with_under()|
 |Global/Class Constants | CAPS_WITH_UNDER | _CAPS_WITH_UNDER|
 |Global/Class Variables | lower_with_under | _lower_with_under |
 |Instance Variables | lower_with_under | _lower_with_under (protected) |
 |Method name | lower_with_under() | _lower_with_under (protected) |
 |Function/Method Parameters| lower_with_under ||
 |Local Variables | lower_with_under ||

#### Documentation
 Our documentation seeks to provide information on every aspect of the module. To accomplish this and enable collaboration we want to point out a few necessary inclusions to documentation:

##### Variables

```
{{name}}                        - name of the function
{{summaryPlaceholder}}          - [summary] placeholder
{{extendedSummaryPlaceholder}}  - [extended_summary] placeholder
```

##### Sections

```
{{#args}}                       - iterate over function arguments
    {{var}}                     - variable name
    {{typePlaceholder}}         - [type] or guessed type  placeholder
    {{descriptionPlaceholder}}  - [description] placeholder
{{/args}}

{{#kwargs}}                     - iterate over function kwargs
    {{var}}                     - variable name
    {{typePlaceholder}}         - [type] or guessed type placeholder
    {{&default}}                - default value (& unescapes the variable)
    {{descriptionPlaceholder}}  - [description] placeholder
{{/kwargs}}

{{#exceptions}}                 - iterate over exceptions
    {{type}}                    - exception type
    {{descriptionPlaceholder}}  - [description] placeholder
{{/exceptions}}

{{#yields}}                     - iterate over yields
    {{typePlaceholder}}         - [type] placeholder
    {{descriptionPlaceholder}}  - [description] placeholder
{{/yields}}

{{#returns}}                    - iterate over returns
    {{typePlaceholder}}         - [type] placeholder
    {{descriptionPlaceholder}}  - [description] placeholder
{{/returns}}
```

##### Additional Sections

```
{{#argsExist}}          - display contents if args exist
{{/argsExist}}

{{#kwargsExist}}        - display contents if kwargs exist
{{/kwargsExist}}

{{#parametersExist}}    - display contents if args or kwargs exist
{{/parametersExist}}

{{#exceptionsExist}}    - display contents if exceptions exist
{{/exceptionsExist}}

{{#yieldsExist}}        - display contents if returns exist
{{/yieldsExist}}

{{#returnsExist}}       - display contents if returns exist
{{/returnsExist}}

{{#placeholder}}        - makes contents a placeholder
{{/placeholder}}
```
Thank you to [NilsJPWerner](https://github.com/NilsJPWerner) for providing this example. You can use his Python Docstring generation tool for VSCode to quickly create documentation such as this. 


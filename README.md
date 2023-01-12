# Kurtosis Plugin (Under Development)

This plugin is under development and currently in order to use this follow the steps below

## Setup

The below steps are temporary, ideally we would like to ingtegrate lsp service with kurtosis using `kurtosis lsp` or similar.  
It will involve moving `starlark-lsp` to `kurtosis` repo and integrating with `kurtosis cli`

Until then, this should get the things going.

1. Clone this folder

2. Go to `starlark-lsp` folder and in it

    > go install ./...

    ( This should create `starlark-lsp` executable and installs it in `$GOPATH/bin`) 
    
    *Important*

    This assumes that `GOPATH` is configured - if not then the plugin won't work.  
    Add the lines below in `bash_profile` or similar file, replace `<username>` with
    your username.
    
    > export GOPATH=/Users/<username>/go   
      export PATH="${GOPATH}/bin:$PATH"

## Run  

1. Open `kurtosis-plugin` folder in `Visual Studio Code`

2. Press `F5`. This should open a new window and in the title you should see `Extension Development Host`.  

3. In the `Extension Development Host` window, you should be able to see plugins capabiltites on `.star` files.

## Publish
//TODO
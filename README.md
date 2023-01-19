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
    
    ### Important

    This assumes that `GOPATH` is configured - if not then the plugin won't work.  
    Add the lines below in `bash_profile` or similar file, replace `user_name` with
    your username.
    
    > export GOPATH=/Users/user_name/go   
      export PATH="${GOPATH}/bin:$PATH"    
      source ~/.bash_profile (or similar)

## Run  

1. Open `kurtosis-plugin` folder in `Visual Studio Code`
   
   Check whether env variables in VSCODE, see the updated path:-
   
   <img width="1728" alt="Screen Shot 2023-01-19 at 9 49 11 AM" src="https://user-images.githubusercontent.com/15133250/213478971-59d6ca80-2551-48fd-ae0f-04efabbef706.png">

    If you don't see your PATH being updated, please restart VsCode to read new global path variables.

2. Press `F5`. This should open a new window and in the title you should see `Extension Development Host`
    
    <img width="1728" alt="Screen Shot 2023-01-19 at 10 19 11 AM" src="https://user-images.githubusercontent.com/15133250/213481201-50d1345a-3b2d-46e6-adc4-1c092abf49c5.png">
    
      1. Open command view and select `kurtosis lsp`:
           `Cmd` + `Shift` + `P` ( to open command palette)
      2. Search for `Output: Focus on Output View`
      3. Once the view is open, select `kurtosis_lsp`
      4. You should see the logs from `starlark-lsp server`

3. In the `Extension Development Host` window, you should be able to see plugins capabiltites on `.star` files.

## Publish
//TODO

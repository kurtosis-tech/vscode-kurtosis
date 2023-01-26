# Kurtosis Plugin (Under Development)

## Setup

Please follow the setups outlined below to run kurtosis plugin with starlark code. It assumes that you have `go`, `node`, and `npm` already installed.

1. Add GoPath to your Path  
  Add the following lines in your `bash_profile` or similar file.
  > 
    export GOPATH=/Users/{USER_NAME}/go (where USER_NAME is your username)    
    export PATH="${GOPATH}/bin:$PATH"
2. source ~/.bash_profile
3. cd `vscode-kurtosis`
4. `npm install .`
5. cd `starlark-lsp`  
6. `go install ./...`

## Run

1. Open `vscode-kurtosis` folder in `Visual Studio Code`.   
2. Press `F5`, and it will open another window titled `Extenstion Development Host` and has the extension capabilites.   
    Create or open an existing `*.star` files, and you should see the extension in action.
   
## Debug   
  If `plugin` does not work, check whether vscode has latest path variable. In the main vscode window (where vscode-kurtosis folder is opened), view `DEBUG CONSOLE` and verify `$GOPATH` is defined in $PATH variable like shown below. 
  
  #### Example image:
  
  <img width="1716" alt="Screen Shot 2023-01-26 at 12 29 38 AM" src="https://user-images.githubusercontent.com/15133250/214765520-348b3b64-5027-4f08-adde-b049bdce3094.png">
 
  If you do not see `$GOPATH` in the `PATH`, restart the `vs-code`.
  You can also check the server logs, by going to `kurtosis_lsp` ouput section in `Extenstion Development Host`, to do so follow the steps below:

  1. Open Command Pallete (`Cmd` + `Shift` + `P`)
  2. Search for `Output: Focus on Output View`
  3. Once the view is open, select `kurtosis_lsp` and you should see the logs. 
  4. If you don't see any logs or only see error logs, let me know!
           
  #### Example image:   

  <img width="1728" alt="Screen Shot 2023-01-19 at 10 19 11 AM" src="https://user-images.githubusercontent.com/15133250/213481201-50d1345a-3b2d-46e6-adc4-1c092abf49c5.png">

## Next Steps

This [document](https://www.notion.so/kurtosistech/Project-IDE-support-for-Starlark-4030246877004e928ecb935a4233ca54) contains more information about the plugin, and lays out some of the next steps.

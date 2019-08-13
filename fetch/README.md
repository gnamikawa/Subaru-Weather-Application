# Fetch Scripts 💾

These scripts are mainly for the organized launching of applications within the Subaru Weather Application (SWA). There are a total of four scripts that were created for the application. Each script must be edited to search-and-replace `Genzo` with the specified username, or to replace the path altogether.

|Name|Description|
|-|-|
|`CopyScript.sh`|A script to copy data from the server's directories, and the SWA-generated images.|
|`GenerateScript.sh`|A script to launch the python application with the options `-l` and `-o` which ultimately collects data then outputs images based on the data. (It is recommended that the user launch the options separately utilizing cronjob. This will allow the user better control of the frequency to update the graph, and the frequency to update the data. )|
|`Master.sh`|A script to launch both the `CopyScript.sh` and `GenerateScript.sh` one after another in the required Miniconda environment.|
|`Webdev.sh`|A script to launch any application within the `Webdev` Miniconda environment.|

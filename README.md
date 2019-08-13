# 1. Subaru Weather Application

The Subaru Weather Application (SWA) was developed in order to replace the previous, outdated website on the internal company website. The project was developed as a system of four components: Subaru Weather Application, the website itself; Figurebot, a graph generation script; Fetch, a combination of launch scripts and copy scripts, and the makefile as a deployment script (Hardcoded paths and does not build the application).  

## 1.1. System Overview

The system was coded using multiple programming and scripting languages on a 64-bit Windows installation and installed on a Red-Hat 7.6 Server through SSH. This project uses JavaScript (JS), Cascading Style Sheets (CSS), Hypertext Markup Language (HTML), Python, and Bash. The project, split in parts, uses the technologies in the following fashion:  

List of technologies and libraries per section  

| Name | Purpose | Technologies | Libraries |
|-|-|-|-|
| `Website (SWA)` | Front-end Website. | JS, JSX, HTML, CSS, React, NPM | D3, and Semantic-UI |
| `Figurebot` | Graph generation and data collection. | Miniconda and Python | Numpy, Matplotlib, Chest, G2cam |
| `Fetch` | Launch scripts and copy scripts. | Bash | None |
| `Makefile` | Installs dependencies then moves applications to their respective locations. | Make and Bash | None |  

The application was created with the intention that this is a one-time implementation that does not require relocation. Therefore, the locations and paths for obtaining website material and installing the software were hardcoded for both the makefile and fetch scripts respectively.  

However, the Figurebot was designed to be very reconfigurable, and has a settings file to accommodate many different situations. The Figurebot can generate an array of different figures with multiple plots just by tweaking the settings.  

Here are some useful documents and links that I have used for development:  

|Name|Description|Link|
|-|-|-|
|G2cam|G2cam is a Python module for interfacing instruments to Subaru Telescope.|https://github.com/naojsoft/g2cam/|
|React|A JavaScript library for building user interfaces.|https://reactjs.org/|
|Semantic-UI React|A React library for creating quick and stylish user interfaces. |https://react.semantic-ui.com/|
|Miniconda|A portable environment for python. Can install python-unrelated packages like nodejs to the environment if need-be.|https://docs.conda.io/en/latest/miniconda.html/|

## 1.2. Installation for Development

The Installation of the SWA is as simple as any other application that uses a “make” script on Linux, ASSUMING that the prerequisites are met. The process should be simple if it is installed on the “SHELL” system, although it may prove to be a challenge if the location or environment is changed.  

The SWA must be installed on the “SHELL” server to guarantee that fetch script can obtain the website’s images and data. Currently, there exists no script to automate this check, and the program relies on not being moved from the “SHELL” environment and server. The application can be moved anywhere within the server if the scripts’ path variables are changed accordingly.

### 1.2.1. Prerequisites

There are prerequisites that must be manually installed to the system. This set of software should be installed on the system by the user. The software required for development are as follows:

#### Installation Environment

| Item | Description |
|-|-|
| Python 3.7.4 | Python interpreter. Used to create and run python applications. |
| ReactJS | Foundation for modern web-applications. Specialized in creating Single Page Applications. |
| NPM (NodeJS) |  Package manager for website components. |
| Git | Used for version tracking and the cloning of a repository for building. |
| Miniconda | Environment manager for python scripts. Used to quickly swap libraries and Python versions. |

## 1.3. Setting the environment up

In order to get the system up and running, we need to first install the Miniconda environment to the user directory.

### 1.3.1. Install Miniconda

In the user home directory, type the following commands:

```bash
$ cd <HOME_DIRECTORY>
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
$ rm Miniconda3-latest-Linux-x86_64.sh
```

These commands will first download the latest Miniconda distribution for linux. It will then run the installation script and install the distribution to the home directory. The final command will remove the installation script from the directory.

### 1.3.2. Miniconda setup

Next, we need to set the Miniconda environment up. The Miniconda environment does not come automatically set-up, so we need to edit the user's `.bashrc` file and their `.bash_profile`. These files should be created if they do not exist.

The `.bash_profile` script should look like this:

```bash
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH
```

The `.bashrc` script should look like this, but replace all `<USERNAME>` occurrences with your actual username (ctrl+f):

```bash
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

export PATH=$HOME/miniconda3/bin:$PATH\

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/<USERNAME>/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/<USERNAME>/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/<USERNAME>/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/<USERNAME>/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

### 1.3.3. Creation of the Development Environment

Next, we need to create an environment for the web-application to run within. Type the following commands:

```bash
$ conda create -n webdev python=3.7
$ conda activate webdev
```

This will create the environment for the application to run in.  
Next, install the following python packages and NodeJS through the conda package manager:

```bash
$ conda install numpy 
$ conda install pymongo
$ conda install chest
$ conda install matplotlib
$ conda install nodejs
```

## 1.4. Installation of the Website and its Components

### 1.4.1. Create a Location for the SWA Website's Scripts

Make sure that you are in the home directory and run the following commands:

```Bash
$ mkdir Git
$ cd Git
$ git clone "https://github.com/gnamikawa/SubaruWeatherApplet"
```

Run the following in the user's home directory, or choose another directory for the deployment location:
```Bash
$ mkdir -p "public_html/Weather"
```

#### Make Commands

|Command|Description|
|-|-|
| `make cleanall` | Removes all dependencies and libraries for the website and generated data/output from previous sessions. (runs `dataclean` and `websiteclean`) |
| `make websiteclean` | Cleans and rids the website of all of its dependencies. |
|`make dataclean`|Cleans and rids the application of all data and output that the program may have generated from previous sessions.|
|`make getdep`|Installs all dependencies for the website.|
|`make build`|Runs the build script for the website. Outputs to `swa/website/build`.|
|`make or make deploy`|Runs `make getdep` then `make build`. This command will install the website's dependencies, and then it will build the website.|

Run the following in the base directory of the swa where the `Makefile` resides:

```Bash
$ cd Git/swa
$ make cleanall
$ make deploy
```

Next, for each of the following files, replace the username of `Genzo` with the respective username, and make sure to change the `homepage` within the `package.json` file to ensure that the webpage can refer to itself correctly.

|File|Location|
|-|-|
|`Copyscript.sh` |`Git/swa/fetch/Master.sh/Webdev.sh/CopyScript.sh`|
|`package.json` |`Git/swa/website/package.json`|

Next, change your directory to the root directory of the project and run the following:
```bash
$ cd fetch
$ bash Master.sh 
```
This should copy data from around the server into the website's image and data directories. Once finished, it will move the built website into the directory of your choice.

## 1.5. Crontabs

Finally, crontabs are required to make sure that the website is updated with the most recent data. Run the following to manage your chrontabs and then insert the following code snippet into your file. Make sure to replace `<USERNAME>` with your actual username.

```bash
$ crontab -e
```

```
# Chrontab Example
HOME=/home/<USERNAME>
* * * * * /usr/bin/bash $HOME/Git/swa/fetch/Master.sh >> $HOME/cronlog.txt 2>&1
```


# 2. Unfortunately out of time.

I have unfortunately run out of time to write the rest of the documentation. Here is a snippet of the rest of the notes that Mr.Inagaki has kindly written. Other snippets can be found within each components' directories as `README.md` files. Most of this information was supposed to lie in them. 

Thank you for your understanding.

```bash


# add/delete image. 
    note: /home/tinagaki/Git/swa/website/src/Components
          CameraCollection.js  - camera images
          GraphCollection.js  -  plots
          DetailCollection.js - table(labels)

    * edit /home/tinagaki/Git/swa/website/src/Components/CameraCollection.js

      e.g.,
      QuadLayout(Data){ 
      <Segment.Group vertical>
                <Segment.Group horizontal>
                    <Segment textAlign={"center"}>
                        {this.ConstructPil(this.state.Images.E, this.state.Thumbs.E)}
                        Test<br/>Test: - - - # or {this.HumidityTooltip("Test", 60)}
                    </Segment>
                    <Segment textAlign={"center"}>
                        
                    </Segment>

      </Segment.Group>
      }


      <Container fluid stretched >
      <Menu fluid pointing style={menu} attached={"bottom"}>
          ...   
            
        <Menu.Item
         as={"a"}
         name={"T"}
         active={activeItem === "T"}
         onClick={this.HandleItemClick}
        />

      </Menu>

     {activeItem==="Overview" && this.QuadLayout(this.FormattedData())}
     ...
     {activeItem==="T" && <Segment> {this.ConstructPil(this.state.Images.S, this.state.Thumbs.S)} </Segment>}




    * make and copy 
      (webdev) [tinagaki@om04 swa]$$make cleanall; make 
      (webdev) [tinagaki@om04 fetch]$ bash Master.sh 

    * refresh web 
```
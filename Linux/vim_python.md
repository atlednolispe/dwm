vim简单配置支持Python
===================


## 通过vundle配置ycm

[Vundle](https://github.com/VundleVim/Vundle.vim)

```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

```
$ vim ~/.vimrc

" 修改为以下内容
set nocompatible              " be iMproved, required
set backspace=2               " backspace delete
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
" Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
" Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

Plugin 'scrooloose/nerdtree'
Bundle 'ShowTrailingWhitespace'
Bundle 'scrooloose/syntastic'

Plugin 'MarcWeber/vim-addon-mw-utils'
Plugin 'tomtom/tlib_vim'
Plugin 'garbas/vim-snipmate'

" Smart auto-indentation for Python
Plugin 'vim-scripts/indentpython.vim'
" Rich python syntax highlighting
Plugin 'kh3phr3n/python-syntax'

" 据说ycm包含jedi
" Plugin 'davidhalter/jedi-vim'

" Bundle 'Valloric/YouCompleteMe' or
Plugin 'Valloric/YouCompleteMe'


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

let g:syntastic_python_checkers = ['pylint']

" keyboard mapping
inoremap jk <Esc>
inoremap <Esc> <nop>

" syntax
syntax enable
syntax on

" PEP8
set textwidth=79  " lines longer than 79 columns will be broken
set shiftwidth=4  " operation >> indents 4 columns; << unindents 4 columns
set tabstop=4     " a hard TAB displays as 4 columns
set expandtab     " insert spaces when hitting TABs
set softtabstop=4 " insert/delete 4 spaces when hitting a TAB/BACKSPACE
set shiftround    " round indent to multiple of 'shiftwidth'
set autoindent    " align the new line indent with the previous line

" Point YCM to the Pipenv created virtualenv, if possible
" At first, get the output of 'pipenv --venv' command.
let pipenv_venv_path = system('pipenv --venv')
" The above system() call produces a non zero exit code whenever
" a proper virtual environment has not been found.
" So, second, we only point YCM to the virtual environment when
" the call to 'pipenv --venv' was successful.
" Remember, that 'pipenv --venv' only points to the root directory
" of the virtual environment, so we have to append a full path to
" the python executable.
if shell_error == 0
  let venv_path = substitute(pipenv_venv_path, '\n', '', '')
  let g:ycm_python_binary_path = venv_path . '/bin/python'
else
  let g:ycm_python_binary_path = 'python'
endif

# backspace can't delete other lines

[backspace don't work](http://cenalulu.github.io/linux/why-my-backspace-not-work-in-vim/)

# COMMAND + C/V

[paste compatible](https://stackoverflow.com/questions/5585129/pasting-code-into-terminal-window-into-vim-on-mac-os-x)
:set paste/nopaste

# 安装插件
PluginInstall
BundleInstall

# 卸载插件
PluginClean
BundleClean

# 更换ycm就不需要jedi了!
#########################################################
# 安装jedi支持
$ apt install python3-pip

# ImportError: cannot import name 'sysconfig'
sudo apt install python3-distutils

# 安装时可能出现ImportError: cannot import name 'main'
# 安装jedi时又需要改回from pip import main
# 真是不容易啊
$ sudo vim /usr/bin/pip3
from pip._internal import main

# Please install Jedi if you want to use jedi-vim.
$ pip3 install jedi
#########################################################

# 通过git不通过vundle安装ycm

$ cd ~/.vim/bundle/
$ git clone https://github.com/Valloric/YouCompleteMe.git
$ git submodule update --init --recursive
# 最后在~/.vimrc中添加ycm并且PluginInstall,执行之后才可以正常使用YouCompleteMe


$ sudo apt-get install build-essential cmake -y
$ sudo apt-get install python-dev python3-dev -y
$ cd ~/.vim/bundle/YouCompleteMe
$ ./install.py --clang-completer


## 还可以尝试通过apt安装ycm,还没试过
# https://askubuntu.com/questions/541737/how-to-use-vim-youcompleteme

$ sudo apt install vim-youcompleteme -y
$ sudo apt-get install vim-addon-manager -y
$ vam install youcompleteme

# 重启terminal即可使用

```

# ycm在pipenv环境下无法自动补全

[ycm在virtualenv和pipenv下的自动补全](https://www.linkedin.com/pulse/can-vim-detect-pipenv-environment-vagiz-duseev)

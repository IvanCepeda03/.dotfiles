set number relativenumber	" Show relative line numbers
set colorcolumn=81			" Highlight the column to mark the line width
set laststatus=0            " Hide the status bar in the last window
set smartindent				" Enable smart indentation based on syntax
set autoindent				" Mantain the indentation of the previous line
set expandtab				" Convert tabs into spaces
set smarttab				" Insert the appropiate number of spaces when Tab is pressed
set tabstop=4 				" Set the tab stops to 4
set shiftwidth=4			" Set the number of spaces for auto-indentation
set showtabline=4			" Always show the tabline even if it's only one file open
set formatoptions-=cro		" Disable automatic formatting of comments and other auto-setting
set hidden				    " Allow switching buffers without saving changes
set nowrap				    " Disable automatic line wrapping
set encoding=utf-8			" Set character encoding to UTF-8
set fileencoding=utf-8		" Set file encoding to UTF-8
set ruler				    " Show the current cursor position in the status line
set mouse=a				    " Enable using mouse in all modes
set cursorline				" Highlight the current cursor line
set splitbelow				" Open new split windows bellow the current one
set splitright				" Open new split windows to the right of the current one
set clipboard=unnamedplus	" Use the system clipboard for copy and paste operations
set background=dark			" Adjust color for dark barkgrounds themes
set autochdir				" Automaticaly change the working directory to the one on the current file
syntax enable 				" Enable syntax highlighting
filetype on		    	   	" Enable automatic file type detection
filetype indent on			" Enable automatic indentation based on type file
filetype plugin on			" Enable filetype-specific plugins

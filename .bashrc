#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='grep --color=auto'
alias tree='exa -T'
alias ls='exa --group-directories-first'
alias cat='bat --style=plain --paging=never'
alias dotfiles="git --git-dir $HOME/.dotfiles/ --work-tree $HOME"
alias vim='nvim'

# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
. ~/.git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\] '

# export PATH=$PATH:~/.scripts/


neofetch

# Created by `pipx` on 2024-09-13 00:38:22
export PATH="$PATH:/home/ivan/.local/bin"

" This file contains custom vim keybindings

" Alternative way to safe 'Ctrl+S'
noremap <C-s> :w<CR>
" Alternative way to quit 
noremap <C-q> :q<CR>

" Better tabbing
vnoremap < <gv
vnoremap > >gv

" Move selected line / block of text in visual mode
xnoremap K :move '<-2<CR>gv-gv
xnoremap J :move '>+1<CR>gv-gv

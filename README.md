# Problemas con las teclas Fn del teclado

Tengo un teclado NewSkill Serive V2 y no funcionaban las teclas Fn. 
Para solucionarlo he seguido las instruciones de esta 
[página](https://wiki.archlinux.org/title/Apple_Keyboard#Function_keys_do_not_work):

Modificar el archivo `/etc/modprobe.d/hid_apple.conf` añadiendo la siguiente línea
```bash
# /etc/modprobe.d/hid_apple.conf
options hid_apple fnmode=2
```

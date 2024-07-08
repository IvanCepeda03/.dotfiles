# Dotfiles & config
Este repositorio contiene una guía con los pasos necesarios para instalar mi entorno de escritorio en ArchLinux.
Te puedes basar en ella para configurar tu propio entorno de escritorio.
La rama main contiene el README con la guía de instalación y configuración básica del software que utilizo.
La rama desktop contiene los dotfiles de mi configuración para mi PC de sobremesa.
La rama laptop contiene los dotfiles de mi configuración para mi ordenador portátil.

# Indice
- [Instalación de Arch Linux](#instalación-de-arch-linux)
- [LightDM](#lightdm)
- [Qtile](#qtile)

# Instalación de Arch Linux

Esta guía empieza justo después de una instalación de Arch Linux siguiendo la 
**[Wiki de Arch](https://wiki.archlinux.org/title/Installation_guide_(Espa%C3%B1ol)).
Se deben de seguir todos los pasos hasta la sección 3.5 (incluida). Luego basta con seguir esta guía.

Instalar y habilitar NetworkManager para simplificar el uso de redes:
```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

Para poder cargar el sistema es importante instalar un gestor de arranque. El gestor de arranque 
escogido es `grub`. **Los pasos de instalación descritos suponen un sistema con un procesador de 
arquitectura x86_64-efi con una partición EFI montada /boot.**

```bash
pacman -S grub efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot
grub-mkconfig -o /boot/grub/grub.cfg
```

En caso de contar con más de un sistema operativo se debera instalar `os-prober` para detectar
otros SOs instalados en el sistema.

```bash
pacman -S os-prober
grub-mkconfig -o /boot/grub/grub.cfg # Necesario aunque se haya hecho previamente
```

Asignamos una contraseña a root:

```bash
passwd
```

Creamos nuestro usuario y lo añadimos a varios grupos

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

Para tener privilegios sudo necesitamos sudo:

```bash
pacman -S sudo
```
Tras la instalación de `sudo` hay que asignar los permisos a wheel editando el
archivo **`/etc/sudoers`** y descomentando la siguiente linea:

```bash
## Uncomment to allow members of group wheel to execute any command
%wheel ALL=(ALL) ALL
```

Finalmente salimos del entorno `chroot` con `exit` o `Ctrl+D`. Desmontamos la imagen ISO y reiniciamos del sistema.

```bash
exit
umount -R /mnt
reboot
```

# Primeros pasos

En caso de contar con una conexión a internet por medio de wifi, durante la instalación de ArchLinux probablemente hayas
usado [iwctl](https://wiki.archlinux.org/index.php/Iwd#iwctl).** Este programa ya no esta disponible a no ser que lo hayas 
instalado explícitamente. Sin embargo, previamente hemos instalado **[NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager)**.
que cuenta con la herramienta `nmcli`, la cual podemos usar para conectarnos a una red inalambrica:

```bash
# Lista las redes disponibles
nmcli device wifi list
# Conectarse a una red
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

Antes de nada recomiendo actualizar el sistema con:

```bash
sudo pacman -Syu
```

Si cuentas con un procesador AMD o Intel deberías instalar el 
**[microcode](https://wiki.archlinux.org/title/Microcode_(Espa%C3%B1ol))** 
correspondiente a tu tipo de procesador

```bash
# Microcode para procesadores AMD
sudo pacman -S amd-ucode
# Microcode para procesadores Intel
sudo pacman -S intel-ucode
```

Después de instalar `ucode` es necesario volver a cargar la configuración del grub
para activar la carga de la actualización de microcódigo:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

Para instalar paquetes del 
**[Arch Linux User Repository](https://wiki.archlinux.org/title/Arch_User_Repository_(Espa%C3%B1ol))
utilizaremos el **[AUR Helper](https://wiki.archlinux.org/title/AUR_helpers)** 
**[yay](https://github.com/Jguer/yay):

```bash
sudo pacman -S base-devel git # Dependencias necesarias para la instalación
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```

Antes de empezar con los gestores de ventana es necesario instalar
**[xorg](https://wiki.archlinux.org/index.php/Xorg).

```bash
sudo pacman -S xorg
```
# LightDM
Para poder iniciar sesión en el isstema con una interfaz gráfica es necesario instalar un display manager, 
en este caso instalaremos [LightDM](https://wiki.archlinux.org/index.php/LightDM). 
Para que lightdm funcione necesitamos un **[greeter](https://wiki.archlinux.org/index.php/LightDM#Greeter)**

```bash
sudo pacman -S lightdm lightdm-greeter
```

Tras la instalación hay que activar el servicio *lightdm*:

```bash
sudo systemctl enable lightdm
```

Ahora al reiniciar el sistema se nos abrira *lightdm*.
**Aún no lo hagas, pues falta instalar un gestor de ventanas.**

## Tema para LightDM
Podemos cambiar el tema de LightDM por uno más bonito. En mi caso he elegido el 
**[lightdm-webkit-theme-aether](https://aur.archlinux.org/packages/lightdm-webkit-theme-aether/)**. 
Para el cual necesitamos 
**[lightdm-webkit2-greeter](https://www.archlinux.org/packages/community/x86_64/lightdm-webkit2-greeter/)**

```bash
sudo pacman -S lightdm-webkit2-greeter
yay -S lightdm-webkit-theme-aether
```

Tras esto debemos cambiar la configuración de LightDM:

```ini
# /etc/lightdm/lightdm.conf
[Seat:*]
# ...
# Descomenta esta línea y pon este valor
greeter-session = lightdm-webkit2-greeter
# ...

# /etc/lightdm/lightdm-webkit2-greeter.conf
[greeter]
# ...
webkit_theme = lightdm-webkit-theme-aether
```

# Qtile

[Qtile](https://qtile.org/) es un gestor de ventanas personalizable. Para instalarlo:

```bash
sudo pacman -S qtile
```

Ahora si reiniciamos podremos abrir *qtile* desde *lightdm*.

Qtile usa por defecto la terminal `xterm` que tendremos que instalar para abrir una terminal.

```bash
pacman -S xterm
```

También puedes instalar otro emulador de terminal como `alacritty`:

```bash
pacman -S alacritty
```

Para cambiar el teclado a la distribución española:

```bash
setxkbmap es
```

La configuración de Qtile se encuentra en `~/.config/qtile/`. Puedes replicar mi configuración,
basarte en ella o incluso crear una configuración desde cero para tí. Te puedes guiar con 
**[Qtile docs](https://docs.qtile.org/en/stable/)**.

## Rofi

En mi configuración de Qtile uso Rofi el cual es un menú con el cual podemos abrir programas 
o seleccionar programas que ya esten abiertos. Además podemos crear nuestros propios menús de 
selección.

```bash
sudo pacman -S rofi
```

Para cambiar el tema de rofi:

```bash
rofi-theme-selector
```

Los temas de Rofi se encuentran en el directorio `/usr/share/rofi/themes/'. 
Es posible descargar temas o incluso crear los tuyos propios y moverlos a esa carpeta para aplicarlos.
En mi caso uso el tema [OneDark](https://github.com/davatorium/rofi-themes/blob/master/User%20Themes/onedark.rasi).

Rofi se puede configurar mediante el archivo `/.config/rofi/config.rasi/`. 
Para ver la documentación de Rofi: 

```bash
man rofi
```

#!/bin/bash
# Create by toey/2022
clear
#
update_upgrade() {
                echo -e "\n\e[97m       ∟ UPDATE && UPGRADE...\e[31m ▐\e[0m\n"
                pkg update -y && pkg upgrade -y
}
package() {
         clear
         echo -e "\n\e[97m       ∟ INSTALL PACKAGE FOR SCRIPT...\e[31m ▐\e[0m\n"
         pkg install python -y && pkg install python2 -y && pkg install zip -y && pkg install unzip -y && pip install -r requirements.txt
}
install_package_done() {
         clear
         echo -e "\n\e[97m       ∟ INSTALL PACKAGE DONE!\e[31m ▐\e[0m\n"
         sleep 3
}
update_upgrade
package
install_package_done

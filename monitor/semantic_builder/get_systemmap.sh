if [ -e /boot/vmlinux ]; then
  sudo nm /boot/vmlinux > System.map
  echo "success: use nm to get System.map!"
else
  echo "/boot/vmlinux doesn't exist! try to use /boot/System.map-$(uname -r)"
  if [ -e /boot/System.map-$(uname -r) ]; then
    sudo cp /boot/System.map-$(uname -r) ./System.map
    sudo chmod +r ./System.map
    echo "success: use /boot/System.map-$(uname -r) to get System.map!"
  else
    echo "System.map-$(uname -r) doesn't exist!"
  fi
fi
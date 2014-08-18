import urllib
import shutil
import os

urllib.urlretrieve('http://nimbus.howopenstack.org/'
                           'nimbus-installer.tar.gz',
                           '/tmp/nimbus-installer.tar.gz')
urllib.urlretrieve('https://raw.githubusercontent.com/rcbops/support-tools/'
                           'master/support-scripts/rax-nimbus-installer.sh',
                           '/tmp/rax-nimbus-installer.sh')
subprocess.call(["chmod", "+x", "/tmp/rax-nimbus-installer.sh"])
subprocess.call(["bash", "/tmp/rax-nimbus-installer.sh"])
shutil.rmtree("/tmp/nimbus-installer/")
os.remove("/tmp/nimbus-installer.tar.gz")
os.remove("/tmp/rax-nimbus-installer.sh")
os.remove("~/install.py")

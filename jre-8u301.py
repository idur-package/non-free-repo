
Name="jre-8u301"
Version="1"
License="https://java.com/otnlicense"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"

idurDepends= ["idur-pkg"]
Conflict= ["jre-8u301"]
Description="""
jre 8

"""

Install64="""
idur-pkg tmp jre
cd /tmp/idur-jre-tmp/
idur-pkg download https://github.com/idur-package/non-free-repo/releases/download/binaries/jre-8u301-linux-x64.tar.gz
tar -xvzf jre-8u301-linux-x64.tar.gz
cp -r jre1.8.0_301/ /opt/
idur-pkg download https://github.com/idur-package/non-free-repo/releases/download/binaries/jre-8u301
cp jre-8u301 /usr/bin/jre-8u301
chmod a+x /usr/bin/jre-8u301
idur-pkg rm-tmp

"""

Remove="""
idur-pkg rm /usr/bin/jre-8u301
idur-pkg rm /opt/jre1.8.0_301/
"""

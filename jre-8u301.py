
Name="jre-8u301"
Version="1"


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
echo "#!/usr/bin/bash
if [ ! -z $1]
then
	cd /opt/jre1.8.0_301/
	if [ $1 = "-l" ]
	then
		ls bin/
	else
		./$1
	fi 
else
	echo Use:
	echo jre-8u301 \"command\"
	echo or:
	echo jre-8u301 -l
fi" > /usr/bin/jre-8u301
chmod a+x /usr/bin/jre-8u301

"""

Remove="""
idur-pkg rm /usr/bin/jre-8u301
idur-pkg rm /opt/jre1.8.0_301/
"""

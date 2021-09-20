
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
echo "#!/usr/bin/bash
if [ ! -z $1 ]
then
	cd /opt/jre1.8.0_301/
	if [ $1 = '-l' ]
	then
		ls bin/
	elif [ $1 = '-r' ]
	then
		if [ ! -z $2 ]
		then
			./bin/java -jar $2
		else
			echo 'jre-8u301 -r <.jar>'
		fi
	else
		./bin/$1
	fi 
else
	echo 'jre-8u301
Use:
	jre-8u301 command
Other:
	jre-8u301 -l            list commands
	jre-8u301 -r <.jar>     run .jar'
fi" > /usr/bin/jre-8u301
chmod a+x /usr/bin/jre-8u301

"""

Remove="""
idur-pkg rm /usr/bin/jre-8u301
idur-pkg rm /opt/jre1.8.0_301/
"""

# LANGSCIID=${PWD##*/}
LANGSCIID=$1
echo LangSci ID is $LANGSCIID
PHIDtmp=`curl -s "https://paperhive.org/api/document-items/by-document/external?type=langsci&id="$LANGSCIID |jq '.["documentItems"][0]["id"]'`
PHID=${PHIDtmp:1:-1}
echo Paperhive ID is $PHID
curl -s "https://paperhive.org/api/discussions?documentItem=$PHID"| jq  ".discussions[] | .author.displayName"|sort -u 
if [[ $# -ne 1 ]]
then
    echo 1>&2 "Usage: $0 \"commit message\""
    exit 3
fi

MODIFIED="$(git status | grep modified | sed 's/\(.*modified:\s*\)//')"
ADDED="$(git status | grep "new file" | sed 's/\(.*new file:\s*\)//')"

git add *
git commit -m "$1"
git push origin development

git checkout master
git checkout development .

while read -r line; do
    if [[ "$line" == *.md ]] 
    then
      python githubify.py "$line"  
      git add "$line"
    fi
done <<< "$MODIFIED"

while read -r line; do
    if [[ "$line" == *.md ]] 
    then
      python githubify.py "$line"  
      git add "$line"
    fi
done <<< "$ADDED"

git commit -m "$1"
git push origin master

git checkout development
MODIFIED="$(git status | grep modified | sed 's/\(.*modified:\s*\)//')"
ADDED="$(git status | grep "new file" | sed 's/\(.*new file:\s*\)//')"

git add *
git commit -m "$1"
git push origin development

git checkout master

while read -r line; do
    git checkout development "$line"
    if [[ "$line" == *.md ]] 
    then
      python githubify.py "$line"  
    fi
    git add "$line"
done <<< "$MODIFIED"

while read -r line; do
    git checkout development "$line"
    if [[ "$line" == *.md ]] 
    then
      python githubify.py "$line"  
    fi
    git add "$line"
done <<< "$ADDED"

git commit -m "$1"
git push origin master

git checkout development
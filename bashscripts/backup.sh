read -p "Welcome, Master. Enter file for backup: " files
mkdir -p $HOME/backup
dir="$HOME/backup"
for file in $files
do
if [ -f "$file" ]; then
cp "$file" "$dir/"
echo "File backed up: $file"
else echo "$file does not exist"
fi
done


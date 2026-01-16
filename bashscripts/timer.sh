read -p "Set Timer (sec): " num
while [ "$num" -gt 0 ]; do
clear
echo "$num"
((num--))
sleep 1
done
echo "Time's Up!"

attempts=3
crusr="prem"
crpass="eldenlord"
while [ "$attempts" -ne "0" ]; do
read -p "Enter user name: " usr
read -s -p  "Enter password: " pass
echo
if [ "$usr" = "$crusr" ] && [ "$pass" = "$crpass" ]; then
echo "Welcome, Master."; exit 0
else echo "Invalid credentials!"
fi
((attempts--))
echo "You have $attempts attempts left."
done
echo "Invalid credentials. Access denied."

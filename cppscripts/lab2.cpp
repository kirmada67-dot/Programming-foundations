#include <iostream>
using namespace std;

class person{
	char name[30];
	int age;
	int prn;
	char address[30];

	public:
		void getdata(void);
                void display(void);
};

void person :: getdata(void){
	cout << "Enter name: ";
	cin >> name;
	cout << "Enter age: ";
	cin >> age;
	cout << "Enter PRN: ";
	cin >> prn;
	cout << "Enter Address: ";
	cin >> address;
}

void person :: display(void){
	cout << "\nName: " << name;
	cout << "\nAge: " << age;
	cout << "\nPRN: " << prn;
	cout << "\nAddress: " << address;
}


int main(){
	person  p[20];
	int n;
	cout << "\nEnter total number of students: ";
	cin >> n;

	//person students[n];
	for (int i = 0; i < n; i++){
		//person pi;
		p[i].getdata();
		//students[i] = pi;
	}

	for (int i = 0; i < n; i++){
		p[i].display();
	}

	return 0;
}

#include <iostream>
#include <string>

int penguins[3]
ifstream myfile;
myfile.open ("input.txt");
getline(myfile,line)
while ( getline (myfile,line) )
{
	if(line[0] == "E")
		penguins[0]++;
	else if (line[0] == "M")
		penguins[1]++;
	else
		penguins[2]++;
}
myfile.close();


ofstream outputFile;
outputFile.open("output.txt");
outputString = "Emperor Penguin"
maxValue = 0;
for(int i =1;i<3;i++) {
	if(penguins[i]>maxValue){
		if(i == 1)
			outputString = "Macaroni Penguin"
		else
			outputString = "Little Penguin"
		maxValue = penguins[i];
	}
}

outputFile << outputString
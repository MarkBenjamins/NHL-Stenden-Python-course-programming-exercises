1. Stel een groepje van max * peronsone samen en vraag aan de docent, om toestemming, een groeps nummer en om samenen met de rechten voor de github page die gekoppeld is aan de Ci van de drone. 
2. Ga naar de github page https://github.com/SydneyM123/p-tff_ci_public
3. Clone the repository (maak hier een manual for)
4. Maak een python file aan met Groep(nummer).py (bijvoorbeeld groep1.py)
Het is van belang dat de file een Py file is anders zal de file niet worden uitgevoerd. 
Het is ook van beelang dat de file uniek is, er kunnen geen twee files bestaan in de repository met dezelfde naam, 
denk hierbij aan Group_1 in de main en in de folder groep1 staat nog en file group_1 dan zal de file niet worden uitgevoerd.

5. Voeg deze file toe aan de repository en push deze naar server.

Zodra de code wordt gepushed zal de geschreven code in de wachtrij komen voor en zal de code worden uitgevoerd op de drone.

indien the code niet uitgevoerd wordt neem dan contoact op met de docent.


notes (anders dan simulatie):
- manual for the drone commands
- connection manual ip/poort

# Executing code on the Tello drone

In this manual we will describe how you can execute your code on the drone. 

## Assemble the groups

Before you can work with the drone, you have to assemble your groups:

- Form a group with around 4 á 5 other students.

- Ask the corresponding teacher for permission to receive a groups number.

- Receive the rights to access the GitHub page where you can push code to the drone.

  

## Setup your file

Each group gets one file to execute code on the drone. In order to acquire the group file, follow the instructions below:

1. Visit [this]( [https://github.com/SydneyM123/p-tff_ci_public](https://github.com/SydneyM123/p-tff_ci_public)) GitHub page.

2. Clone the repository.

3. Create a new Python file called group + your specific groups number. (for example group1.py)

   *DISCLAIMER: Make sure your file name is unique within the entire repository.*

4. Commit your changes and push the file to the repository.


Now your code is ready to control the Tello drone, it will be executed within three minutes.

## Code execution

The pushed code will be executed automatically. Every 3 minutes the system will scan the repository for changed files. The system will then detect those changed files and place them in the system queue. The system queue is continuously executed through the Jenkins pipeline. The file's in front of the system queue will be run and the code will be executed onto the drone.

*DISCLAIMER: If your code is not executed, please contact the teacher.*




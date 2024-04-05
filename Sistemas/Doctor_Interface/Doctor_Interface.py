'''
    The program in the file patient_data.py contains a Dictionary named patients which
contains information about several patients. Each patient is represented as a key-value pair, where
the key is a patient ID (e.g., 'P12345'), and the corresponding value is another dictionary
containing the patient's details.
Imagine you are writing a program for a doctor to query his patient's information through the
command line.
The program will ask the doctor for a patient ID. Then given this ID, print the following information:
• Patients name, age and gender.
• The patient's diagnosis.
• Medications and allergies and the number of Medications and number of allergies.
'''

patients = {
        "P12345": {
            "name": "John Doe",
            "age": 35,
            "gender": "Male",
            "diagnosis": "Hypertension",
            "medications": ["Lisinopril", "Hydrochlorothiazide"],
            "allergies": ["Penicillin"],
            "blood_pressure_checks": [[130, 90],[146, 99],[138, 88],[128, 82]],
            "last_checkup_date": "2022-05-20",
            "next_appointment_date": "2023-11-15"
        },
        "P67890": {
            "name": "Jane Smith",
            "age": 41,
            "gender": "Female",
            "diagnosis": "Diabetes",
            "medications": ["Semaglutide", "Insulin"],
            "blood_pressure_checks": [[119, 79],[122, 77],[120, 81],[118, 85]],
            "allergies": ["Metformin"],
            "last_checkup_date": "2023-04-20",
            "next_appointment_date": "No-Date"
        },
        "P24680": {
            "name": "Robert Johnson",
            "age": 28,
            "gender": "Male",
            "diagnosis": "Asthma",
            "medications": ["Albuterol", "Prednisone"],
            "allergies": ["Peanuts"],
            "blood_pressure_checks": [[121, 80],[122, 78],[125, 80],[119, 83]],
            "last_checkup_date": "2022-06-08",
            "next_appointment_date": "2023-12-10"
        },
        "P18945": {
            "name": "Alice Davis",
            "age": 55,
            "gender": "Female",
            "diagnosis": "Diabetes",
            "medications": ["Metformin", "Insulin"],
            "allergies": ["Penicillin"],
            "blood_pressure_checks": [[122, 81],[122, 78],[123, 78],[119, 81]],
            "last_checkup_date": "2023-04-15",
            "next_appointment_date": "No-Date"
        },
        "P69918": {
            "name": "Michael Smith",
            "age": 42,
            "gender": "Male",
            "diagnosis": ["Hypertension","Celiac Disease"],
            "medications": ["Lisinopril", "Hydrochlorothiazide"],
            "allergies": [],
            "blood_pressure_checks": [[175, 95],[155, 89],[145, 100]],
            "last_checkup_date": "2023-05-20",
            "next_appointment_date": "2023-11-20"
        },
        "P13579": {
            "name": "Emily Johnson",
            "age": 33,
            "gender": "Female",
            "diagnosis": "Migraine",
            "medications": ["Sumatriptan", "Ibuprofen"],
            "allergies": ["Codeine"],
            "blood_pressure_checks": [[100, 72],[103, 76],[110, 69],[115, 68],[103, 76]],
            "last_checkup_date": "2023-01-05",
            "next_appointment_date": "2023-12-05"
        }
    }
from datetime import datetime

pat = input("\033[1mWould you like to consult the patient's situation?: "'\033[37m').upper().strip()
print("")
while pat == "YES":
    n = input('Enter patient ID: ').upper().strip()
    if n in patients.keys():
        print(f'Name: {patients[n]["name"]}')
        print(f'Age: {patients[n]["age"]}')
        print(f'Gender: {patients[n]["gender"]}')
        print(f'Diagnosis: {patients[n]["diagnosis"]}')
        print(f'Number of medications: {len(patients[n]["medications"])}')
        print(f'Medications: {patients[n]["medications"]}')
        print(f'Number of allergies: {len(patients[n]["allergies"])}')
        print(f'Allergies: {patients[n]["allergies"]}')

        q = len(patients[n]['blood_pressure_checks'])
        i = 0
        high = []
        low = []

        while i < q:
            high.append(patients[n]["blood_pressure_checks"][i][0])
            low.append(patients[n]["blood_pressure_checks"][i][1])
            i = i + 1

        media_high = sum(high) / q
        media_low = sum(low) / q
        print('Systolic-average/Diastolic-average: {:.2f}/{:.2f}'.format(media_high, media_low))

        if media_high > 125 and media_low > 85:
            print('The patients average blood pressure is:''\033[31m HIGH''\033[37m')
        elif 115 < media_high < 125 and 75 < media_low < 85:
            print('The patients average blood pressure is:''\033[32m NORMAL''\033[37m')
        else:
            print('The patients average blood pressure is:''\033[33m LOW''\033[37m')

        date1 = datetime.strptime(patients[n]['last_checkup_date'], '%Y-%m-%d')
        try:
            date2 = datetime.strptime(patients[n]['next_appointment_date'], '%Y-%m-%d')
            time_difference = (date2 - date1).days
            print(f'The difference between the patients last checkup and next appointment is: {time_difference} days')
        except ValueError:
            print('The patient does not have an upcoming appointment!')
        print("")

        pm = input(str("Add medication for the patient?:")).upper().strip()
        print("")
        while pm == 'YES':
            nm = input(str('Which medicine to add?:')).capitalize().strip()

            if nm in patients[n]['medications']:
                print("\033[36mThis item is already on the patient's medication list"'\033[37m')
            elif nm in patients[n]['allergies']:
                print('\033[31mThe patient is allergic to this medicine!''\033[37m')
            else:
                patients[n]['medications'].append(nm)
            pm = input(str('Add another medicines?')).upper().strip()

        print("")
        print(f'This is patient {patients[n]["name"]}s medication list')
        print(patients[n]['medications'])
        print("")

        rm = input(str('Would you like to remove an item?:')).upper().strip()
        while rm == 'YES':
            mr = input(str('Remove which medication?:')).capitalize().strip()

            if mr in patients[n]['medications']:
                patients[n]['medications'].remove(mr)
            else:
                print("Medication does not exist in the patient's list!")

            print(f'This is patient {patients[n]["name"]}s medication list')
            print(patients[n]['medications'])
            rm = input(str('Continue removing?:')).upper().strip()

        print("")
        pat = input("See another patient?: ").upper().strip()
        print("")
    else:
        print("ID not registered!")
        pat = input("Try Again?: ").upper().strip()
        print("")
print("\033[1mConsultation Completed")



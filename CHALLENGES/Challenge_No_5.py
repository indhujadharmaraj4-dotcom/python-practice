candidate_name = "Indhuja"
age = 23
education = "Diploma"
experience = 4
communication_skill = True

age_eligible = age>=18
education_eligible = education=="Diploma"
experience_or_communication=(experience>=2 or communication_skill==True)
print("Candidate Name:", candidate_name)
print("Age Eligible:",age_eligible)
print("Experience Or Communication:",experience_or_communication)
print("Communication Not Available:",not communication_skill)

#Print the value of key ‘history’ from the below dict



sampleDict = {
  "class": {
    "student": {
      "name": "Mike",
      "marks": {
        "physics": 70,
        "history": 80
      }
    }
  }
}

a = sampleDict["class"]["student"]["marks"]["history"]
print(a)

#output: 80
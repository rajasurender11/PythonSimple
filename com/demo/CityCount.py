
#"CHN|20" --> split("|") --> ["CHN","20"]  [20,50]

data_str =["CHN|20",
           "BNG|40",
           "CHN|50",
           "BNG|90",
           "MUM|40"]
chn_sum=0
bng_sum=0
mum_sum=0

def addCHN(data):
    global chn_sum
    result_of_split = data.split("|")
    num = int(result_of_split[1])
    chn_sum =chn_sum+num


def addBNG(data):
    global bng_sum
    result_of_split = data.split("|")
    num = int(result_of_split[1])
    bng_sum =bng_sum+num

def addMUM(data):
    global mum_sum
    result_of_split = data.split("|")
    num = int(result_of_split[1])
    mum_sum =mum_sum+num

def addOthers(data):
    result_of_split = data.split("|")
    num = int(result_of_split[1])

for i in data_str:
    print(i)
    if(i.startswith("CHN")):

        addCHN(i)
    elif(i.startswith("BNG")):
        addBNG(i)
    elif(i.startswith("MUM")):
        addMUM(i)
    else:
        addOthers(i)

print(f"sum of CHN {chn_sum}")
print(f"sum of BNG {bng_sum}")
print(f"sum of MUM {mum_sum}")

s1 = "100~surender~raja|chennai"

split_s1 = s1.split(",")
print(split_s1)

s2 ="SurenderRaja"

print(s2[2:6])
print(s2[2:])
print(s2[:6])

s3 = '2022-01-30'
print(s3[0:4])
print(s3[:4])
print(s3.split("-")[0])

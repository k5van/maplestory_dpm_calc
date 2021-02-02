def loadDPM(filename:str):
    DPMlist=[]
    with open(filename, "r") as DPMfile:
            
        entries=[[str(val) for val in line.split() ] for line in DPMfile]

    for entry in entries:
        DPMlist.append([str(entry[0]),float(entry[1])])
    DPMfile.close()
    return DPMlist

def storeDPM(filename:str, DPMlist:list):
    with open(filename,"a") as DPMfile:
        DPMfile.write("\n")
        for i in range(len(DPMlist)):
            DPMfile.write(str(i+1)+" "+str(DPMlist[i][0])+"     "+str(DPMlist[i][1])+"\n")


DPMlist=loadDPM("dpm_output.txt")
DPMlist.sort(key=lambda x: x[1] ,reverse=True)
storeDPM("results/3600secDPM20jag.txt",DPMlist)
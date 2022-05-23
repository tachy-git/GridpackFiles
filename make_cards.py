import os
import sys

generator = sys.argv[1] #MadGraph5_aMCatNLO #Powheg
path = sys.argv[2] #Cards/MadGraph5_aMCatNLO/DYJets/DYJets_0J_amcatnloFXFX-pythia8

if not os.path.exists(path):
    os.system("mkdir -p " + path)
else:
    sys.exit("error : " + path + " already exists")

process = path.split("/")[3]

skeleton_path = "Cards/"+generator+"/skeleton/"

if (generator == "MadGraph5_aMCatNLO"):

    os.system("cp " + skeleton_path + "/skeleton.json " + path + "/" + process + ".json")
    os.system("cp " + skeleton_path + "/skeleton_madspin_card.dat " + path + "/" + process + "_madspin_card.dat")
    os.system("cp " + skeleton_path + "/skeleton_proc_card.dat " + path + "/" + process + "_proc_card.dat")
    os.system("sed -i 's|__process__|" + process + "|g' " + path + "/" + process + "_proc_card.dat")

if (generator == "Powheg"):

    pass
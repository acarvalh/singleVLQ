#!/bin/bash

scriptname=`basename $0`
EXPECTED_ARGS=3
if [ $# -ne $EXPECTED_ARGS ]
then
echo "Usage: $scriptname processName massInputFile customizationInputFile"
echo "Example: ./$scriptname tW_tW_x53x53 mass_points.txt tW_tW_x53x53_RH_customizecards.dat"
exit 1
fi

# name of the run
name=$1

# mass input files
massInput=$2

## customercards
custom=$3


export PRODHOME=$GridPackHome/genproductions/bin/MadGraph5_aMCatNLO/cards
CARDSDIR=${PRODHOME}/pairVLQ

########################
#Locating the proc card#
########################
if [ ! -e $CARDSDIR/${name}_madspin/${name}_madspin_proc_card.dat ]; then
    echo $CARDSDIR/${name}_madspin/${name}_madspin_proc_card.dat " does not exist!"
    exit 1;
fi


########################
#Locating the customization 
########################
if [ ! -e $CARDSDIR/${name}_madspin/$custom ]; then
    echo $CARDSDIR/${name}_madspin/$custom " does not exist!"
    exit 1;
fi


run=run_card.dat
########################
#Locating the run card
########################
if [ ! -e $CARDSDIR/$run ]; then
    echo $CARDSDIR/$run " does not exist!"
    exit 1;
fi

########################
#Run the code-generation step to create the process directory
########################
topdir=$CARDSDIR/${name}_madspin
#mkdir $topdir
iteration=0
lastfile=`cat $massInput | wc -l`
echo "There are "$lastfile" mass points"

while [ $iteration -lt $lastfile ]; 
do
  iteration=$(( iteration + 1 ))
  mass=(`head -n $iteration $massInput  | tail -1`)
  echo "Producing cards for X mass = "$mass" GeV"
  newname=${name}_madspin_narrow_RH_M${mass}
  mkdir -p $topdir/$newname
  dir=$CARDSDIR/${name}_madspin/$newname
  sed -e 's/'${name}_madspin'/'${newname}' -nojpeg\n/g' $topdir/${name}_madspin_proc_card.dat > $dir/${newname}_proc_card.dat
  sed 's/MASS/'$mass'/g' $topdir/${custom} > $dir/${newname}_customizecards.dat
  cp $CARDSDIR/run_card.dat $dir/${newname}_run_card.dat
  cp $CARDSDIR/${name}_madspin/madspin_card.dat $dir/${newname}_madspin_card.dat
done

# singleVLQ
Cards for generation of all possible channels of single VLQ production in LHC

The subfoldes contain:

- MG process card with the VLQ candidate that produces that final state

- MG param card for narrow (1 MeV) width with LH coupling of the relevant VLQ candidate
  (to be done for masses mx = 500, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1800)
- MG param card for narrow (1 MeV) width with RH coupling of therelevant VLQ candidate
  (only when relevant, to be done for mx = 1 TeV and 1.8 TeV only)

- MG param cards for (30%)*mx natural width for two masses with LH coupling of the relevant VLQ candidate
  (to be done for massesmx = 700 GeV and mx = 1.8 TeV)
- MG param cards for (30%)*mx natural width for two masses with RH coupling of the relevant VLQ candidate
  (only when relevant, to be done for massesmx = 700 GeV and mx = 1.8 TeV)

- MG reweigt cards to the last two bullets
  (still to be written)

The model uploaded allow free variation of VLQ total width. 


tecnicalities:

a) We are decaying up to W's and Z's final states inclusively, it is in 4F scheeme and contain also all the subdominant diagrams. 
===> the  generation of each lhe itself will take some time, it is better to do in GRID! specially the ones with t-associated ones.

b) to make the process like tZ_t to be all inclusive in W and Z but not all inclusive in the T.P., instead of change syntax I turn off the T_Wt coupling in param_card. I takes more generation time, but well it is the way.

c)
>Xandra, since we have decided to move to Andrea's model, can you confirm that producing 
>LHE files with Andrea's model with Madgraph5_aMC@NLO is ok.      
yes, is ok.

d) I still need to write the reweigh cards

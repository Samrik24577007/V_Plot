import sys
from collections import defaultdict
DS_c=defaultdict(lambda:defaultdict(lambda:0))

#2	chr1	90919	91937	chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA	16.2951	+	chr1	90838	91006	IH02_00.pairs@15152	168	+
#2	chr1	90919	91937	chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA	16.2951	+	chr1	90846	90998	IH02_04.pairs@4163	152	+
#2	chr1	90919	91937	chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA	16.2951	+	chr1	90851	91000	IH02_04.pairs@4164	149	+
#2	chr1	90919	91937	chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA	16.2951	+	chr1	90850	91014	IH02_00.pairs@15153	164	+

for line in sys.stdin:
	l=line.strip().split("\t")
	a=(float(l[9])+float(l[8]))/2 - (float(l[3])+float(l[2]))/2
	b=(float(l[3])-float(l[2]))/2
	dist=a*500/b
	length=float(l[11])*500/b
	
	
	DS_c[dist][length]+=1
sum=0
for dist in DS_c:
	for length in DS_c[dist]:
		sum+=DS_c[dist][length]
 
for dist in DS_c:
	for length in DS_c[dist]:

		print(dist,"\t",length,"\t",DS_c[dist][length]/sum)
	
	

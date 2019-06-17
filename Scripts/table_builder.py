star = []
salmon = []

starcount = open('star_counts.tab','w')
stardata = open('star_data.tab','w')
salmoncount = open('salmon_counts.tab','w')
salmondata = open('salmon_data.tab','w')

stardata.write('\tcondition\n')
salmondata.write('\tcondition\n')

with open('STAR2DESEQ.txt') as infile:
    for lines in infile:
        star.append(lines.split('\t')[0])
        stardata.write(lines.split('\t')[1].rstrip() + '\t' + lines.split('\t')[1][:-2] + '\n')
        starcount.write('\t' + lines.split('\t')[1].rstrip())
with open('Salmon2DESEQ.txt') as infile:
    for lines in infile:
        salmon.append(lines.split('\t')[0])
        salmondata.write(lines.split('\t')[1].rstrip() + '\t' + lines.split('\t')[1][:-2] + '\n')
        salmoncount.write('\t' + lines.split('\t')[1].rstrip())
        
stardata.close()
salmondata.close()

starcount.write('\n')
salmoncount.write('\n')

stargenes = {}
salmongenes = {}

for s in star:
    with open(s) as infile:
        for lines in infile:
            if lines.startswith('N_'):
                continue
            else:
                geneid = lines.split('\t')[0]
                rawcount = lines.split('\t')[1]
                try:
                    stargenes[geneid].append(rawcount)
                except:
                    stargenes[geneid] = [rawcount]
                    
for s in salmon:
    with open(s) as infile:
        next(infile)
        for lines in infile:
            transcript = lines.split('\t')[0]
            rawcount = str(round(float(lines.split('\t')[-1].rstrip())))
            try:
                salmongenes[transcript].append(rawcount)
            except:
                salmongenes[transcript] = [rawcount]
                
for s in stargenes:
    starcount.write(s + '\t' + '\t'.join(stargenes[s]) + '\n')
for s in salmongenes:
    salmoncount.write(s + '\t' + '\t'.join(salmongenes[s]) + '\n')
    
starcount.close()
salmoncount.close()     
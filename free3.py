import re
a="""The Nile (Arabic: النيل‎, romanized: an-Nīl, Arabic pronunciation: [an'niːl], Bohairic Coptic: ⲫⲓⲁⲣⲟ Pronounced [pʰjaˈro][4], Luganda: Kiira Ganda pronunciation: [ki:ra], Nobiin: Áman Dawū[5]) is a major north-flowing river in northeastern Africa. The longest river in Africa, it has historically been considered the longest river in the world,[6][7] though this has been contested by research suggesting that the Amazon River is slightly longer.[8][9] The Nile is about 6,650 km (4,130 mi)[n
1] long and its drainage basin covers eleven countries: Tanzania, Uganda, Rwanda, Burundi, the Democratic Republic of the Congo, Kenya, Ethiopia, Eritrea, South Sudan, Republic of the Sudan, and Egypt.[11] In particular, the Nile is the primary water source of Egypt and Sudan.[12]
The Nile has two major tributaries – the White Nile and the Blue Nile. The White Nile is considered to be the headwaters and primary stream of the Nile itself. The Blue Nile, however, is the source of most of the water, containing 80% of the water and silt. The White Nile is longer and rises in the Great Lakes region of central Africa, with the most distant source still undetermined but located in either Rwanda or Burundi. It flows north through Tanzania, Lake Victoria, Uganda and South Sudan.
The Blue Nile begins at Lake Tana in Ethiopia[13] and flows into Sudan from the southeast. The two rivers meet just north of the Sudanese capital of Khartoum.[14]
The northern section of the river flows north almost entirely through the Sudanese desert to Egypt, then ends in a large delta and flows into the Mediterranean Sea. Egyptian civilization and Sudanese kingdoms have depended on the river since ancient times. Most of the population and cities of Egypt lie along those parts of the Nile valley north of Aswan, and nearly all the cultural and historical sites of Ancient Egypt are found along river banks."""
sentence="hello i am not hostile"
#pattern=re.compile(r'hello')
#matches=pattern.finditer(sentence)
#for i in matches:
    #print(i)
txt = "aman.hebbale@gmail.com"
x = re.search("am",txt)

print("The first white-space character is located in position:", x.span())

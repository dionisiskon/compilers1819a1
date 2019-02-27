"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	return c	# anything else
	

def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 's0': { '0' : 's1','1' : 's1', '2' : 's1' , '3' : 's2' },
       			's1': { '0' : 's7' ,'1':'s7','2':'s7','3' : 's7','4' : 's7','5' : 's7','6' : 's7','7' : 's7','8' : 's7','9' : 's7' },
       			's2': { '0' : 's3','1' : 's3','2' : 's3','3' : 's3','4' : 's3','5' : 's4' },
       			's3': {'0' : 's6', '1':'s6','2':'s6','3' : 's6', '4' : 's6','5' : 's6','6' : 's6','7' : 's6','8' : 's6','9' : 's6' },
				's4': {'0' : 's5'},
				's5': {'0' : 's9','1':'s9','2':'s9','3' : 's9','4' : 's9','5' : 's9','6' : 's9','7' : 's9','8' : 's9','9' : 's9'},
				's6': {'0' : 's9','1':'s9','2':'s9','3' : 's9','4' : 's9','5' : 's9','6' : 's9','7' : 's9','8' : 's9','9' : 's9'},
				's7': {'0' : 's8','1':'s8','2':'s8','3' : 's8','4' : 's8','5' : 's8','6' : 's8','7' : 's8','8' : 's8','9' : 's8'},
				's8': {'0' : 's9','1':'s9','2':'s9','3' : 's9','4' : 's9','5' : 's9','6' : 's9','7' : 's9','8' : 's9','9' : 's9'},
				's9': {'0' : 's10','1':'s10','2':'s10','3' : 's10','4' : 's10','5' : 's10','6' : 's10','7' : 's10','8' : 's10','9' : 's10'},
				's10' : {'K' : 's11','M' : 's13','G' : 's15'},
				's11' : {'T' : 's12'},
				's13' : {'P' : 's14'},
				's14' : {'S' : 's12'},
				's15' : {'0' : 's16','1':'s16','2':'s16','3' : 's16','4' : 's16','5' : 's16','6' : 's16','7' : 's16','8' : 's16','9' : 's16'},
				's16' : {'0' : 's17','1':'s17','2':'s17','3' : 's17','4' : 's17','5' : 's17','6' : 's17','7' : 's17','8' : 's17','9' : 's17'},
				's17' : {'K' : 's18','M' : 's19'},
				's18' : {'T' : 's12'},
				's19' : {'P' : 's20'},
				's20' : {'S' : 's12'}      
     		  } 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = {
	 's12' : 'WIND_TOKEN'
}


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	

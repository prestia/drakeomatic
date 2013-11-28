from db import Db
from gen import Generator
from parse import Parser
from sql import Sql
from rnd import Rnd
import sys
import sqlite3
import codecs
from keys import *
from twitter import *

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '

def main():
	args = sys.argv
	usage = 'Usage: %s (parse <name> <depth> <path to txt file>|gen <name> <count>)' % (args[0], )

	if (len(args) < 3):
		raise ValueError(usage)

	mode  = args[1]
	name  = args[2]
	
	if mode == 'parse':
		if (len(args) != 5):
			raise ValueError(usage)
		
		depth = int(args[3])
		file_name = args[4]
		
		db = Db(sqlite3.connect(name + '.db'), Sql())
		db.setup(depth)
		
		txt = codecs.open(file_name, 'r', 'utf-8').read()
		Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(txt)
	
	elif mode == 'gen':
		count = int(args[3])
		db = Db(sqlite3.connect(name + '.db'), Sql())
		generator = Generator(name, db, Rnd())
		for i in range(0, count):
			output = generator.generate(WORD_SEPARATOR) + '.'
			# START code to lengthen tweets
			if len(output) < 100:
				output2 = output
				output = generator.generate(WORD_SEPARATOR) + '. ' + output
				if len(output) >140:
					output = output2
			# END code to lengthen tweets
			while len(output) > 140:
				output = generator.generate(WORD_SEPARATOR) + '.'
				print output
			print output
			tweet_output(output)
	
	else:
		raise ValueError(usage)

def tweet_output(output):
    t = Twitter(auth=OAuth(key_access_token_key, key_access_token_secret, key_consumer_key, key_consumer_secret))

    t.statuses.update(status=output)

if __name__ == "__main__":
    main()


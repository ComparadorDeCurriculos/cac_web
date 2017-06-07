class stoplist:

	def __init__(self, StopListFile):
		self.words = [];
		self.file = open(StopListFile);

		#gets file end
		self.file.seek(0,2); #2 = SEEK_END
		end = self.file.tell();
		self.file.seek(0,0);

		i = 0;
		#reads every line of the file
		while(self.file.tell() != end):
			#fetches each line
			text = self.file.readline().rstrip();
			#appends it to a vector of words
			self.words.append(text);
			++i;

		#creates a set of words
		self.words = set(self.words);

	def check(self, word):
		return word in self.words;

class wordnet:

	def __init__(self,wordnetFilename):

		import string;
		import Stemmer;

		stemmer = Stemmer.Stemmer('portuguese');

		#maps words to their synsets
		self.words = {};

		#list of synsets
		#pos 0 in synsets is empty (None)
		self.synsets = [None];

		#creating translator used to remove punctuations
		punc = string.punctuation.replace('-','');
		translator = str.maketrans({key:None for key in punc});

		self.file = open(wordnetFilename);

		for line in self.file:
			#removing punctuation
			bfr = line;
			bfr = bfr.rstrip().translate(translator);

			#splitting
			bfr = bfr.split(' ');

			bfr2 = [];

			#stemming text
			for word in bfr:
				bfr2.append(stemmer.stemWord(word));
			bfr = bfr2;

			#checking if the last split should be discarded
			try:
				float(bfr[len(bfr) - 1]);
				del bfr[-1];
			except ValueError:
				pass

			#removing the synset class
			bfr.pop(1);

			synsetNo = bfr.pop(0);

			#building synsets list
			self.synsets.append(bfr);

			#building words map
			for word in bfr:
				if word in self.words:
					self.words[word].append(synsetNo);
				else:
					self.words[word] = [synsetNo];

	def checkSynonym(self, word_a, word_b):
		try:
			synsets = self.words[word_a]
		except KeyError:
			return False;

		for synset in synsets:
			for word in self.synsets[int(synset)]:
				if word == word_b:
					return True;

		return False;


class wordEmbedding:
	
	import Stemmer

	#generates required stopList, open docs
	stopList = stoplist('cac_app/nucleos/stoplist_portugues.txt');
	wordNet = wordnet('cac_app/nucleos/base_tep2.txt');
	stemmer = Stemmer.Stemmer('portuguese');
	
	def __init__(self, text):	
		self.words = self.createBoW(text)

	def createBoW(self, text):
		import string

		#puts to lower case
		text = text.lower();
		#removing punctuation
		translator = str.maketrans({key:None for key in string.punctuation});
		text = text.translate(translator);
		#split words of text
		split_text = text.split();

		#stemming text
		stemmed_text = [];
		for word in split_text:
			stemmed_text.append(self.stemmer.stemWord(word))

		# stemmed_text = split_text;
		final_words = [];
		#removing stopwords and removing duplicity of words 
		for word in stemmed_text:
			if(not wordEmbedding.stopList.check(word)):
				try:
					final_words.index(word)
				except:
					final_words.append(word)

		return final_words

	def appendBoW(self, text):
		words = self.createBoW(text)

		for w in words:
			try: 
				self.words.index(w)
			except:
				self.words.append(w)

	def calculateCos(self,vec1,vec2):

		num = 0.0;
		den1 = 0.0;
		den2 = 0.0;
		
		for i in range(len(vec1)):
			num +=  vec1[i]*vec2[i];
			den1 += vec1[i]**2
			den2 += vec2[i]**2

		den1 **= 0.5;
		den2 **= 0.5;

		res = num/(den1*den2)

		return res;


	def compare(self, other):
		
		words1 = self.words
		words2 = other.words

		#bag of words
		bow = [];

		#preparing bag of words
		for word in words1:
			if not (word in bow):
				bow.append(word)

		for word in words2:
			if not (word in bow):
				bow.append(word)

		#bag of words ready, preparing embedding
		embeddings = [bow,[0]*len(bow),[0]*len(bow)]
		#counting 
		for word in words1:
			for bow_word in bow:
				if (word == bow_word): #or wordEmbedding.wordNet.checkSynonym(bow_word, word):
					embeddings[1][bow.index(word)] += 1
		for word in words2:
			for bow_word in bow:
				if (word == bow_word): #or wordEmbedding.wordNet.checkSynonym(bow_word, word): 
					embeddings[2][bow.index(word)] += 1

		return self.calculateCos(embeddings[1],embeddings[2]);

	def compare2(self,other):
		words1 = self.words;
		words2 = other.words;

		#bag of words
		bow = [];

		#preparing bag of words
		for word in words1:
			if not (word in bow):
				bow.append(word);

		for word in words2:
			if not (word in bow):
				bow.append(word);

		#bag of words ready, preparing embedding
		embeddings = [bow,[0]*len(bow),[0]*len(bow)]
		#counting 
		for word in words1:
			for bow_word in bow:
				if (word == bow_word) :#or wordEmbedding.wordNet.checkSynonym(bow_word, word):
					embeddings[1][bow.index(word)] += 1;
		for word in words2:
			for bow_word in bow:
				if (word == bow_word) :#or wordEmbedding.wordNet.checkSynonym(bow_word, word): 
					embeddings[2][bow.index(word)] += 1;

		print('{0:13} | {1:5} | {2:5}|'.format('Bag of Words',' doc1',' doc2'))
		for j in range(0, len(bow)):
			print('{0:13} | {1:5d} | {2:5d}|'.format(embeddings[0][j], embeddings[1][j], embeddings[2][j]))

		return self.calculateCos(embeddings[1],embeddings[2]);
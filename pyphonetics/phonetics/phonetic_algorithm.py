class PhoneticAlgorithm:
    """
    The main Phonetic Algorithm class, to ensure a unified API
    for all the included algorithms.
    """
    def phonetics(self, word):
        """Get the phonetic representation of the word."""
        pass

    def sounds_like(self, word1, word2):
        """Compare the phonetic representations of 2 words, and return a boolean value."""
        return self.phonetics(word1) == self.phonetics(word2)

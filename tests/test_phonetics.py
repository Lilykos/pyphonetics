from pyphonetics import Metaphone, Soundex, MatchingRatingApproach,\
    FuzzySoundex, Lein, RefinedSoundex


def test_metaphone():
    tests = [
        ('TSKRMNXN', 'discrimination'),
        ('HL', 'hello'),
        ('TRT', 'droid'),
        ('HPKRT', 'hypocrite'),
        ('WL', 'well'),
        ('AM', 'am'),
        ('S', 'say'),
        ('FSNT', 'pheasant'),
        ('KT', 'god')
    ]

    metaphone = Metaphone()
    for test in tests:
        assert metaphone.phonetics(test[1]) == test[0]


def test_soundex():
    tests = [
        ('R163', 'Rupert'),
        ('R163', 'Robert'),
        ('R150', 'Rubin'),
        ('A261', 'Ashcroft'),
        ('A261', 'Ashcraft'),
        ('T522', 'Tymczak'),
        ('P123', 'Pfister'),
        ('A536', 'Andrew'),
        ('W252', 'Wozniak'),
        ('C423', 'Callister'),
        ('H400', 'Hello'),
        ('M635', 'Martin'),
        ('B656', 'Bernard'),
        ('F600', 'Faure'),
        ('P620', 'Perez'),
        ('G620', 'Gros'),
        ('C120', 'Chapuis'),
        ('B600', 'Boyer'),
        ('G360', 'Gauthier'),
        ('R000', 'Rey'),
        ('B634', 'Barthélémy'),
        ('H560', 'Henry'),
        ('M450', 'Moulin'),
        ('R200', 'Rousseau')
    ]

    soundex = Soundex()
    for test in tests:
        assert soundex.phonetics(test[1]) == test[0]


def test_soundex_refined():
    tests = [
        ('T6036084', 'testing'),
        ('T6036084', 'TESTING'),
        ('T60', 'The'),
        ('Q503', 'quick'),
        ('B1908', 'brown'),
        ('F205', 'fox'),
        ('J408106', 'jumped'),
        ('O0209', 'over'),
        ('L7050', 'lazy'),
        ('D6043', 'dogs')
    ]

    soundex = RefinedSoundex()
    for test in tests:
        assert soundex.phonetics(test[1]) == test[0]
        
        
def test_soundex_homophones():
    tests = [
        ('Braz', 'Broz'),
        ('Caren', 'Caron', 'Carren', 'Charon', 'Corain', 'Coram', 'Corran', 
         'Corrin', 'Corwin', 'Curran', 'Curreen','Currin', 'Currom', 'Currum', 'Curwen'),
        ('Hairs', 'Hark', 'Hars', 'Hayers', 'Heers', 'Hiers'),
        ('Lambard', 'Lambart', 'Lambert', 'Lambird', 'Lampaert', 'Lampard', 
         'Lampart', 'Lamperd', 'Lampert', 'Lamport','Limbert', 'Lombard'),
        ('Nolton', 'Noulton')
    ]

    soundex = Soundex()
    for test in tests:
        phonetics = [soundex.phonetics(word) for word in test]
        assert len(set(phonetics)) == 1  # all phonetics are the same, so set size = 1


def test_mra():
    tests = [
        ('BYRN', 'Byrne'),
        ('BRN', 'Boern'),
        ('SMTH', 'Smith'),
        ('SMYTH', 'Smyth'),
        ('CTHRN', 'Catherine'),
        ('KTHRYN', 'Kathryn')
    ]

    mra = MatchingRatingApproach()
    for test in tests:
        assert mra.phonetics(test[1]) == test[0]


def test_fuzzy_soundex():
    tests = [
        ('Kristen', 'K6935'),
        ('Krissy', 'K69'),
        ('Christen', 'K6935'),
        ('peter', 'P36'),
        ('pete', 'P3'),
        ('pedro', 'P36'),
        ('stephen', 'S315'),
        ('steve', 'S31'),
        ('smith', 'S53'),
        ('smythe', 'S53'),
        ('gail', 'G4'),
        ('gayle', 'G4'),
        ('guillaume', 'G45'),
        ('christine', 'K6935'),
        ('christina', 'K6935'),
        ('kristina', 'K6935'),
        ('Wight', 'W3'),
        ('Hardt', 'H6'),
        ('Knight', 'N3'),
        ('Czech', 'S7'),
        ('Tsech', 'S7'),
        ('gnomic', 'N59'),
        ('Wright', 'R3'),
        ('Hrothgar', 'R376'),
        ('Hwaet', 'W3'),
        ('Grant', 'G63'),
        ('Hart', 'H6')
    ]

    fuzzy = FuzzySoundex()
    for test in tests:
        assert fuzzy.phonetics(test[0]) == test[1]


def test_lein():
    tests = [
        ('Guillaume', 'G320'),
        ('Dabbs', 'D450'),
        ('Daves', 'D450'),
        ('Davies', 'D450'),
        ('Davis', 'D450'),
        ('Debaca', 'D450'),
        ('Debose', 'D450'),
        ('Debus', 'D450'),
        ('Defazio', 'D450'),
        ('Defigh', 'D450'),
        ('Deveaux', 'D450'),
        ('Devese', 'D450'),
        ('Devies', 'D450'),
        ('Devos', 'D450'),
        ('Dipiazza', 'D450'),
        ('Divish', 'D450'),
        ('Dobak', 'D450'),
        ('Dobbs', 'D450'),
        ('Dobis', 'D450'),
        ('Dobish', 'D450'),
        ('Dobosh', 'D450'),
        ('Doepke', 'D450'),
        ('Dopps', 'D450'),
        ('Doubek', 'D450'),
        ('Doviak', 'D450'),
        ('Dubbs', 'D450'),
        ('Dubke', 'D450'),
        ('Dubois', 'D450'),
        ('Duboise', 'D450'),
        ('Dubose', 'D450'),
        ('Dubs', 'D450'),
        ('Dubukey', 'D450'),
        ('Dubus', 'D450'),
        ('Dufek', 'D450'),
        ('Duffek', 'D450'),
        ('Dupas', 'D450'),
        ('Dupois', 'D450'),
        ('Dupuis', 'D450'),
        ('Arlène', 'A332'),
        ('Lüdenscheidt', 'L125')
    ]

    lein = Lein()
    for test in tests:
        assert lein.phonetics(test[0]) == test[1]

from fuzzywuzzy import fuzz, process

def spellCheck(List, Cell, cutoff_score=50):
    # Use process.extractOne for more efficient fuzzy string matching
    result = process.extractOne(Cell.upper(), List, scorer=fuzz.ratio, score_cutoff=cutoff_score)
    
    if result:
        corrected, score = result
        return corrected, score
    else:
        return 'Manual_Input', 0

def listCheck(DataList, ManagementList, cutoff_score=50):
    output = []
    for item in DataList:
        corrected, confidence = spellCheck(ManagementList, item, cutoff_score=cutoff_score)
        output.append((corrected, confidence))
    return output
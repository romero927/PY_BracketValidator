#Bracket Validator
# Pass in a string, and validate that all Brackets of types: ( ) { } [ ] are correctly closed and opened.
# Written by Kyle Romero, hand coded (No AI) with the aid of W3Schools to refresh on Python syntax

#Set to True to see more console output
DEBUG = True;

#Value object to be stored in a Dictionary
class BracketInstance:
    def __init__(self, Start, End, Type):
        self.Start = Start;
        self.End = End;
        self.Type = Type;

#Function to Validate Brackets in a String
def ValidateBracket(InputString):
    #Instantiate your objects
    Dictionary = {};
    Key = 0; #What Dictionary Key are we currently on? Key = Current Level, Key - 1 = Previous Level, Key + 1 = Next Level
    ix = 0; #What Character in the string are we currently on?
    print("Iterating through string: ", InputString);
    if(DEBUG):print('-----------------------------------------------');
    for char in InputString:
        if(DEBUG):print("Character: ", char, " | Index: ", ix)
        if char == '(' or char == '{' or char == '[':
                #On an opening bracket, add a level
                if(DEBUG):print('Add:', char, ' : Level: ', Key);
                Dictionary[Key] = BracketInstance(ix, None, char);
                Key = Key + 1;
        elif char == ')' or char == ']' or char == '}':
            #On a closing brace
            if(Key - 1 not in Dictionary):
                #If Level doesn't exist, add level
                if(DEBUG):print('Add:', char, ' : Level: ', Key);
                Dictionary[Key] = BracketInstance(None, ix, char);
                Key = Key + 1;
            elif Key -1 in Dictionary:
                #If level does exist, reverse through Dictionary until we find or dont find a matching opening brace
                if char == ')':
                        if Dictionary[Key -1].Type == '(' :
                            #If corresponding opener found, remove from dictionary
                            if(DEBUG):print('Removed Level:', Key -1, '| Type:', Dictionary[Key -1].Type, ' | Start Index:', Dictionary[Key -1].Start, ' | Stop Index:', ix);
                            del Dictionary[Key -1];
                            Key = Key - 1;
                        else:
                            #If opener doesn't exist, add level
                            if(DEBUG):print('Add:', char, ' : Level: ', Key);
                            Dictionary[Key] = BracketInstance(None, ix, char);
                            Key = Key + 1;
                elif char == '}':
                        if Dictionary[Key -1].Type == '{' :
                            #If corresponding opener found, remove from dictionary
                            if(DEBUG):print('Removed Level:', Key -1, '| Type:', Dictionary[Key -1].Type, ' | Start Index:', Dictionary[Key -1].Start, ' | Stop Index:', ix);
                            del Dictionary[Key -1];
                            Key = Key - 1;
                        else:
                            #If opener doesn't exist, add level
                            if(DEBUG):print('Add:', char, ' : Level: ', Key);
                            Dictionary[Key] = BracketInstance(None, ix, char);
                            Key = Key + 1;
                elif char == ']':
                        if Dictionary[Key -1].Type == '[' :
                            #If corresponding opener found, remove from dictionary
                            if(DEBUG):print('Removed Level:', Key -1, '| Type:', Dictionary[Key -1].Type, ' | Start Index:', Dictionary[Key -1].Start, ' | Stop Index:', ix);
                            del Dictionary[Key -1];
                            Key = Key - 1;
                        else:
                            #If opener doesn't exist, add level
                            if(DEBUG):print('Add:', char, ' : Level: ', Key);
                            Dictionary[Key] = BracketInstance(None, ix, char);
                            Key = Key + 1;
                        
        #Iterate character tracking index     
        ix = ix+1;
        if(DEBUG):print("");
    if(DEBUG):print('-----------------------------------------------');
    if len(Dictionary) == 0:
        #If Dictionary Empty, no invalid brackets found
        print("No Invalid Brackets")
    else:
        for key in Dictionary:
            #If Dictionary Not Empty, invalid brackets found
            print("Invalid Brackets:")
            print('Type:', Dictionary[key].Type, ' | Start Index:', Dictionary[key].Start, ' | Stop Index:', Dictionary[key].End, ' | Level:', key);
            print("");
    print('-----------------------------------------------');

#-----------------------------------------
#TEST CASE 1
string = "{((()()(((()))))))}"
ValidateBracket(string);
#-----------------------------------------
#TEST CASE 2
string = "{Hello (Kyle) {How (are) you})"
ValidateBracket(string);
#-----------------------------------------
#TEST CASE 3
string = "{Hello (Kyle How are you})"
ValidateBracket(string);
#-----------------------------------------
#TEST CASE 4
string = "Hello Kyle How are you"
ValidateBracket(string);
#-----------------------------------------
#TEST CASE 5
string = "{a}[b]{(c)([{}])"
ValidateBracket(string);
#-----------------------------------------



        




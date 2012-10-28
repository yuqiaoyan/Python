/* deck.case.1.cpp		this file tests that the constructor creates a deck specified by the RME
					it will 
						check					expected output
						first card				2S
						13th card				AS
						14th card				2H
						last card				AD	*/

#include "deck.h"

int main()
{
	//create an instance of deck to test constructor 
	Deck test;
	
	if( test.deck[0].spot	==	TWO	&&	test.deck[0].suit ==	SPADES	&& //first card is 2S
		test.deck[12].spot	==	ACE &&	test.deck[12].suit	==	SPADES	&& //13th card is AS
		test.deck[13].spot	==	TWO	&&	test.deck[13].suit	==	HEARTS	&& //14th card is 2H
		test.deck[51].spot	==	ACE	&&	test.deck[51].suit	==	DIAMONDS)	//last card is AD
		return 0;
		
	cout << "first card is 2S" << SpotNames[test.deck[0].spot] << SuitNames[test.deck[0].suit];
	return -1;

}
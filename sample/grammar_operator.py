from pyauparser import *

def load():
	grm = Grammar()
	grm.properties = {
		0:Property(0, 'Name', 'Operator Example'),
		1:Property(1, 'Version', '1.0'),
		2:Property(2, 'Author', 'Esun Kim'),
		3:Property(3, 'About', 'Test Data'),
		4:Property(4, 'Character Set', 'Unicode'),
		5:Property(5, 'Character Mapping', 'Windows-1252'),
		6:Property(6, 'Generated By', 'GOLD Parser Builder 5.2.0.'),
		7:Property(7, 'Generated Date', '2012-11-27 10:34'),
	}
	grm.charsets = {
		0:CharacterSet(0, 0, ((9, 13), (32, 32), (133, 133), (160, 160), (5760, 5760), (6158, 6158), (8192, 8202), (8230, 8230), (8232, 8233), (8239, 8239), (8287, 8287), (12288, 12288))),
		1:CharacterSet(1, 0, ((45, 45),)),
		2:CharacterSet(2, 0, ((40, 40),)),
		3:CharacterSet(3, 0, ((41, 41),)),
		4:CharacterSet(4, 0, ((42, 42),)),
		5:CharacterSet(5, 0, ((47, 47),)),
		6:CharacterSet(6, 0, ((43, 43),)),
		7:CharacterSet(7, 0, ((48, 48),)),
		8:CharacterSet(8, 0, ((49, 57),)),
		9:CharacterSet(9, 0, ((48, 57),)),
	}
	grm.symbols = {
		0:Symbol(0, 'EOF', 3),
		1:Symbol(1, 'Error', 7),
		2:Symbol(2, 'Whitespace', 2),
		3:Symbol(3, '-', 1),
		4:Symbol(4, '(', 1),
		5:Symbol(5, ')', 1),
		6:Symbol(6, '*', 1),
		7:Symbol(7, '/', 1),
		8:Symbol(8, '+', 1),
		9:Symbol(9, 'Num', 1),
		10:Symbol(10, 'E', 0),
		11:Symbol(11, 'M', 0),
		12:Symbol(12, 'N', 0),
		13:Symbol(13, 'V', 0),
	}
	grm.symbolgroups = {
	}
	grm.productions = {
		0:Production(0, 10, [10, 8, 11]),
		1:Production(1, 10, [10, 3, 11]),
		2:Production(2, 10, [11]),
		3:Production(3, 11, [11, 6, 12]),
		4:Production(4, 11, [11, 7, 12]),
		5:Production(5, 11, [12]),
		6:Production(6, 12, [3, 13]),
		7:Production(7, 12, [13]),
		8:Production(8, 13, [9]),
		9:Production(9, 13, [4, 10, 5]),
	}
	grm.dfainit = 0
	grm.dfastates = {
		0:DFAState(0, None, (DFAEdge(0, 1), DFAEdge(1, 2), DFAEdge(2, 3), DFAEdge(3, 4), DFAEdge(4, 5), DFAEdge(5, 6), DFAEdge(6, 7), DFAEdge(7, 8), DFAEdge(8, 9))),
		1:DFAState(1, 2, (DFAEdge(0, 1),)),
		2:DFAState(2, 3, ()),
		3:DFAState(3, 4, ()),
		4:DFAState(4, 5, ()),
		5:DFAState(5, 6, ()),
		6:DFAState(6, 7, ()),
		7:DFAState(7, 8, ()),
		8:DFAState(8, 9, ()),
		9:DFAState(9, 9, (DFAEdge(9, 10),)),
		10:DFAState(10, 9, (DFAEdge(9, 10),)),
	}
	grm.lalrinit = 0
	grm.lalrstates = {
		0:LALRState(0, {3:LALRAction(3, 1, 1), 4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 10:LALRAction(10, 3, 4), 11:LALRAction(11, 3, 5), 12:LALRAction(12, 3, 6), 13:LALRAction(13, 3, 7)}),
		1:LALRState(1, {4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 13:LALRAction(13, 3, 8)}),
		2:LALRState(2, {3:LALRAction(3, 1, 1), 4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 10:LALRAction(10, 3, 9), 11:LALRAction(11, 3, 5), 12:LALRAction(12, 3, 6), 13:LALRAction(13, 3, 7)}),
		3:LALRState(3, {0:LALRAction(0, 2, 8), 3:LALRAction(3, 2, 8), 5:LALRAction(5, 2, 8), 6:LALRAction(6, 2, 8), 7:LALRAction(7, 2, 8), 8:LALRAction(8, 2, 8)}),
		4:LALRState(4, {0:LALRAction(0, 4, None), 3:LALRAction(3, 1, 10), 8:LALRAction(8, 1, 11)}),
		5:LALRState(5, {0:LALRAction(0, 2, 2), 3:LALRAction(3, 2, 2), 5:LALRAction(5, 2, 2), 6:LALRAction(6, 1, 12), 7:LALRAction(7, 1, 13), 8:LALRAction(8, 2, 2)}),
		6:LALRState(6, {0:LALRAction(0, 2, 5), 3:LALRAction(3, 2, 5), 5:LALRAction(5, 2, 5), 6:LALRAction(6, 2, 5), 7:LALRAction(7, 2, 5), 8:LALRAction(8, 2, 5)}),
		7:LALRState(7, {0:LALRAction(0, 2, 7), 3:LALRAction(3, 2, 7), 5:LALRAction(5, 2, 7), 6:LALRAction(6, 2, 7), 7:LALRAction(7, 2, 7), 8:LALRAction(8, 2, 7)}),
		8:LALRState(8, {0:LALRAction(0, 2, 6), 3:LALRAction(3, 2, 6), 5:LALRAction(5, 2, 6), 6:LALRAction(6, 2, 6), 7:LALRAction(7, 2, 6), 8:LALRAction(8, 2, 6)}),
		9:LALRState(9, {3:LALRAction(3, 1, 10), 5:LALRAction(5, 1, 14), 8:LALRAction(8, 1, 11)}),
		10:LALRState(10, {3:LALRAction(3, 1, 1), 4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 11:LALRAction(11, 3, 15), 12:LALRAction(12, 3, 6), 13:LALRAction(13, 3, 7)}),
		11:LALRState(11, {3:LALRAction(3, 1, 1), 4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 11:LALRAction(11, 3, 16), 12:LALRAction(12, 3, 6), 13:LALRAction(13, 3, 7)}),
		12:LALRState(12, {3:LALRAction(3, 1, 1), 4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 12:LALRAction(12, 3, 17), 13:LALRAction(13, 3, 7)}),
		13:LALRState(13, {3:LALRAction(3, 1, 1), 4:LALRAction(4, 1, 2), 9:LALRAction(9, 1, 3), 12:LALRAction(12, 3, 18), 13:LALRAction(13, 3, 7)}),
		14:LALRState(14, {0:LALRAction(0, 2, 9), 3:LALRAction(3, 2, 9), 5:LALRAction(5, 2, 9), 6:LALRAction(6, 2, 9), 7:LALRAction(7, 2, 9), 8:LALRAction(8, 2, 9)}),
		15:LALRState(15, {0:LALRAction(0, 2, 1), 3:LALRAction(3, 2, 1), 5:LALRAction(5, 2, 1), 6:LALRAction(6, 1, 12), 7:LALRAction(7, 1, 13), 8:LALRAction(8, 2, 1)}),
		16:LALRState(16, {0:LALRAction(0, 2, 0), 3:LALRAction(3, 2, 0), 5:LALRAction(5, 2, 0), 6:LALRAction(6, 1, 12), 7:LALRAction(7, 1, 13), 8:LALRAction(8, 2, 0)}),
		17:LALRState(17, {0:LALRAction(0, 2, 3), 3:LALRAction(3, 2, 3), 5:LALRAction(5, 2, 3), 6:LALRAction(6, 2, 3), 7:LALRAction(7, 2, 3), 8:LALRAction(8, 2, 3)}),
		18:LALRState(18, {0:LALRAction(0, 2, 4), 3:LALRAction(3, 2, 4), 5:LALRAction(5, 2, 4), 6:LALRAction(6, 2, 4), 7:LALRAction(7, 2, 4), 8:LALRAction(8, 2, 4)}),
	}
	grm._process_after_load()
	return grm

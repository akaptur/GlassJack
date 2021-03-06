data = [
 ['hand', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
 ['8', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
 ['9', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
 ['10', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],
 ['11', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H'],
 ['12', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
 ['13', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
 ['14', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
 ['15', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
 ['16', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
 ['17', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
 ['A,2', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
 ['A,3', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
 ['A,4', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
 ['A,5', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
 ['A,6', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
 ['A,7', 'S', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H', 'H'],
 ['A,8', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
 ['A,9', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
 ['A,A', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
 ['2,2', 'H', 'H', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'],
 ['3,3', 'H', 'H', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'],
 ['4,4', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
 ['6,6', 'H', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H', 'H'],
 ['7,7', 'P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'],
 ['8,8', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
 ['9,9', 'P', 'P', 'P', 'P', 'P', 'S', 'P', 'P', 'S', 'S'],
 ['10,10', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

card_book= {}

for col, dealer_card in enumerate(data[0][1:]):
    for row, hand in enumerate(line[0] for line in data[1:]):
        card_book[(hand, dealer_card)] = data[row+1][col+1]
